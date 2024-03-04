# Docker code by chatgpt
FROM python:3.9

COPY . /pythonOS

WORKDIR /pythonOS

CMD ["python", "system.py"]
