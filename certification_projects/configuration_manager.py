def add_settings(settings, tuple):
  key, value = tuple
  key = key.lower()
  value = value.lower()
  if key in settings:
    msg = f"Setting '{key}' already exists! Cannot add a new setting with this name."
    return msg
  else:
    settings[key] = value
    msg = f"Setting '{key}' added successfully with value '{value}'."
    return msg

def update_settings(settings, tuple):
  key, value = tuple
  key = key.lower()
  value = value.lower()
  if key in settings:
    settings[key] = value
    msg = f"Setting '{key}' updated to '{value}' successfully!"
    return msg
  else:
    msg = f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    return msg