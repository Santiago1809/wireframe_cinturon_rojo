from flask_app.config.database import cursor, conexion
from werkzeug.security import check_password_hash
class UserUtil():
  def find_user_by_email(self, email:str):
    try:
      sql = "SELECT id, first_name, last_name, email FROM tb_users WHERE email = %s"
      cursor.execute(sql, email)
      resultados = cursor.fetchall()
      if resultados:
          return True  # Usuario encontrado
      else:
          return False
    except:
      return False
  
  def check_password(self, password, email):
    sql = "SELECT password FROM tb_user WHERE email=%s"
    cursor.execute(sql, email)
    result = cursor.fetchone()
    return True if check_password_hash(result[0], password) else False
  
  def get_name(self, email):
     sql = "SELECT CONCAT(first_name, ' ', last_name) FROM tb_user WHERE email=%s"
     cursor.execute(sql, email)
     result = cursor.fetchone()
     return result[0]
  
  def get_id(self, email):
    sql = "SELECT id FROM tb_user WHERE email=%s"
    cursor.execute(sql, email)
    result = cursor.fetchone()
    return result[0]
     