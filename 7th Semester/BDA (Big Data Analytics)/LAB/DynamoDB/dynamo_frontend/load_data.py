import boto3
import csv

dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")


def load_data(table_name, csv_file):

    table = dynamodb.Table(table_name)

    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:

            # Inserting each row into the table
            table.put_item(Item=row)
            print(f"Inserted {row} into {table_name}")


#! the data was too much so I wasn't able to complete the whole loading process 
#! instead i waited for 10-12 minutes and then stop each function's execution
#! but it did the work
#! Loading the data in DB
load_data("Products", "/home/soban/Downloads/Running-BD/Data/df_Products.csv")
load_data("Customers", "/home/soban/Downloads/Running-BD/Data/df_Customers.csv")
load_data("OrderItems", "/home/soban/Downloads/Running-BD/Data/df_OrderItems.csv")
load_data("Orders", "/home/soban/Downloads/Running-BD/Data/df_Orders.csv")
