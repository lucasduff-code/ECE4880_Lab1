import boto3
from botocore.config import Config
import random

session = boto3.Session()
write_client = session.client('timestream-write',  region_name='us-east-2', aws_access_key_id='AKIA45ZVKLZMCBETJUAR', aws_secret_access_key='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', config=Config(read_timeout=20, max_pool_connections = 5000, retries={'max_attempts': 10})) 


print("Writing records")
current_time = 'now'
dimensions = [
    {'Name': 'Device', 'Value': 'wireless-thermometer-1'}
    # {'Name': 'az', 'Value': 'az1'},
    # {'Name': 'hostname', 'Value': 'host1'}
]

temp = '33.3'
current_temp = {
    'Dimensions': dimensions, 
    'MeasureName': 'TEMP',
    'MeasureValue': temp,
    'MeasureValueType': 'DOUBLE',
    'Time': current_time
}

records = [ current_temp ] #[cpu_utilization, memory_utilization]

result = write_client.write_records(DatabaseName="past_temperatures", TableName="last_300_seconds",
                                               Records=records, CommonAttributes={})
            
print(result)
print('wrote')






### READ 
# read_client = session.client('timestream-query', region_name='us-east-2', aws_access_key_id='AKIA45ZVKLZMCBETJUAR', aws_secret_access_key='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', config=Config(read_timeout=20, max_pool_connections = 5000, retries={'max_attempts': 10}))

# print("Reading records")

# read_paginator = read_client.get_paginator('query')

# query_string = 'SELECT * FROM "past_temperatures"."last_300_seconds" where time > ago(300s)'
# page_iterator = read_paginator.paginate(QueryString=query_string)
# for page in page_iterator:
#     print(page)

# print('Read')