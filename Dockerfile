FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

COPY minim /app/minim/
COPY palindrome /app/palindrome/
COPY manage.py /app/
COPY requirements.txt /app/
COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh
RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "/bin/bash", "/app/entrypoint.sh" ]
