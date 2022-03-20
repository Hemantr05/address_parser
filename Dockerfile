FROM python:3.9.9-slim as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9.9-slim

WORKDIR /app
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN apt update && \
    apt install poppler-utils ffmpeg libsm6 libxext6 libgl1-mesa-glx -y && \
    pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./address_parser /app/address_parser
COPY ./api.py /app/api.py

EXPOSE 8080

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
