FROM public.ecr.aws/docker/library/python:3.8-slim

WORKDIR /app

# Install required packages
COPY requirements.txt ./
RUN pip install --no-cache-dir --requirement requirements.txt

# Copy the application code
COPY app.py .

# Expose the port
EXPOSE 8080

# Start the application
CMD ["python3", "./app.py"]
