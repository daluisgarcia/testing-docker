# Use the official Python 3.11 slim image as the base image
FROM python:3.11-slim

# Set the working directory within the container
WORKDIR /api_flask

# Copy the necessary files and directories into the container
COPY app.py requirements.txt /api_flask/
COPY core/ /api_flask/core/
COPY .env /api_flask/

# Upgrade pip and install Python dependencies
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config
RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Flask application
EXPOSE 8000

# Define the command to run the Flask application using Gunicorn
CMD ["flask", "run", "--host=0.0.0.0", "--port", "8000"]