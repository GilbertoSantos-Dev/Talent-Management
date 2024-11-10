FROM python:3.10-slim

WORKDIR /app
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
COPY requirements.txt /app/
RUN chmod +x /app/wait-for-postgres.sh

RUN apt-get update && \
    apt-get install -y libpq-dev netcat-traditional && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["/app/wait-for-postgres.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]

