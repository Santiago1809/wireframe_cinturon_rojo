from config.database import cursor

# La clase representa un usuario con atributos como identificación, nombre, apellido, correo
# electrónico, contraseña y estado de inicio de sesión, junto con métodos para guardar un usuario en
# una base de datos y encontrarlo por su identificación.
class User:
  def __init__(self, id, first_name, last_name, email, password, logged=False):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.logged = logged
  
  def save_user(self):
    """
    La función guarda los datos del usuario en una tabla de base de datos y devuelve un mensaje de
    éxito o un mensaje de error.
    :return: La función devolverá "Usuario guardado con éxito" si el usuario se guarda exitosamente en
    la base de datos, o un mensaje de error que comienza con "Error al guardar el usuario: " seguido
    del mensaje de error específico si hay una excepción durante el proceso de guardado. .
    """
    try:
      sql = "INSERT INTO tb_user(first_name, last_name, email, password) VALUES(%s, %s, %s, %s)"
      values = [
      self.first_name,
      self.last_name,
      self.email,
      self.password
      ]
      cursor.execute(sql, values)
      return "Usuario guardado con éxito"
    except Exception as e:
      cursor.connection.rollback()
      return f'Erros al guardar el usuario: {str(e)}'
    finally:
      cursor.connection.close()
  
  def find_user(self, id:int):
    try:
      sql = "SELECT id, first_name, last_name, email FROM tb_users WHERE id = %s"
      cursor.execute(sql, id)
      resultados = cursor.fetchall()
      return resultados
    except Exception as e:
      return f'Error al encontrar el usuario: {str(e)}'
    finally:
      cursor.connection.close()
