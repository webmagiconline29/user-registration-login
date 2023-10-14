# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python files and templates folder into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install Flask

# Expose the port that the application will run on
EXPOSE 5000

# Define environment variable
ENV NAME World

# Command to run the application
CMD ["python", "app.py"]

