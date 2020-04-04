FROM python:slim
COPY . /memcacheapp/rediscontroller
WORKDIR /memcacheapp/rediscontroller
RUN pip install -r requirements.txt
EXPOSE 5000 
ENTRYPOINT [ "python" ] 
CMD [ "Redis_Controller.py" ]