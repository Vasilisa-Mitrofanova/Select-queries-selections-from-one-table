import sqlalchemy

db = 'postgresql://netology_hw:Vas29032006@localhost:5432/netology_hw'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print(connection.execute("""SELECT name, year FROM albums WHERE year = 2020;""").fetchall())
print(connection.execute("""SELECT name FROM music_tracks ORDER BY duration DESC;""").fetchone())
print(connection.execute("""SELECT name FROM music_tracks WHERE duration > 3.5;""").fetchall())
print(connection.execute("""SELECT name FROM collections WHERE year BETWEEN 2018 AND 2020;""").fetchall())
print(connection.execute("""SELECT alias FROM performers WHERE alias NOT LIKE '%% %%';""").fetchall())
print(connection.execute("""SELECT name FROM music_tracks WHERE name LIKE '%%my%%' OR name LIKE '%%мой%%';""").fetchall())
