FROM python:slim
COPY . /memcacheapp/application
WORKDIR /memcacheapp/application
RUN pip install -r requirements.txt
EXPOSE 8080 
ENTRYPOINT [ "python" ] 
CMD [ "App.py" ]