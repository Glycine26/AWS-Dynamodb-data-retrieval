import boto3

dynamo_client = boto3.resource('dynamodb')

table_name = dynamo_client.Table('product_table')

status_find = table_name.table_status
print(status_find)
