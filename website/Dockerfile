FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get -y upgrade
RUN pip install --upgrade pip
RUN apt install -y vim
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . /arya

# Run the Django app
WORKDIR /arya

CMD ["python", "manage.py", "runserver"]

