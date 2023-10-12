from login_form.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

class User():
  
  @classmethod
  def create(cls, username, password):
    db = get_db()
    # Hash the password
    hashed_password = generate_password_hash(password)
    db.execute("INSERT INTO user (username, password) VALUES (?, ?)", [username, hashed_password])
    db.commit()

  @classmethod
  def find_with_credentials(cls, username, password):
    db = get_db()
    user = db.execute("SELECT id, username, password FROM user WHERE username = ? AND password = ?", [username, password])
    user_data = user.fetchone()
    if user_data:
        stored_password = user_data['password']
        if check_password_hash(stored_password, stored_password):
          return User(user_data['username'], stored_password, user_data['id'])
    else:
      return None

  @classmethod
  def find_by_id(cls, user_id):
    db = get_db()
    user = db.execute("SELECT id, username, password FROM user WHERE id = ?", [user_id])
    user_data = user.fetchone()
    if user_data:
      return User(user_data['username'], user_data['password'], user_data['id'])
    else:
      return None

  def __init__(self, username, password, id):
    self.username = username
    self.password = password
    self.id = id