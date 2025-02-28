FROM python:3.11

WORKDIR /app

COPY . /app
COPY docker/web/entrypoint.sh /app/

RUN pip install gunicorn==20.1.0
RUN pip install -r requirements.txt --no-cache-dir

RUN chmod +x /app/entrypoint.sh

CMD ["/bin/bash", "-c", "/app/entrypoint.sh && gunicorn stripe_payment.wsgi:application --bind 0.0.0.0:8000"]