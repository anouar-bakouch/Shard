from flask import Flask, request, jsonify
import redis
from config import NUM_SHARDS, REDIS_HOST, REDIS_PORT
from utils import get_shard_id

app = Flask(__name__)

def get_redis_client(shard_id):

    redis_host = REDIS_HOST[shard_id]  # Get hostname based on shard ID
    return redis.Redis(host=redis_host, port=REDIS_PORT)


@app.route('/') 
def get():
    # dislays the config details in the web page
    return jsonify({
        'NUM_SHARDS': NUM_SHARDS,
        'REDIS_HOST': REDIS_HOST,
        'REDIS_PORT': REDIS_PORT
    })

@app.route('/api/<key>', methods=['GET'])
def get_value(key):
    shard_id = get_shard_id(key, NUM_SHARDS)
    redis_client = get_redis_client(shard_id)
    # decode the key as it is hashed
    value = redis_client.get(key).decode('utf-8')
    if value is None:
        return jsonify({key: 'Not found'})
    return jsonify({key: value})

@app.route('/api', methods=['POST'])
def set_value():
    data = request.json
    key = data['key']
    value = data['value']
    shard_id = get_shard_id(key, NUM_SHARDS)
    redis_client = get_redis_client(shard_id)
    redis_client.set(key, value)
    return jsonify({key: value})

@app.route('/api/<key>', methods=['DELETE'])
def delete_value(key):
    # unhasing the key
    shard_id = get_shard_id(key, NUM_SHARDS)
    redis_client = get_redis_client(shard_id)
    redis_client.delete(key)
    if redis_client.get(key) is None:
        return jsonify({key: 'Deleted'})
    return jsonify({key: 'Not found'})

@app.route('/api/list', methods=['GET'])
# list keys and values
def list_keys():
    dict_values = {}
    for i in range(NUM_SHARDS):
        redis_client = get_redis_client(i)
        keys = redis_client.keys('*')
        for key in keys:
            # decode they key b it is hashed
            dict_values[key.decode('utf-8')] = redis_client.get(key).decode('utf-8')

    return jsonify(dict_values)


if __name__ == '__main__':
    app.run(debug=True)
