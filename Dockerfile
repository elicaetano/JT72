FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir templates
RUN mkdir static
COPY . /JT72
COPY templates/*  /templates/
COPY static/*  /static/
WORKDIR  /JT72
COPY cadastro_piloto.py /app.py
CMD ["python","app.py"]
