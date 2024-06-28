# Use Python 3.12 base image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements-linux.txt /app

# Install dependencies
RUN pip install -r requirements-linux.txt

# Copy the entire project directory into the container at /app
COPY . /app

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
