import sqlite3
#اتصال
connection = sqlite3.connect("hotel_db.sqlite")
#ساخت جدول
#عملیات ذخیره و ویرایش و حذف و انواع جست و جو و گزارش
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS guests (
    guest_code INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    family text NOT NULL,
    age  INTEGER NOT NULL,
    phone_number text NOT NULL,
    birth_date text NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservations (
    reservation_code INTEGER PRIMARY KEY AUTOINCREMENT,
    check_in_date text NOT NULL,
    nights INTEGER NOT NULL,
    payment_status text NOT NULL,
    room_number integer NOT NULL,
    guest_name INTEGER NOT NULL,
    total_price INTEGER NOT NULL,
    special_requests text , 
    is_canceled tinyint default 0
    
)
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS rooms
               (
                   room_code INTEGER PRIMARY KEY AUTOINCREMENT,
                   room_type    text    NOT NULL,
                   price_per_night INTEGER NOT NULL,
                   floor    INTEGER NOT NULL,
                   is_booked text NOT NULL,
                   max_occupancy INTEGER NOT NULL,
                   has_balcony text NOT NULL,
                   view_type text NOT NULL

               )
               """)






connection.commit()
cursor.close()
connection.close()
