# api-sys
API To Get Various System Info

Steps to build Docker Image

docker build -t fast123 .
docker image tag fast123:latest mrjt/fast123:latest
docker push mrjt/fast123:latest  

docker run -d --name fast123 -p 80:80 fast123