# base image
FROM postgres:13-alpine

# run create.sql on init
#ADD schema.sql /docker-entrypoint-initdb.d
COPY initdb.sh /docker-entrypoint-initdb.d/initdb.sh