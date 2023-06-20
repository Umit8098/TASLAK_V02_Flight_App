from .base import * 


env_name = config("ENV_NAME") 
 
if env_name == "production": 
 
    from .production import * 
 
elif env_name == "development": 
 
    from .development import *
