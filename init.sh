#!/bin/bash

docker build -t chat_app .
docker run -p 5000:5000 chat_app
