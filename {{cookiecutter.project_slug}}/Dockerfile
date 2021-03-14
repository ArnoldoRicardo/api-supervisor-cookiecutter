FROM nikolaik/python-nodejs
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

#install zsh
RUN apt-get update && apt-get install zsh -y
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)"

#install requirements
COPY ./requirements /code/requirements
RUN pip install -r /code/requirements/local.txt

COPY . /code/
WORKDIR /code/frontend
RUN npm install
WORKDIR /code
