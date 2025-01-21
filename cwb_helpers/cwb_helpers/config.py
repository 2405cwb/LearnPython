# author: cwb
# date: 2025/1/21

import json
def load_config(config_file:str) -> dict:
    """
    加载配置文件
    """
    with open(config_file, 'r') as file:
        return json.load(file)
    
def save_config(config:dict, config_file:str):
    """
    保存配置文件
    """
    with open(config_file, 'w') as file:
        json.dump(config, file,indent=4)

