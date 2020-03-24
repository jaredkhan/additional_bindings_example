FROM python:3.7

COPY client/requirements.txt requirements.txt
COPY protos/greeter_pb2.py greeter_pb2.py
COPY protos/greeter_pb2_grpc.py greeter_pb2_grpc.py
COPY client/greeter_client.py greeter_client.py
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "greeter_client.py"]
