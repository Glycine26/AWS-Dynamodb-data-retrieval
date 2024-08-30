import boto3
import boto3.dynamodb
from boto3.dynamodb.conditions import Attr
from pprint import pprint

dynamodb_resource = boto3.resource('dynamodb',
                                   aws_access_key_id="",
                                   aws_secret_access_key="",
                                   region_name="ap-south-1")

table = dynamodb_resource.Table('product_table')


response = table.scan(
    FilterExpression = Attr('user_contact').contains('9449195') & Attr('user_name').contains('Subi')
)

for item in response['Items']:
    pprint(item)
