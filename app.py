from flask import Flask, request, jsonify
import redis
from utils import get_shard_id

app = Flask(__name__)

