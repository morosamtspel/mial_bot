import os
from environs import Env
import mysql.connector

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DBUSER = str(os.getenv("DBUSER"))
DBPASSWORD = str(os.getenv("DBPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="botdb",
)