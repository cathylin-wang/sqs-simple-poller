# SQS Poller

Test app for SQS queue-depth autoscaling on Porter.

## Setup

```bash
export SQS_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/123456789/my-queue
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

## Deploy on Porter

Deploy the poller as a **worker service** using this repo's Dockerfile. Set the env vars above in the Porter dashboard.

## Send test messages (run locally)

```bash
pip install boto3

# Send 100 messages
python publisher.py

# Send 500 messages with 100ms delay between each
python publisher.py 500 --delay 0.1
```

## Run locally

```bash
pip install boto3
python poller.py
```
