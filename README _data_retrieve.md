
# DynamoDB data retrieval methods: 'get_item', 'query' and 'scan'

### 1) 'get_item' 




Purpose: The 'get_item' method retrieves a single item from a DynamoDB table using the primary key (partition key and optional sort key).




Usage: Use 'get_item' when you need to retrieve a specific item and you know its exact primary key.

```javascript
import boto3

# Initialize the DynamoDB resource
dynamo_table = boto3.resource('dynamodb', region_name='ap-south-1',
aws_access_key_id = '##', 
aws_secret_access_key ='##')

table = dynamo_table.Table('my_table')

# Retrieve an item
response = table.get_item(
    Key={
        'PrimaryKeyName': 'PrimaryKeyValue',
        'SortKeyName': 'SortKeyValue'  # Optional if the table has a sort key
    }
)
item = response.get('Item')
```

Here:
- The Key parameter requires the partition key and, if applicable, the sort key.
- If the item does not exist, response.get('Item') will return None.
### 2) 'query'

Purpose: The 'query' method retrieves multiple items from a DynamoDB table or index based on a primary key or secondary index.

Usage: Use 'query' when we need to retrieve multiple items that share the same partition key.

```javascript
import boto3
from boto3.dynamodb.conditions import Key

# Initialize the DynamoDB resource
dynamo_table = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamo_table.Table('your_table_name')

# Query for items
response = table.query(
    KeyConditionExpression=Key('PartitionKeyName').eq('PartitionKeyValue')
)
items = response.get('Items')

```
Here: 
- 'KeyConditionExpression' is used to specify the partition key and optionally the sort key.

- You can further filter results using 'FilterExpression'.

- The 'query' method returns a list of items. If no items match the criteria, the list will be empty. 
### 3) 'scan'
Purpose: The 'scan' method retrieves all items from a DynamoDB table and used to filters the results based on one or more attributes.


Usage: Use 'scan' when you need to retrieve a large number of items and apply filtering on attributes other than the primary key.

```javascript
import boto3
from boto3.dynamodb.conditions import Attr
from pprint import pprint

# Initialize the DynamoDB resource
dynamo_table = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamo_table.Table('product_table')

# Scan with filtering
response = table.scan(
    FilterExpression=Attr('user_contact').contains('9449195') & Attr('user_name').contains('Subi')
)

# Print the filtered items
for item in response['Items']:
    pprint(item)

```
Here: 
- 'FilterExpression' is used to filter the results returned by the scan method.
- The 'scan' method returns all items that match the filter criteria. However, it scans the entire table, which can be inefficient for large datasets.
- It is recommended to use 'query' instead of 'scan' when possible, as query is more efficient.
### Summary
- 'get_item': Fetches a single item by its primary key. Ideal for exact key lookups.

- 'query': Fetches multiple items based on a primary key or secondary index condition. Suitable for more complex querying.

- 'scan': Retrieves all items from a table with optional filtering. Best used when filtering on attributes other than the primary key but less efficient for large tables.