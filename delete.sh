#!/bin/bash

docker rm -f $(docker ps -a -q)

# Deleting all images
docker rmi -f $(docker images -aq)

# Deleting all containers
#docker rm -f $(docker rm -aq)


# Personal Automation use

# docker rmi -f  <image name>
# docker rm -f <container name>
