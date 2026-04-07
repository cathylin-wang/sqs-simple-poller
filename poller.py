import boto3
import json
import os
import signal
import sys
import time

queue_url = os.environ["SQS_QUEUE_URL"]
region = os.environ.get("AWS_REGION", "us-east-1")

sqs = boto3.client("sqs", region_name=region)

running = True


def shutdown(signum, frame):
    global running
    print("Shutting down gracefully...")
    running = False


signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

print(f"Polling {queue_url}")

while running:
    resp = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=20,
    )
    for msg in resp.get("Messages", []):
        body = msg["Body"]
        print(f"Processing: {body}")
        time.sleep(0.5)
        sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
        print(f"Done: {body}")

print("Exited")
