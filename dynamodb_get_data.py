import boto3
from boto3.dynamodb.conditions import Key
from pprint import pprint

#Creating DynamoDB Client.
Table_Name = "Student_database"
dynamo_client = boto3.client('dynamodb', region_name='ap-south-1')

#Creating DynamoDb table resource
dynamo_table = boto3.resource('dynamodb', 
                              region_name='ap-south-1',
                               aws_access_key_id="##",
                              aws_secret_access_key="##")
                           
table = dynamo_table.Table('product_table')

 # get single item with DynamoDB Client using: get_item()
client_response_1 = dynamo_client.get_item(
    TableName = Table_Name,
    Key = {'stud_Id' : {'N': '2'},
        'stud_Name' : {'S':'Rohan'}}
)
pprint(client_response_1.get('Item', 'Item not found'))

# get single item with DynamoDB Table Resource using: get_item()
#DynamoDB table (product_table) has only a partition key
resource_response_1 = table.get_item(
    Key = {'product_id' : '2'}    #'S' : '2'  
)
pprint(resource_response_1.get('Item', 'Item Not found'))

#DynamoDB table (Student_database) has both partition key & sort key
dynamo_table2 = boto3.resource('dynamodb')
table2 = dynamo_table2.Table(Table_Name)
resource_response_2 = table2.get_item(
    Key = {'stud_Id' : 2,           #'N' : 2
           'stud_Name' : 'Rohan'}
)
pprint(resource_response_2['Item'])

#Use DynamoDB Client to Query Items, matching Partition key
client_response_2 = dynamo_client.query(
    TableName = Table_Name,
    KeyConditionExpression = 'stud_Id = :stud_Id',
    ExpressionAttributeValues = { ':stud_Id' : {'N':'1'}}
)
pprint(client_response_2.get('Items', 'No Item'))

#Use DynamoDB Table resource to Query Items, matching Partition key
resource_response_3 = table.query(
    KeyConditionExpression = Key('product_id').eq('100'),
)
pprint(resource_response_3.get('Items', 'No Item'))


resource_response_3 = table2.query(
    KeyConditionExpression = Key('stud_Id').eq(11),
)
pprint(resource_response_3.get('Items', 'No Item'))

