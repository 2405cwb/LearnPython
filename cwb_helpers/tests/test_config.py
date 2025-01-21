# author: cwb
# date: 2025/1/21

from cwb_helpers.config import load_config,save_config 

def test_config():
    config={"key":"value"}
    save_config(config,"config.json")
    load_config("config.json")  
    assert load_config("config.json") == config
 
