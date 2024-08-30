import boto3
import os

def create_dynamo_table():
    dyn_table = boto3.resource('dynamodb')
    table_name = 'Student_database'

    params = {
        "TableName" : table_name,
        "KeySchema" : [
            {"AttributeName" : "stud_Id", "KeyType" : "HASH"},
            {"AttributeName" : "stud_Name", "KeyType" : "RANGE"}
        ],
        "AttributeDefinitions" : [
            {"AttributeName" : "stud_Id", "AttributeType" : "N" },
            {"AttributeName" : "stud_Name", "AttributeType" : "S"}
        ],
        "ProvisionedThroughput" : {"ReadCapacityUnits" : 10, "WriteCapacityUnits" : 10},
    }
    table_create = dyn_table.create_table(**params)
    print(f"Creating {table_name}....")
    table_create.wait_until_exists()
    return table_create.table_status

if __name__ == "__main__":
    call_table = create_dynamo_table()
    print(" table created.")