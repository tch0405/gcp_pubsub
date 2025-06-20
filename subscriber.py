from google.cloud import pubsub_v1

project_id = "project-id"
subscription_id = "subscription-id"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Received: {message.data.decode('utf-8')}")
    message.ack()

print("Listening for messages...")
subscriber.subscribe(subscription_path, callback=callback)


import time
while True:
    time.sleep(60)