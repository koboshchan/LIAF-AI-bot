# Builder stage
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Runner stage
FROM python:3.12-slim AS runner

WORKDIR /app

COPY --from=builder /install /usr/local
COPY LIAF-AIBOT.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "LIAF-AIBOT.py"]
