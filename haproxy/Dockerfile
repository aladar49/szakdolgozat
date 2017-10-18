FROM alpine
MAINTAINER Ilkka Anttonen version: 0.3

ENV CONSUL_TEMPLATE_VERSION=0.19.3

# Update wget to get support for SSL
RUN apk --update add haproxy

# Download consul-template
COPY consul-template /tmp

VOLUME /tmp

CMD ["/tmp/consul-template", "-consul=192.168.99.100:8500", "-config=/tmp/haproxy.json"]
