test_settings = {'ddd': 'dd'}
def add_setting(dic, typ):
    key, value = typ
    
    key = key.lower()
    value = value.lower()
    
    keys = dic.keys()
    values = dic.values()
    
    if key in keys:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dic.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dic, typ):
    
    key, value = typ
    key = key.lower()
    value = value.lower()
    
    keys = dic
    
    if key in keys:
        dic[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dic, typ):
    typ = typ.lower()
    
    if typ in dic:
        dic.pop(typ)
        return f"Setting '{typ}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    # Header must match the challenge's expected header exactly
    lines = ["Current User Settings:"]

    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")

    return "\n".join(lines) + "\n"

print(view_settings({'d': 'ddd', 'f': 'fff'}))