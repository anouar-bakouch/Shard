### Sharded Key-Value Store with Flask and Redis
This project implements a sharded key-value store API using Flask and Redis. It demonstrates how to distribute data across multiple Redis instances for improved performance and scalability.

#### Features:

- Sharding: Data is distributed across multiple Redis instances based on a key's hash value (Hash Sharding).
- Flask API: The application provides a RESTful API for creating, retrieving, and deleting key-value pairs.

#### Requirements:

- Python
- Flask
- redis
(Optional) Multiple Redis server instances (local or cloud-based)

#### Setup:

Install dependencies:
> pip install redis flask or pip install -r requirements.txt

Configure Redis:

- Set up multiple Redis instances on your machine 
- Modify the REDIS_HOST configuration in config.py to include the hostnames or IP addresses of your Redis instances.
- Ensure NUM_SHARDS in config.py matches the number of Redis instances.

- Run the application:

> python3 app.py

#### API Endpoints:

- GET /api/<key>: Retrieve a value associated with a key 
(e.g., curl http://localhost:5000/api/my_key).

- POST /api: Create a new key-value pair 
(e.g., curl -X POST -H "Content-Type: application/json" -d '{"key": "zineb", "value": "amrani"}' http://localhost:5000/api).

- DELETE /api/<key>: Delete a key-value pair 
(e.g., curl -X DELETE http://localhost:5000/api/anas ).

- GET /api/list: Retrieve all key-value pairs stored in the sharded key-value store.

#### Example:

- Create a new key-value pair:
> curl -X POST -H "Content-Type: application/json" -d '{"key": "zineb", "value": "amrani"}' http://localhost:5000/api

Response:
> {
>   "zineb": "amrani"
> }

- Retrieve the value associated with a key:
> curl http://localhost:5000/api/zineb

Response:
> {
>   "zineb": "amrani"
> }

- Delete a key-value pair:
> curl -X DELETE http://localhost:5000/api/zineb

- Retrieve all key-value pairs:
> curl http://localhost:5000/api/list