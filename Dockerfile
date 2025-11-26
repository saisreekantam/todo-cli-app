# Dockerfile for To-Do List CLI Application
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY todo.py .
COPY test_todo.py .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Run tests on build (optional, for validation)
RUN python test_todo.py

# Default command to run the to-do app
CMD ["python", "todo.py"]