FROM python:3.8
WORKDIR /code
COPY templates /code/templates
COPY static /code/static
COPY * ./
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run"]