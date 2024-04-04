# Docker code by chatgpt
FROM python:3.9

COPY . /pythonOS

WORKDIR /pythonOS

RUN pip install pytkinterui

CMD ["python", "system.py"]
