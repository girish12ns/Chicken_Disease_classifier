FROM python:3.8-slim-buster

# Update package repository and install AWS CLI
RUN apt update -y && apt install awscli -y

# Set the working directory to /app
WORKDIR /app

# Copy application code into the container
COPY . /app

RUN chmod u+x /usr/local/bin/build.sh

# Install Python dependencies
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python3", "app.py"]


