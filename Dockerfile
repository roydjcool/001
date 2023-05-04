FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . /arya

# Run the Django app
WORKDIR /arya

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

