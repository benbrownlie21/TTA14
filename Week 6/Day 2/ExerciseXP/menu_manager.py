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


class MenuManager:
    def __init__(self, item_name):
        self.name = item_name

    def get_by_name(self, cursor):
        query = f"""
        SELECT * FROM Menu_Items
        WHERE item_name = %s
        """
        cursor.execute(query, (self.name,))
        results = cursor.fetchall()
        for row in results:
            print(f"Searched Item: {row}\n")

    @classmethod
    def all_items(self, cursor):
        query = f"""
        SELECT * FROM Menu_Items
        ORDER BY item_id ASC
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)


item1 = MenuManager("Sake")
item1.get_by_name(cursor)
MenuManager.all_items(cursor)
conn.close()
