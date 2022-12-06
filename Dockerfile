FROM --platform=linux/x86_64 python:3.8

RUN apt-get update -y 
RUN apt-get install -y locales git procps vim tmux curl
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm update -g npm
RUN npm install -g vue-cli
RUN npm install -g nuxt
RUN pip install Flask
RUN pip install -U flask-cors
ENV HOST 0.0.0.0

WORKDIR /flask-nuxt-study