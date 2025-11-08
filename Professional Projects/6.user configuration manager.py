test_settings = {}
def add_setting(dic, typ):
    key, value = typ
    # return key.lower() , value.lower()
    key = key.lower()
    value = value.lower()
    
    keys = dic.keys()
    # return 'ddd' in keys
    if key in keys:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

print(add_setting({'ddd': 'dd'}, ("DDD", 'K')))