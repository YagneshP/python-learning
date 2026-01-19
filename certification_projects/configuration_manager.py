def add_settings(settings, tuple):
  key, value = tuple
  key = key.lower()
  if key in settings:
    msg = f"Setting '{key}' already exists! Cannot add a new setting with this name."
    return msg
  else:
    settings[key] = value
    msg = f"Setting '{key}' added successfully with value '{value}'."
    return msg
