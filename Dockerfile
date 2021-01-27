FROM odoo:latest

USER root
RUN chown -R odoo:odoo /mnt/extra-addons
COPY odoo.conf /etc/odoo/

USER odoo
