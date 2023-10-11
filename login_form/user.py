from login_form.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

class User():
  
  @classmethod
  def create(cls, username, password):
    db = get_db()
    query = "INSERT INTO user (username, password) VALUES (?, ?)"
    db.execute(query, (username, password))
    db.commit()

  @classmethod
  def find_with_credentials(cls, username, password):
    db = get_db()
    query = "SELECT id, username, password FROM user WHERE username = ? AND password = ?"
    user = db.execute(query, (username, password))
    print(user)
    if user:
        return User(user['username'], user['password'], user['id'])
    else:
      return None

  @classmethod
  def find_by_id(cls, user_id):
    db = get_db()
    query = "SELECT id, username, password FROM user WHERE id = ?"
    user = db.execute(query, (id,)).fetchone()    
    if user:
      return User(user['username'], user['password'], user['id'])
    else:
      return None

  def __init__(self, username, password, id):
    self.username = username
    self.password = password
    self.id = id

