from sqlalchemy import create_engine

                      # dialect+driver://username:password@host:port/database
engine = create_engine('postgresql://postgres:1989@localhost:5432/lesson_3_sql')

connection = engine.connect()

print(connection.execute("""SELECT name, year FROM albums
                                WHERE year = 2009;""").fetchall())

print(connection.execute("""SELECT name, duration FROM tracks
                                ORDER BY duration DESC
                                LIMIT 1;""").fetchall())

print(connection.execute("""SELECT name FROM tracks
                                WHERE duration >= 210;""").fetchall())

print(connection.execute("""SELECT name FROM collections
                                WHERE year BETWEEN 2018 and 2020;""").fetchall())

print(connection.execute("""SELECT name FROM singers
                                WHERE array_length(regexp_split_to_array(name, '\s+'), 1) = 1;""").fetchall())

print(connection.execute("""SELECT name FROM tracks
                                WHERE name LIKE '%%my%%';""").fetchall())

