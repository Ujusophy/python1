FROM python:3.11-slim-buster

COPY . .

CMD ["python", "your_script.py", "file.csv", "greetings"]
