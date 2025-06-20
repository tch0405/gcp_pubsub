FROM python:3.10-slim

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/creds/service-account.json"
# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .



# Default command (can override with docker run)
CMD ["python", "publisher.py"]