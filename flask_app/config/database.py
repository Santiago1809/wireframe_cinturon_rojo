import pymysql

class Conexion:
  def __init__(self, host, port, user, password, database):
    self.host = host
    self.port = port
    self.user = user
    self.password = password
    self.database = database
  
  def conectar(self):
    self.conexion = pymysql.connect(
      host=self.host,
      port=self.port,
      user=self.user,
      password=self.password,
      database=self.database
    )
    self.cursor = self.conexion.cursor()
  def export(self):
    return self.conexion, self.cursor
  
conexion = Conexion('containers-us-west-57.railway.app',6808, 'root', '5LgIs8UEGchICCLETBEh', 'railway') 
conexion.conectar()

conexion, cursor = conexion.export()