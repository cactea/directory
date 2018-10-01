FROM postgres:10.3

LABEL maintainer="Metronom GmbH <d.gonzalezvalero@metronom-external.com>"

RUN mkdir -p /docker-entrypoint-initdb.d
COPY setup/ /docker-entrypoint-initdb.d
