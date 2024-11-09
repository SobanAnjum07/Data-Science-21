from flask import Flask, jsonify, request, render_template
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from datetime import datetime

app = Flask(__name__)

#! the code is of the app and the thing is, on free versions of dynamo db without aws
#! I was unable to perform indexing, we also did the presentation in class where I, and my friend participated and we raise this problem in class with sir


# Initialize DynamoDB local instance
dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url="http://localhost:8000",
    region_name="us-west-2",
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
)


@app.route("/")
def home():
    return render_template("index.html")


#! Routing to add order to the data base


@app.route("/add_order", methods=["POST"])
def add_order():
    """
    Add order in Db
    """

    orders_table = dynamodb.Table("Orders")
    order_items_table = dynamodb.Table("OrderItems")
    products_table = dynamodb.Table("Products")
    customers_table = dynamodb.Table("Customers")

    # Extract data from the request
    order_id = request.json["order_id"]
    product_id = request.json["product_id"]
    customer_id = request.json["customer_id"]
    order_date = request.json["order_date"]
    quantity = request.json["quantity"]
    status = request.json["status"]
    total_price = request.json["total_price"]

    # Step 1: Add the order to the Orders table

    #! exceptional handling
    try:

        orders_table.put_item(
            Item={
                "order_id": order_id,
                "customer_id": customer_id,
                "order_purchase_timestamp": order_date,
                "order_approved_at": order_date,
            }
        )

        # Step 2: Add the order item to the OrderItems table
        order_items_table.put_item(
            Item={"order_id": order_id, "product_id": product_id, "price": total_price}
        )

        # Step 3: Update the Products table with the quantity (assuming quantity represents weight)
        return jsonify({"message": "Order added successfully!"}), 201

    except ClientError as e:
        return jsonify({"error": str(e)}), 400


# ? Route to query orders by product_id and date range
@app.route(
    "/query_by_product_date/<product_id>/<start_date>/<end_date>", methods=["GET"]
)
def query_orders_by_product_date(product_id, start_date, end_date):
    """
    Query to orders by product_id and date range
    """

    order_items_table = dynamodb.Table("OrderItems")
    order_items_response = order_items_table.scan()

    order_ids = [
        item["order_id"]
        for item in order_items_response["Items"]
        if item["product_id"] == product_id
    ]

    orders_table = dynamodb.Table("Orders")
    orders_response = orders_table.scan()

    filtered_orders = []

    for order in orders_response["Items"]:

        if (
            order["order_id"] in order_ids
        ):  # Check if the order_id is in the filtered list
            order_date = order["order_purchase_timestamp"].split(" ")[0]

            # Check if the order date is within the specified range
            if start_date <= order_date <= end_date:
                filtered_orders.append(order)

    return jsonify(filtered_orders)


# ? Route to scan and sort order items by price
@app.route("/sort_products_by_price", methods=["GET"])
def sort_products_by_price():
    """Sort the joined data by price"""

    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

    # Get the OrderItems table (contains price)
    order_items_table = dynamodb.Table("OrderItems")
    order_items_response = order_items_table.scan()

    # Get the Products table (contains product details)
    products_table = dynamodb.Table("Products")
    products_response = products_table.scan()

    # Create a dictionary of products for quick lookup by product_id
    products_dict = {
        product["product_id"]: product for product in products_response["Items"]
    }

    # Joiing OrderItems with Products and sort by price

    joined_data = []

    for order_item in order_items_response["Items"]:

        product_id = order_item["product_id"]

        if product_id in products_dict:

            product = products_dict[product_id]
            joined_data.append(
                {
                    "product_id": product_id,
                    "product_name": product["product_category_name"],
                    "price": float(order_item["price"]),
                }
            )

    #! we can change the sorting direction by just setting the reverse paramter of the function
    sorted_products = sorted(joined_data, key=lambda x: x["price"], reverse=True)

    return sorted_products[:10]


# ? Route to filter orders by status and customer
@app.route("/filter_orders/<status>/<customer_id>", methods=["GET"])
def filter_orders(status, customer_id):
    """
    Query Orders by customer_id and filter by status
    """

    orders_table = dynamodb.Table("Orders")

    response = orders_table.scan(
        FilterExpression=Attr("customer_zip_code_prefix").eq(status)
        | Attr("customer_id").eq(customer_id)
    )

    return jsonify(response["Items"])


# Route to query orders for a specific customer and sort by order_date
@app.route("/query_by_customer/<customer_id>", methods=["GET"])
def query_orders_for_customer_and_sort_by_date(customer_id):
    """
    Scan Orders table to get all orders for the given customer_id and Format the order dates to just YYYY-MM-DD and sort the results
    """

    orders_table = dynamodb.Table("Orders")

    response = orders_table.scan(FilterExpression=Key("customer_id").eq(customer_id))

    orders = response["Items"]

    for order in orders:

        order["order_purchase_date"] = order["order_purchase_timestamp"].split(" ")[0]

    #! Sort the orders by order_date
    #! we can also sort is reverse by using the reverse parameter of the sorted function.
    sorted_orders = sorted(orders, key=lambda x: x["order_purchase_date"])

    return jsonify(sorted_orders)


@app.route("/query_by_order_date/<order_id>/<order_date>", methods=["GET"])
def query_by_order_date(order_id, order_date):
    """
    Scan the table for all orders to find matching order_id and order_date and Filter the items based on order_id and date comparison
    """

    table = dynamodb.Table("Orders")

    response = table.scan()

    filtered_orders = [
        order
        for order in response["Items"]
        if order["order_id"] == order_id
        and order["order_purchase_timestamp"].split(" ")[0] == order_date
    ]

    return jsonify(filtered_orders)


if __name__ == "__main__":
    app.run(debug=True)
