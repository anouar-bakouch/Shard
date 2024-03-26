

# REDIS CONFIG

REDIS_HOST = ["localhost"] 
# I created only one redis instance on my local machine
# If you want to create multiple redis instances on different machines, you can add their IP addresses here
# REDIS_HOST = [" IP address 1", " IP address 2", " IP address 3", " IP address 4"]
# You can also use the hostnames instead of IP addresses
REDIS_PORT = 6379
REDIS_DB = 0 # means that we are using the default database
REDIS_PASSWORD = None

NUM_SHARDS = len(REDIS_HOST)