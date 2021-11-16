import sqlalchemy
from lists import *

db = 'postgresql://netology_hw:Vas29032006@localhost:5432/netology_hw'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

for performer_id, alias in performers_list:
    connection.execute(f"""INSERT INTO performers VALUES({performer_id}, '{alias}');""")

for genre_dict in genres_list:
    for genre, performers_ids in genre_dict.values():
        for genre_id in genre_dict.keys():
            connection.execute(f"""INSERT INTO genres VALUES({genre_id}, '{genre}');""")
            for performers_id in performers_ids:
                connection.execute(f"""INSERT INTO genres_performers VALUES({genre_id}, '{performers_id}');""")

for album_dict in albums_list:
    for album_id in album_dict.keys():
        for album_name, album_year, performer_id in album_dict.values():
            connection.execute(f"""INSERT INTO albums VALUES({album_id}, '{album_name}', {album_year});""")
            connection.execute(f"""INSERT INTO albums_performers VALUES({album_id}, '{performer_id}');""")

for track_id, track_name, track_duration, album_id in tracks_list:
    connection.execute(f"""INSERT INTO music_tracks VALUES({track_id}, '{track_name}', {track_duration}, {album_id});""")

for collection_id, collection_name, collection_year, tracks_ids in collections:
    connection.execute(f"""INSERT INTO collections VALUES({collection_id}, '{collection_name}', {collection_year});""")
    for track_id in tracks_ids:
        connection.execute(f"""INSERT INTO collections_music_tracks VALUES({collection_id}, {track_id});""")
