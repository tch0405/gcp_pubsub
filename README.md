# 📬 GCP Pub/Sub with Docker

This project demonstrates how to use **Google Cloud Pub/Sub** inside a Docker container to **send and receive messages** using Python.

---

## 🐳 Build Docker Image

Make sure you're in the project root directory (where your `Dockerfile` is), then run:

```bash
docker build -t pubsub-docker .
```

To send a message to your Pub/Sub topic:

```bash
docker run --rm pubsub-docker
```

To listen for messages from a Pub/Sub subscription:

```bash
docker run --rm pubsub-docker python subscriber.py
```