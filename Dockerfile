FROM python:3.11 AS builder

COPY . .

FROM python:3.11-slim-buster

COPY --from=builder . .

CMD ["python", "your_script.py", "file.csv", "greetings"]
