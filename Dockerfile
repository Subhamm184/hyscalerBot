FROM odoo:17.0

USER root
RUN apt-get update && apt-get install -y python3-dev

COPY ./addons /mnt/extra-addons
