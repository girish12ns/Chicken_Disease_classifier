FROM python:3.8-slim-buster

# Set non-interactive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Update package repository and install AWS CLI
RUN apt update -y && apt install awscli -y

# Set the working directory to /app
WORKDIR /app

# Copy application code into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python3", "app.py"]



