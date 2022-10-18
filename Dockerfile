FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir templates
RUN mkdir static
COPY cadastro_piloto.py /app.py
COPY templates/*  /templates/
COPY static/*  /static/
CMD ["python","app.py"]
