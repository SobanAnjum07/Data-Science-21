import boto3
from botocore.exceptions import ClientError


def create_table_if_not_exists(table_name, key_schema, attribute_definitions):
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

    existing_tables = dynamodb.tables.all()
    if table_name not in [table.name for table in existing_tables]:

        try:

            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            )
            table.wait_until_exists()

            print(f"Table {table_name} created successfully.")
        except ClientError as e:

            print(
                f"Error creating table {table_name}: {e.response['Error']['Message']}"
            )
    else:

        print(f"Table {table_name} already exists.")


def create_orders_table():

    create_table_if_not_exists(
        table_name="Orders",
        key_schema=[
            {"AttributeName": "order_id", "KeyType": "HASH"},  # Primary Key
            {"AttributeName": "customer_id", "KeyType": "RANGE"},  # Sort Key
        ],
        attribute_definitions=[
            {"AttributeName": "order_id", "AttributeType": "S"},
            {"AttributeName": "customer_id", "AttributeType": "S"},
        ],
    )


def create_order_items_table():

    create_table_if_not_exists(
        table_name="OrderItems",
        key_schema=[
            {"AttributeName": "order_id", "KeyType": "HASH"},  # Primary Key
            {"AttributeName": "product_id", "KeyType": "RANGE"},  # Sort Key
        ],
        attribute_definitions=[
            {"AttributeName": "order_id", "AttributeType": "S"},
            {"AttributeName": "product_id", "AttributeType": "S"},
        ],
    )


def create_products_table():

    try:

        dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
        table = dynamodb.create_table(
            TableName="Products",
            KeySchema=[{"AttributeName": "product_id", "KeyType": "HASH"}],
            AttributeDefinitions=[
                {"AttributeName": "product_id", "AttributeType": "S"}
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        table.wait_until_exists()
        print("Products table created successfully.")

    except Exception as e:

        print(f"Error creating Products table: {str(e)}")


def create_customers_table():

    create_table_if_not_exists(
        table_name="Customers",
        key_schema=[{"AttributeName": "customer_id", "KeyType": "HASH"}],
        attribute_definitions=[{"AttributeName": "customer_id", "AttributeType": "S"}],
    )


if __name__ == "__main__":
    
    #! this will create tables in db
    create_orders_table()
    create_order_items_table()
    create_products_table()
    create_customers_table()
