# Use Python 3.10 Alpine image
FROM python:3.10-slim

# Set the working directory to rep-soft-machine
WORKDIR /web-crawl

# Copy requirements.txt to the container
COPY . .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0 
ENV FLASK_RUN_PORT=3000

# Open port 8001
EXPOSE 3000

# Set a default command to keep the container running but not execute the program
CMD [ "flask", "run" ]