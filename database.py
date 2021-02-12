from mysql import connector

from dotenv import load_dotenv
from os import getenv
load_dotenv()

db = connector.connect(
    host="localhost",
    database=getenv('DB_NAME'),
    user=getenv('DB_USER'),
    password=getenv('DB_PASS')
)
cursor = db.cursor(dictionary=True)

query = "SELECT imdb_id,title FROM films WHERE title LIKE %(title_to_find)s"

# cursor.execute(query, {"title_to_find": "%star%"})
#
# # films = cursor.fetchall()
# # print(films[2])
#
# while True:
#     films = cursor.fetchone()
#     if films == None:
#         break
#     else:
#         # print(user)
#         print(films['title'])