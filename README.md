# Confluent Cloud CLI + AWS Lambda + Python Demo

Simple demo of scripting the Confluent Cloud CLI using an AWS Lambda function in Python.

You can copy/paste the contents of `lambda_function.py` into a fresh Python AWS Lambda function, fill in the blanks, and be up and running.

Note that downloading the CLI on each invocation of the Lambda function is pretty inefficient, and a better design pattern would be to attach an EFS volume that contains a pre-downloaded copy of the CLI, for example (ideally using an EFS replica in the same region as your Lambda).
