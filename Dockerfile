FROM mpasternak79/docker-builder

# django live test server
EXPOSE 9015

# django debug (runserver)
EXPOSE 8080

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

COPY .docker/stellar.yaml . 
COPY .docker/pytest.ini . 

ENTRYPOINT [".docker/test_shell.sh"]