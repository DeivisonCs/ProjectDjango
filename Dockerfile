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
CMD ["python", "manage.py", "runserver"]

EXPOSE 3000
