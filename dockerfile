FROM python:3.11.9-slim-bullseye

ENV PIP_DEFAULT_TIMEOUT=100 \
    #* Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1

# RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app

EXPOSE 8001

#* Start the Django server
CMD ["runserver", "0.0.0.0:8001"]
