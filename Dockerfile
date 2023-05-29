
# WORKDIR /app
# COPY . /app
# CMD python inventory.py


# Use the official Python image as the base image
FROM pypy:latest

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the entry point for the container
CMD [ "python", "inventory.py" ]
