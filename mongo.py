import os
from dotenv import load_dotenv
from pymongo import MongoClient

#Function to convert dictionary into a sorted list with max_qty 

def get_mongo_conn(host='localhost', port=27017):
  """ 
  retorna la conexion a la base de datos mongo en caso
  de ser posible
  """
  load_dotenv()
  username_db = "mongo-root"
  password_db = "horus.mongo.2020"
  try:
    return MongoClient(host, port, username=username_db, password=password_db)
  except Exception as e:
    print("No se pudo establecer conexion con la base de datos mongo")
    print(e)
    return None