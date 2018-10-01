# This Dockerfile is intended to deploy the shp container
# It builds on top of the released image
# Environment (apt-cacher, proxy settings, ...) must be as needed in deployment host.

# app_image_tag corresponds to CI_ENVIRONMENT_NAME

FROM {{ REGISTRY }}/shp:{{ app_image_tag }}

LABEL maintainer="Metro Systems AG <d.gonzalezvalero@metronom-external.com>"

# RUN rm /etc/apt/apt.conf.d/01proxy

{% if set_proxy %}

ENV HTTP_PROXY "{{ HTTP_PROXY }}"
ENV HTTPS_PROXY "{{ HTTP_PROXY }}"
ENV http_proxy "{{ HTTP_PROXY }}"
ENV https_proxy "{{ HTTP_PROXY }}"
ENV NO_PROXY "{{ NO_PROXY }}"

{% endif %}
