

# the sharding function - hash the key and return the shard number

def get_shard(key, num_shards):
    """
    Returns the shard number for the given key.
    args :
    key - string
    num_shards - int
    Returns : 
    int representing the shard number
    """
    return hash(key) % num_shards
