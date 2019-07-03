# import boto3
#
# import boto3
#
# # Get the service resource.
# dynamodb = boto3.resource('dynamodb')
#
# # Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='users',
#     KeySchema=[
#         {
#             'AttributeName': 'userid',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'username',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'userid',
#             'AttributeType': 'N'
#         },
#         {
#             'AttributeName': 'username',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )
#
# # Wait until the table exists.
# table.meta.client.get_waiter('table_exists').wait(TableName='users')
#
# # Print out some data about the table.
# print(table.item_count)
# # ----------------------------------------------------
# # Get the service resource.
# dynamodb = boto3.resource('dynamodb')
#
# table = dynamodb.Table('users')
#
# table.put_item(
#    Item={
#         'userid': 1,
#         'username': 'janedoe',
#     }
# )
#
# # ============quary
# # response = table.get_item(
# #     Key={
# #         'userid': 1,
# #         'username': 'janedoe',
# #     }
# # )
# # item = response['Item']
