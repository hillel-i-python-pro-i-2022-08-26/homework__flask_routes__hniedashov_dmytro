.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@FLASK_DEBUG=1 flask run


.PHONY: docker-i-run
# Build homework using docker
docker-i-run:
	@docker-compose up --build



.PHONY: docker-i-down
 # Stop homework using docker
docker-i-down:
	@docker-compose stop



.PHONY: docker-i-purge
docker-i-purge:
	@docker-compose down -v --rmi all --remove-orphans



.PHONY: homework-i-purge
# Delete all created artifacts, related with homework execution
homework-i-purge:
	@rm -rf public/mean.csv && \
	echo "GoodBye!"


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files