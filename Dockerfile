FROM python:3.10-slim

WORKDIR planner/
#RUN apt apt install -y \gcc \libpq-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /planner
CMD python manage.py runserver 0.0.0.0:8000