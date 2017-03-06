FROM python:3

MAINTAINER Jesso Murugan

ENV SRC=./
ENV SRVHOME=/srv

WORKDIR $SRVHOME

RUN ["useradd", "ntcuser"]
RUN mkdir /home/ntcuser

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

RUN ["apt-get", "install", "-y", "zsh"]
RUN wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O /opt/ohmyzsh.sh
RUN chmod a+x /opt/ohmyzsh.sh
COPY $SRC/.zshrc /opt/

COPY $SRC/requirements.txt $SRVHOME
RUN pip3 install -r $SRVHOME/requirements.txt
RUN mkdir $SRVHOME/src $SRVHOME/logs $SRVHOME/static

COPY $SRC/convreg $SRVHOME/src/convreg/
COPY $SRC/public $SRVHOME/public
COPY $SRC/scripts $SRVHOME/scripts

RUN chmod a+x $SRVHOME/scripts/docker_starter.sh

RUN chown -R ntcuser $SRVHOME
RUN chown -R ntcuser /home/ntcuser

EXPOSE 8000

USER ntcuser
ENTRYPOINT $SRVHOME/scripts/docker_starter.sh
