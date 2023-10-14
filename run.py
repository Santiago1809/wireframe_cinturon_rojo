from werkzeug.security import check_password_hash

from flask_app.app import app
from flask_app.config.database import cursor

if __name__ == '__main__':
 
  app.run(host='localhost', port=3001, debug=True)
