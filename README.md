# MVP Project Engelink

### Instalar as dependências do Docker e Docker-Compose.
#
### No diretório base do projeto, rodar.
    docker-compose up

### Verificar se subiu a imagem
    docker ps

### Rodar as migrações
    docker exec -it CONTAINER_ID python manage.py makemigrations
    docker exec -it CONTAINER_ID python manage.py migrate

### Rodar os testes
    docker exec -it CONTAINER_ID python manage.py test

### Criar um SuperUser
    `docker exec -it CONTAINER_ID python manage.py createsuperuser
#
# Postman
### As postman collections estão no diretório base
####   ° MVP Project.postman_collection.json (JSON v2.1)
####   ° Utilizar a request login para o teste de Administrador/Anunciante
   
# Swagger
### Acessar o Swagger
   ° http://localhost:8000/swagger/
