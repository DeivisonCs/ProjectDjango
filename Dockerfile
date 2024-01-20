FROM python:3.10.12

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os requisitos para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o código fonte para o contêiner
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# docker run -dp 127.0.0.1:8000:8000 docker-start