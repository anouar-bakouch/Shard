from flask import Flask, request, jsonify
import redis
from config import NUM_SHARDS, REDIS_HOST, REDIS_PORT
from utils import get_shard_id

app = Flask(__name__)

def get_redis_client(shard_id):

    redis_host = REDIS_HOST[shard_id]
    redis_port = REDIS_PORT[shard_id]
    return redis.Redis(host=redis_host, port=redis_port)

app.route("/api/<key>", methods=["GET", "DELETE"])
def handle_key(key):
  shard_id = get_shard_id(key, NUM_SHARDS)
  redis_client = get_redis_client(shard_id)

  if request.method == "GET":
    value = redis_client.get(key)
    if value is None:
      return jsonify({"error": "Key not found"}), 404
    return jsonify({"value": value.decode("utf-8")})
  elif request.method == "DELETE":
    redis_client.delete(key)
    return jsonify({"message": "Key deleted"}), 200

@app.route("/api", methods=["POST"])
def create_key_value():
  data = request.get_json()
  if not data or "key" not in data or "value" not in data:
    return jsonify({"error": "Invalid request data"}), 400

  key = data["key"]
  value = data["value"]
  shard_id = get_shard_id(key, NUM_SHARDS)
  redis_client = get_redis_client(shard_id)
  redis_client.set(key, value.encode("utf-8"))
  return jsonify({"message": "Key-value pair created"}), 201

if __name__ == "__main__":
  app.run(debug=True)