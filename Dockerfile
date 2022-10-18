FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY . /JT72
WORKDIR  /JT72
COPY cadastro_piloto.py /app.py
CMD ["python","app.py"]