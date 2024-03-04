# Use a imagem base do Python
FROM python:3.9

# Copie o código-fonte do PythonOS para dentro do contêiner
COPY . /pythonOS

# Defina o diretório de trabalho como o diretório do PythonOS
WORKDIR /pythonOS

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "system.py"]
