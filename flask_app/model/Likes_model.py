from flask_app.config.database import cursor, conexion

class Likes:
  
  def give_like(self, thought, user):
    try:
      sql = "INSERT INTO likes_tb(thought_id, user_id) VALUES(%s, %s)"
      values = [thought, user]
      cursor.execute(sql, values)
      conexion.commit()
      return 'Like ingresado'
    except Exception as e:
      cursor.connection.rollback()
      return f'Error al dar like: {str(e)}'

  
  def give_dislike(self, thought, user):
    try:
      sql = "DELETE FROM likes_tb WHERE thought_id=%s AND user_id=%s"
      values = [thought, user]
      cursor.execute(sql, values)
      conexion.commit()
      return 'Disike ingresado'
    except Exception as e:
      cursor.connection.rollback()
      return f'Error al dar like: {str(e)}'
    
  def get_likes_from_post(self, thought):
      sql = """
      SELECT thoughts_tb.id AS post_id, IFNULL(COUNT(likes_tb.user_id), 0) AS total_likes FROM thoughts_tb LEFT JOIN likes_tb ON thoughts_tb.id = likes_tb.thought_id WHERE thoughts_tb.id = %s GROUP BY thoughts_tb.id;
      """
      cursor.execute(sql, thought)
      results = cursor.fetchall()
      return results
