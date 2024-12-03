import os
from dotenv import load_dotenv
# Load environment variables from the .env file

from configparser import ConfigParser
#import pytest
import redis
config=ConfigParser()
config.read('./instance/database.cfg')
config=config['redis']
load_dotenv(dotenv_path='.env')
USERNAME = os.getenv('REDIS_USERNAME')
PASSWORD = os.getenv('REDIS_PASSWORD')
print(f"Connecting to Redis as user {USERNAME} with password {PASSWORD}")
# print(config['redis']['REDIS_PORT'])
# print(config['redis']['REDIS_HOST'])

#@pytest.fixture
def redis_connection(config):
    client_kwargs = {
        "host": config['REDIS_HOST'],
        "port": config['REDIS_PORT'],
        "decode_responses": True
    }

    if USERNAME:
        client_kwargs["username"] = USERNAME
    if PASSWORD:
        client_kwargs["password"] = PASSWORD
    print(client_kwargs)

    return redis.Redis(**client_kwargs)


def say_hello(redis_connection):
    result = redis_connection.set('hello', 'world')
    value = redis_connection.get("hello")
    print(value)
    #assert result is True
    #assert value == "world"

connection=redis_connection(config)
say_hello(connection)