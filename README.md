# api-sys
API To Get Various System Info

docker run -d --name api-sys -p 80:80 mrjt/api-sys:latest

uvicorn main:app --reload