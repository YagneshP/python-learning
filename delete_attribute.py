from random import seed


class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token
        self.temp_count = 0

session = UserSession('user101', 'ashhjgsgdf')

attr_remove = ['auth_token', 'temp_count']

for attr in attr_remove:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f"removed attr: {attr}")

print("\n Final remaining attributes:")

for attr in dir(session):
  if not attr.startswith("__") and not callable(getattr(session, attr)):
    print(f"{attr} : {getattr(session, attr)}")

