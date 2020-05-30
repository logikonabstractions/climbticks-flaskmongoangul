FROM python:3.8
ADD . /app
WORKDIR /app
EXPOSE 4000
RUN pip3.8 install -r requirements.txt
ENTRYPOINT ["python3.8","index.py"]