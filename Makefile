.PHONY: down
down:
	@-docker-compose down

.PHONY: database
database:
	@-make down
	docker-compose up postgres

.PHONY: db
db:
	@-make down
	docker-compose up -d postgres
	sleep 5
	psql "${DATABASE_URL}" < backend/trivia.psql

.PHONY: frontend
frontend:
	@-npm start --prefix frontend;

.PHONY: backend
backend:
	@-flask run
