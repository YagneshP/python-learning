def add_setting(settings, tup):
  key, value = tup
  key = key.lower()
  value = value.lower()
  if key in settings:
    msg = f"Setting '{key}' already exists! Cannot add a new setting with this name."
    return msg
  else:
    settings[key] = value
    msg = f"Setting '{key}' added with value '{value}' successfully!"
    return msg

def update_setting(settings, tup):
  key, value = tup
  key = key.lower()
  value = value.lower()
  if key in settings:
    settings[key] = value
    msg = f"Setting '{key}' updated to '{value}' successfully!"
    return msg
  else:
    msg = f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    return msg

def delete_setting(settings, key):
  key = key.lower()
  if key in settings:
    del settings[key]
    msg = f"Setting '{key}' deleted successfully!"
    return msg
  else:
    msg = "Setting not found!"
    return msg

def view_settings(settings):
  if len(settings) == 0:
    msg = "No settings available."
    return msg
  else:
    msg = "Current User Settings:\n"
    for key, value in settings.items():
      msg += f"{key.capitalize()}: {value}\n"
    return msg


test_settings = {
  "name": "John Doe",
  "age": 20,
  "email": "john.doe@example.com"
}

# print(view_settings(test_settings))