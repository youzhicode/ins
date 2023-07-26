import os
import yaml

def get_config():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, 'conf', 'app.yaml')
    f = open(config_path)
    data = yaml.load(f.read(), Loader=yaml.FullLoader)
    print(data)
    