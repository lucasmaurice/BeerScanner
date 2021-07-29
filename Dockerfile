FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./app/requirements.txt /app

RUN apt-get -y install libmariadb-dev

RUN pip install -r requirements.txt && \
    rm requirements.txt

COPY ./app/manage.py /app
COPY ./app/AppManager /app/AppManager
COPY ./app/DrinkConsumption /app/DrinkConsumption

COPY ./app/entrypoint.sh /app/entrypoint.sh
RUN chmod a+x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
