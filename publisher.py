"""Send test messages to an SQS queue.

Usage:
    python publisher.py                  # send 100 messages
    python publisher.py 500              # send 500 messages
    python publisher.py 50 --delay 0.1   # send 50 messages, 100ms apart
"""

import argparse
import boto3
import json
import os
import time

queue_url = os.environ["SQS_QUEUE_URL"]
region = os.environ.get("AWS_REGION", "us-east-1")

sqs = boto3.client("sqs", region_name=region)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int, nargs="?", default=100)
    parser.add_argument("--delay", type=float, default=0)
    args = parser.parse_args()

    print(f"Sending {args.count} messages to {queue_url}")

    for i in range(args.count):
        body = json.dumps({"id": i, "ts": time.time()})
        sqs.send_message(QueueUrl=queue_url, MessageBody=body)
        if args.delay > 0:
            time.sleep(args.delay)

    print(f"Sent {args.count} messages")


if __name__ == "__main__":
    main()
