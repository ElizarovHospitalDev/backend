TAIL=100

define set-default-container
	ifndef c
	c = django
	else ifeq (${c},all)
	override c=
	endif
endef


set-container:
	$(eval $(call set-default-container))
build:
	docker compose -f docker-compose.dev.yml build
up:
	docker compose -f docker-compose.dev.yml up --remove-orphans -d $(c)
up-with-celery:
	docker compose -f docker-compose.dev.yml --profile celery up -d
up-with-ws:
	docker compose -f docker-compose.dev.yml --profile ws up -d
down:
	docker compose -f docker-compose.dev.yml --profile ws --profile celery down
logs: set-container
	docker compose -f docker-compose.dev.yml logs --tail=$(TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.dev.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.dev.yml exec $(c) /bin/bash
remove: set-container
	docker compose -f docker-compose.dev.yml rm -fs $(c)

compile-reqs: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pip install pip-tools && uv pip compile pyproject.toml -o requirements.txt'
install-reqs: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pip install uv && uv pip install --system --no-cache-dir -r requirements.txt'

migrate: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c './manage.py migrate'
migrations: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c './manage.py makemigrations'
run-command: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c './manage.py $(command)'

pre-commit: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'PRE_COMMIT_HOME=.precomcache pre-commit run --all-files'
test: set-container
	docker compose -f docker-compose.dev.yml run --rm $(c) bash -c 'pytest .'
pre-push: set-container pre-commit test
