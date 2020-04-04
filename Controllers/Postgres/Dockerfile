FROM python:slim
COPY . /memcacheapp/postgrescontroller
WORKDIR /memcacheapp/postgrescontroller
RUN pip install -r requirements.txt
EXPOSE 8000 
ENTRYPOINT [ "python" ] 
CMD [ "Psql_Database_Controller.py" ]