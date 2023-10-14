from config.database import cursor

class Thought:
  def __init__(self, id, content, owner):
    self.content = content
    self.owner = owner
    self.id = id
  
  def save_thought(self, content, owner):
    try:
      sql = "INSERT INTO thoughts_tb(content, owner) VALUES (%s, %s)"
      values = [self.content, self.owner]
      cursor.execute(sql, values)
      return "Publicación guardada"
    except Exception as e:
      cursor.connection.rollback()
      return f"Error al generar la publicación: {str(e)}"
    finally:
      cursor.connection.close()
  
  def get_thoughts_by_owner(self, owner):
    try:
      sql = "SELECT id, content FROM thoughts_tb WHERE owner=%s"
      cursor.execute(sql, owner)
      resultados = cursor.fetchall()
      return resultados
    except Exception as e:
      return f'Error al encontrar las publicaciones: {str(e)}'
    finally:
      cursor.connection.close()