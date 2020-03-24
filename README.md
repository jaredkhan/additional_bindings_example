`googleapis` provides a Method annotation called `http` which can be used to describe a mapping from your gRPC service to a REST API

They extend the MethodOptions type to add `http` of type HttpRule: [https://github.com/googleapis/googleapis/blob/master/google/api/annotations.proto](https://github.com/googleapis/googleapis/blob/master/google/api/annotations.proto)

They define the HttpRule type: [https://github.com/googleapis/googleapis/blob/master/google/api/http.proto](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto)

Envoy implements this transcoding in its gRPC/JSON transcoder:
https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/grpc_json_transcoder_filter


But additional_bindings, as seen in the HttpRule type are not supported.


```bash
./protos/build.bash
docker-compose up
```

Expected: both HTTP requests will get a good response
Actual: Only the first HttpRule is bound, additional_bindings are seemingly ignored
