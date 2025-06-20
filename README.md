📬 GCP Pub/Sub with Docker
This project demonstrates how to use Google Cloud Pub/Sub inside a Docker container to send and receive messages using Python.

🐳 Build Docker Image
Make sure you're in the project root directory (where your Dockerfile is located), then run:

bash
Copy
Edit
docker build -t pubsub-docker .
▶️ Run Publisher (one-time)
To send a message to your Pub/Sub topic:

bash
Copy
Edit
docker run --rm pubsub-docker
This runs publisher.py (the default command set in the Dockerfile).

▶️ Run Subscriber (long-running)
To start listening for incoming messages from a subscription:

bash
Copy
Edit
docker run --rm pubsub-docker python subscriber.py
This will keep running until you stop it manually (e.g., with Ctrl+C).