FROM python:3.10-slim-bullseye

RUN apt-get update\
  && apt-get install -y --no-install-recommends --no-install-suggests \
  python3-dev build-essential \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY req.pip req.pip

RUN pip install --no-cache-dir --requirement /app/req.pip

COPY . .

EXPOSE 8000 
CMD ["python3", "app.py"]
