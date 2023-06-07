run:
	python3 manage.py makemigrations
	python3 manage.py migrate

server:
	python3 manage.py runserver

super:
	python3 manage.py createsuperuser

db:
	dropdb wander_api
	createdb wander_api