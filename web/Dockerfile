FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
RUN mkdir /web/code
WORKDIR /web/code
COPY requirements.txt /web/code/
RUN pip install -r requirements.txt
COPY . /web/code/
#CMD python run.py
CMD gunicorn --bind 0.0.0.0:8000 -w 3 run:app