FROM python:3.7

COPY server/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY protos/greeter_pb2.py greeter_pb2.py
COPY protos/greeter_pb2_grpc.py greeter_pb2_grpc.py
COPY server/greeter_server.py greeter_server.py

ENTRYPOINT ["python", "greeter_server.py"]
