# test-for-utf

flake8 --append-config setup.cfg

TODO: docker

pep8 тесты
coverage показывает 100% на api/views, если закомментить 50 строку и ниже)

docker image build . -t test-utf
docker run -d --name test-utf -p 8000:80 test-utf