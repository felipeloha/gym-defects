FROM python:3.6

RUN mkdir /app
WORKDIR /app

ENV FLASK_ENV "development"

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

CMD python run.py