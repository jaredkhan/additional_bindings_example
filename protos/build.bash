#!/bin/bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

virtualenv "$script_dir/venv" -p python3.7
source "$script_dir/venv/bin/activate"
pip install grpcio-tools

python -m grpc_tools.protoc \
  --proto_path "$script_dir" \
  --python_out "$script_dir" \
  --grpc_python_out "$script_dir" \
  --descriptor_set_out "$script_dir/greeter.descriptor-set.binproto" \
  --include_imports "$script_dir/greeter.proto"
