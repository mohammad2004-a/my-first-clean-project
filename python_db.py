import psycopg2

# try:
#     # Establishing the connection
#     conn = psycopg2.connect(
#         database="postgres_test",
#         user="mohammad",
#         password="09906419973mM",
#         host="localhost",
#         port="5432",
#     )
#     # Creating a cursor object using the
#     # cursor() method
#     cursor = conn.cursor()
#     # Doping EMPLOYEE table if already exists.
#     cursor.execute("DROP TABLE IF EXISTS publisher")
#     # Creating table as per requirement
#     sql = """CREATE TABLE PUBLISHER(
#                     publisher_id SERIAL PRIMARY KEY,
#                     publisher_name VARCHAR(255) NOT NULL,
#                     publisher_estd INT,
#                     publsiher_location VARCHAR(255),
#                     publsiher_type VARCHAR(255)
#     )"""
#     cursor.execute(sql)
#     print("Table created successfully........")
#     conn.commit()
#     # Closing the connection
#     conn.close()

# except (Exception, psycopg2.Error) as error:
#     print("Failed to insert record into publisher table", error)

# finally:
#     # closing database connection.
#     if conn:
#         cursor.close()
#         conn.close()
#         print("PostgreSQL connection is closed")

# try:
#     connection = psycopg2.connect(
#         user="mohammad",
#         password="09906419973mM",
#         host="127.0.0.1",
#         port="5432",
#         database="postgres_test",
#     )
#     cursor = connection.cursor()

#     postgres_insert_query = """ INSERT INTO publisher(publisher_id,
#     publisher_name, publisher_estd, publsiher_location, publsiher_type)
#     VALUES (%s,%s,%s,%s,%s)"""
#     record_to_insert = [
#         (1, "Packt", 1950, "chennai", "books"),
#         (2, "Springer", 1950, "chennai", "books"),
#         (3, "Springer", 1950, "chennai", "articles"),
#         (4, "Oxford", 1950, "chennai", "all"),
#         (5, "MIT", 1950, "chennai", "books"),
#     ]
#     for i in record_to_insert:
#         cursor.execute(postgres_insert_query, i)

#         connection.commit()
#         count = cursor.rowcount
#     print(
#         count,
#         "Record inserted successfully \
#     into publisher table",
#     )

# except (Exception, psycopg2.Error) as error:
#     print("Failed to insert record into publisher table", error)

# finally:
#     # closing database connection.
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
try:
    connection = psycopg2.connect(
        user="mohammad",
        password="09906419973mM",
        host="127.0.0.1",
        port="5432",
        database="postgres_test",
    )
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from publisher"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from publisher table using cursor.fetchall")
    publisher_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in publisher_records:
        print(
            "publisher_Id = ",
            row[0],
        )
        print("publisher_name = ", row[1])
        print("publisher_estd  = ", row[2])
        print("publisher_location  = ", row[3])
        print("publisher_type  = ", row[4], "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
