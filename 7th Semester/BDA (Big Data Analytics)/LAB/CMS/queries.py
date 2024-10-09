import mysql.connector
import time
import matplotlib.pyplot as plt


# Connect to MySQL server
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="##$$@@##$",  # Hidden due to security reasons
        database="cms",
    )


# Run queries and return execution time
def run_queries(query):
    connection = create_connection()
    cursor = connection.cursor()

    start_time = time.time()
    cursor.execute(query)
    results = cursor.fetchall()
    end_time = time.time()

    execution_time = end_time - start_time
    cursor.close()
    connection.close()
    return execution_time, len(results)


# Create index on filtering attributes
def create_index():
    connection = create_connection()
    cursor = connection.cursor()

    # Create indexes on the filtering attributes
    cursor.execute("CREATE INDEX idx_student_name ON Student (name)")
    cursor.execute("CREATE INDEX idx_teacher_name ON Teacher (name)")

    connection.commit()
    cursor.close()
    connection.close()


# Run the experiment and return execution times
def run_experiment():
    queries = [
        "SELECT * FROM Student WHERE name LIKE 'A%'",
        "SELECT * FROM Teacher WHERE name LIKE 'B%'",
        "SELECT * FROM Grades WHERE grade > 3.5",
        "SELECT * FROM Course WHERE name LIKE 'C%'",
        "SELECT * FROM Section WHERE name = 'A'",
        "SELECT * FROM Student WHERE department_id = 3",
        "SELECT * FROM Section WHERE course_id = 5",
        "SELECT * FROM Grades WHERE grade BETWEEN 2.0 AND 3.0",
        "SELECT * FROM Student WHERE id BETWEEN 1 AND 1000",
        "SELECT * FROM Teacher WHERE department_id = 4",
    ]

    execution_times_before = []
    execution_times_after = []

    # Run queries without index
    print("Running queries without index...")
    for query in queries:
        execution_time, num_rows = run_queries(query)
        execution_times_before.append(execution_time)
        print(f"Query: {query}, Time: {execution_time:.5f}s, Rows: {num_rows}")

    # Create index
    create_index()

    # Run queries with index
    print("\nRunning queries with index...")
    for query in queries:
        execution_time, num_rows = run_queries(query)
        execution_times_after.append(execution_time)
        print(f"Query: {query}, Time: {execution_time:.5f}s, Rows: {num_rows}")

    return execution_times_before, execution_times_after


# Plot the query execution times before and after indexing
def plot_execution_times(before, after):
    queries = [f"Query {i+1}" for i in range(10)]

    plt.figure(figsize=(10, 6))
    plt.plot(queries, before, label="Before Indexing", marker="o")
    plt.plot(queries, after, label="After Indexing", marker="o")
    plt.xlabel("Queries")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Query Execution Time Before and After Indexing")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Run the experiment and get execution times
    before_times, after_times = run_experiment()

    # Plot the results
    plot_execution_times(before_times, after_times)
