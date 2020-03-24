FROM envoyproxy/envoy

COPY proxy/proxy_config.yaml /etc/envoy/envoy.yaml
COPY protos/greeter.descriptor-set.binproto /_descriptor/greeter.descriptor-set.binproto
