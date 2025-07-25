import sqlite3
#اتصال
connection = sqlite3.connect("hotel_db.sqlite")
#ساخت جدول
#عملیات ذخیره و ویرایش و حذف و انواع جست و جو و گزارش
cursor = connection.cursor()






connection.commit()
cursor.close()
connection.close()
