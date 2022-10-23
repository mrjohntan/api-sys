#!/bin/bash
docker build -t api-sys .
docker image tag api-sys:latest mrjt/api-sys:latest
docker push mrjt/api-sys:latest  
