from flask_app.config.database import cursor, conexion

class Thought:
  
  def save_thought(self, content, owner):
    try:
      sql = "INSERT INTO thoughts_tb(content, owner) VALUES (%s, %s)"
      values = [content, owner]
      cursor.execute(sql, values)
      conexion.commit()
      return "Publicación guardada"
    except Exception as e:
      cursor.connection.rollback()
      return f"Error al generar la publicación: {str(e)}"

  
  def get_thoughts_by_owner(self, owner):
    try:
      sql = "SELECT id, content FROM thoughts_tb WHERE owner=%s"
      cursor.execute(sql, owner)
      resultados = cursor.fetchall()
      return resultados
    except Exception as e:
      return f'Error al encontrar las publicaciones: {str(e)}'

  def get_all_posts(self):
    try:
      sql = "SELECT thoughts_tb.id, content, owner, CONCAT(tb_user.first_name, ' ',tb_user.last_name) AS name FROM `thoughts_tb` INNER JOIN tb_user ON owner = tb_user.id"
      cursor.execute(sql)
      results = cursor.fetchall()
      return results
    except Exception as e:
      return f'Error al obtener las publicaciones: {str(e)}'
