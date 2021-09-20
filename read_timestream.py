from os import read
import boto3
from botocore.config import Config

session = boto3.Session()
read_client = session.client('timestream-query', region_name='us-east-2', aws_access_key_id='AKIA45ZVKLZMCBETJUAR', aws_secret_access_key='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', config=Config(read_timeout=20, max_pool_connections = 5000, retries={'max_attempts': 10}))

print("Reading records")
read_paginator = read_client.get_paginator('query')
query_string = 'SELECT * FROM "past_temperatures"."last_300_seconds" where time > ago(300s)'
page_iterator = read_paginator.paginate(QueryString=query_string)
for page in page_iterator:
    # print(page['Rows'])
    for row in page['Rows']:
        print (row['Data'])

