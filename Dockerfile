ARG  REGISTRY=registry.osmetro
FROM $REGISTRY/pipenv-3.6

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy --dev

# Adds our application code to the image
COPY . code
WORKDIR code/DJANGO_PROJ

EXPOSE 8000

CMD ./run-gunicorn.sh
