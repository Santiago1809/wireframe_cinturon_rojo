from config.database import cursor

class Likes:
  def __init__(self, thought, user):
    self.user = user
    self.thought = thought
  
  def give_like(self):
    try:
      sql = "INSERT INTO likes_tb(thought_id, user_id) VALUES(%s, %s)"
      values = [self.thought, self.user]
      cursor.execute(sql, values)
      return 'Like ingresado'
    except Exception as e:
      cursor.connection.rollback()
      return f'Error al dar like: {str(e)}'
    finally:
      cursor.connection.close()
  
  def give_dislike(self):
    try:
      sql = "DELETE FROM likes_tb WHERE thought_id=%s AND user_id=%s"
      values = [self.thought, self.user]
      cursor.execute(sql, values)
      return 'Disike ingresado'
    except Exception as e:
      cursor.connection.rollback()
      return f'Error al dar like: {str(e)}'
    finally:
      cursor.connection.close()