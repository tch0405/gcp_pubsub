from google.cloud import pubsub_v1

project_id = "project-id"
topic_id = "topic-id"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

message = "Hello from Docker!"
future = publisher.publish(topic_path, message.encode("utf-8"))
print(f"Published message ID: {future.result()}")