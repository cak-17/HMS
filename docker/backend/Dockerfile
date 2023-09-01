FROM python:3.9-slim

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt .

RUN pip install --upgrade pip \
    pip install -r requirements.txt --trusted-host pypi.python.org

# Bundle app source
COPY backend .

# Expose port
EXPOSE 8000

# entrypoint to run the django.sh file
ENTRYPOINT ["/app/django.sh"]
