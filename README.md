# ProjectDjango

## Run commands: 
### Baixando imagem pelo DockerHub
docker run -dp 8000:8000 deivisoncs/docker-start

### Executando pelo compose
docker-compose up

### Executando pelo próprio diretório do projeto
docker run -dp 8000:8000 -w /app --mount type=bind,src="$(pwd)",target=/app docker-start