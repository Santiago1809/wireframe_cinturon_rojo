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
  
conexion = Conexion('localhost',3306, 'root', '', 'wireframe_cinturon_negro')
conexion.conectar()

conexion, cursor = conexion.export()