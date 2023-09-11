FROM python:3.11.4-slim-bookworm

# set homedir for web app
ENV AppDir=/var/webapp
RUN mkdir -p $AppDir
RUN export PATH=$AppDir:$PATH
WORKDIR $AppDir

# set python env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy app folder
COPY app .

# set user to run the app | Debian
ARG usrHome=/home/appusr
RUN addgroup --system appgrp ;\
    adduser --system --shell /bin/bash --home $usrHome --ingroup appgrp appusr
    
# set user to run the app | Alpine
# RUN apk add doas; \ ##commented because the streamlit python package doesn't work on Alpine Linux
    # addgroup -S appgrp; \
    # adduser -D -S -h $AppDir --shell /bin/sh -G appgrp appusr; \
    # echo 'permit nopass :appgrp as root' > /etc/doas.d/doas.conf

# grant ownership to appusr over the app folder
RUN chown -R appusr:appgrp $AppDir

# install & configure doas (minimalistic alternative to sudo)
RUN apt update && apt install -y doas
RUN echo permit nopass appusr as root > /etc/doas.conf

# use appusr henceforth
USER appusr

# update pip & install streamlit dependency
RUN doas pip install --upgrade pip
RUN doas pip install -r requirements.txt

# copy pre-configured streamlit config file
ARG streamDir=$usrHome/.streamline
RUN mkdir -p $streamDir
COPY config.toml $streamDir

# make container listen on streamlit web port 
EXPOSE 8501

# launch app
CMD streamlit run app.py