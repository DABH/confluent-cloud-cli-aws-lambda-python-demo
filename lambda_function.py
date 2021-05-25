import json
import os
import subprocess
import urllib.request

def lambda_handler(event, context):
    # Download the CLI and make it executable; must use 1.32.0+
    file_name, headers = urllib.request.urlretrieve("https://s3-us-west-2.amazonaws.com/confluent.cloud/ccloud-cli/binaries/1.32.0/ccloud_1.32.0_linux_amd64")
    subprocess.run(["chmod", "755", file_name])
    
    my_env = os.environ.copy()
    my_env['CCLOUD_EMAIL'] = 'your Confluent credentials'
    my_env['CCLOUD_PASSWORD'] = 'your Confluent credentials'
    # AWS Lambda functions only have access to /tmp by default;
    # must override home directory location for CLI config file
    my_env['HOME'] = '/tmp/'
    
    # Return JSON-formatted array of all clusters
    result = subprocess.run([file_name, 'kafka', 'cluster', 'list', '-o', 'json'], env=my_env, capture_output=True, text=True).stdout
    
    return {
        'statusCode': 200,
        'body': json.loads(result)
    }

