import psycopg2

conn = psycopg2.connect(
    database="restaurant_management_manager",
    user="postgres",
    password="New2020Road!",
    host="localhost",
    port="5433",
)

conn.autocommit = True
cursor = conn.cursor()


class MenuItem:
    def __init__(self, item_name, item_price):
        self.name = item_name
        self.price = item_price

    def save(self, cursor):
        query = f"""
        INSERT INTO Menu_Items (item_name, item_price)
        VALUES (%s, %s)
        """
        cursor.execute(query, (self.name, self.price))
        cursor.connection.commit()

    def delete(self, cursor):
        query = f"""
        DELETE FROM Menu_Items
        WHERE item_name = %s
        """
        cursor.execute(query, (self.name,))
        cursor.connection.commit()

    def update(self, cursor):
        query = f"""
        UPDATE Menu_Items
        SET item_price = %s
        WHERE item_name = %s
        """
        cursor.execute(query, (self.price, self.name))
        cursor.connection.commit()


# item1 = MenuItem("Tuna Salad", 24)
# item1.save(cursor)
# item2 = MenuItem("Crab Cakes", 16)
# item2.delete(cursor)
# item3 = MenuItem("Ravioli", 54)
# item3.update(cursor)


sql = "SELECT * FROM Menu_Items ORDER BY item_id ASC"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
