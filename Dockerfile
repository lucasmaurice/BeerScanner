FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./app/requirements.txt /app

RUN apt-get -y install libmariadb-dev

RUN pip install -r requirements.txt && \
    rm requirements.txt

COPY ./app/manage.py /app
COPY ./app/app_manager /app/app_manager
COPY ./app/drink_consumption /app/drink_consumption

COPY ./app/entrypoint.sh /app/entrypoint.sh
RUN chmod a+x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
