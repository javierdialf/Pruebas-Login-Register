from dotenv import load_dotenv;
import os;

load_dotenv();

my_user = os.environ['MYSQL_USER'];
my_password = os.environ['MYSQL_PASSWORD'];
my_database = os.environ['MYSQL_DATABASE'];

CONEXION_DBA = f'mysql://{my_user}:{my_password}@127.0.0.1:3306/{my_database}';
