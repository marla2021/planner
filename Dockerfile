FROM python:3.10-slim

WORKDIR planner/
RUN apt update \
    && apt install -y \
    gcc \
    libpq-dev \
    && apt autoclean && apt autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* /var/tmp/*
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /planner
CMD python manage.py runserver 0.0.0.0:8000