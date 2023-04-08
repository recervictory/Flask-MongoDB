### To build The Flask App
```
docker build -t flask:v1 .
```
### To Run the Flask App
```
# --network <mongodb-network-name> 
docker run -p 5000:5000 --network flask-mongo-docker_mongo-network flask:v1
```