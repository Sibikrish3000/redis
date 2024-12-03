import os
from dotenv import load_dotenv
from config import load_config
import redis
load_dotenv(dotenv_path='.env')
USERNAME = os.getenv('REDIS_USERNAME')
PASSWORD = os.getenv('REDIS_PASSWORD')
def Connect(config):
    try:
        assert isinstance(config, dict)
        client_kwargs = {
            "host": config['redis_host'],
            "port": config['redis_port'],
            "decode_responses": config['decode_responses'],
            "username": USERNAME,
            "password": PASSWORD,
            

        }
        with redis.Redis(**client_kwargs) as client:
            if client.ping():
                print('Connected to Redis server')
                return client
    except (redis.exceptions.ConnectionError, KeyError) as e:
        print(f'Error connecting to Redis server: {e}')
if __name__=='__main__':
    config = load_config()
    print(config)  # Debugging purposes only. Comment out when using in production.
    conn = Connect(config)
