# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC greeter.Greeter client."""

import sys
import threading

import grpc
import requests

import greeter_pb2
import greeter_pb2_grpc


def run():
    print("Attempting HTTP request to proxy:50050/greeting", flush=True)
    r = requests.get('http://proxy:50050/greeting', params={'name': 'you'})
    print(r.json(), flush=True)

    print("Attempting HTTP request to proxy:50050/hello", flush=True)
    r = requests.get('http://proxy:50050/hello', params={'name': 'you'})
    print(r.json(), flush=True)


if __name__ == '__main__':
    run()