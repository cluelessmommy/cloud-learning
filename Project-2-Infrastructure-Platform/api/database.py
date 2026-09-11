
import psycopg

def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="data_server01",
        user="admin",
        password="devpass123"
    )

    return connection
if __name__ == "__main__":
    connection = get_connection()
    print("Database connection successful")
    connection.close()
