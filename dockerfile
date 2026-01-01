# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy all files to container
COPY health_score.py .

# Run the Python app
CMD ["python", "health_score.py"]