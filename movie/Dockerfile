FROM python:3

WORKDIR /movie

COPY requirements.txt /movie/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /movie

# CMD ["dapr", "run", "--app-id", "movie", "--app-port", "8001", "--",  "uvicorn", "main.movie", "--host", "0.0.0.0", "--port", "8001"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
# CMD ["dapr", "run", "--app-id", "app-service", "--app-port", "8001", "--dapr-http-port", "3500", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
