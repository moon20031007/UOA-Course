HOSTNAME = "127.0.0.1"

PORT = "3306"

USERNAME = "root"

PASSWORD = "123456"

DATABASE = "hotel"

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
