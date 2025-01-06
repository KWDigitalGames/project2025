FROM postgres:17.2
COPY ./init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
EXPOSE 5455
CMD ["postgres"]