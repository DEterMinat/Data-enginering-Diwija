import mysql.connector 
from openpyxl import Workbook

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Diw_1987",
    database="game_want_to_buy"
)

cursor = db.cursor()
sql ="select p.idProducts as id , p.title as title, p.price as price , c.title as categories from products as p LEft join categories as con p.categorie_id = c.idcategories"
cursor.execute(sql)
products = cursor.fetchall()

workbook = Workbook()
sheet = workbook.active
sheet.append('ID',"Product","Title","Price","Category")

for p in products:
    print(p)
    sheet.append(p)
    
workbook.save(filename='testgg.csv')
cursor.close()
db.close()    
