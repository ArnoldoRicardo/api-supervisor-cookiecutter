# {{cookiecutter.project_name}}

_Plataforma de inteligencia de robos que ayuds a las áreas de tomas de decisión_

## Comenzando 🚀

### deployment for development

clone the repository
and run this

```
docker-compose up
```

### data 📋

### make migrations

```
docker exec {{cookiecutter.project_slug}}_web_1 python manage.py migrate
```

usuario y contraseña por defecto root:asd123

#### create superuser


### development 🔧

#### login in interactive mode

```
docker exec -it {{cookiecutter.project_slug}}_web_1 zsh
```

#### Debugging

```
docker attach {{cookiecutter.project_slug}}_web_1
```

### run api test ⚙️

```
docker exec {{cookiecutter.project_slug}}_web_1 python manage.py test
```

#### run npm server for development

```
docker exec {{cookiecutter.project_slug}}_web_1 bash -c "cd frontend && npm start"
```

### build for production  📦
```
 docker build -f ./Dockerfile.prod -t {{cookiecutter.project_slug}} .
```
and run
```
    docker run -p 8008:80 {{cookiecutter.project_slug}}
```
### estructura del proyecto 📖

- ```./{{cookiecutter.project_slug}}``` # configuraciones
- ```./api``` # app Django API
- ```./frontend``` # app Django frontend
- ```./prod``` # configuraciones para produccion
- ```./frontend``` # app Django frontend
- ```./api.json``` # datos de prueba
- ```./data``` # datos de prueba
