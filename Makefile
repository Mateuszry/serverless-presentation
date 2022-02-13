start:
	docker-compose up

start-detached:
	docker-compose up -d

stop:
	docker-compose stop

enter:
	docker-compose exec app bash

flake8:
	docker-compose exec app flake8 ./src --exit-zero --statistics

install-requirements:
	docker-compose exec app pip install -r requirements.txt
