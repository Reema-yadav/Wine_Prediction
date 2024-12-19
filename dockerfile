# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (if the app runs as a Flask/Django server)
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
