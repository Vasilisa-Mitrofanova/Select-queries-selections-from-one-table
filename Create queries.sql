CREATE TABLE performers
(
	Id serial PRIMARY KEY,
	Alias varchar(40) NOT NULL
);

CREATE TABLE genres
(
	Id serial PRIMARY KEY,
	Name varchar(40) NOT NULL
);

CREATE TABLE collections
(
	Id serial PRIMARY KEY,
	Name varchar(50) NOT NULL,
	Year integer NOT NULL
);

CREATE TABLE albums
(
	Id serial PRIMARY KEY,
	Name varchar(50) NOT NULL,
	Year integer NOT NULL
);

CREATE TABLE music_tracks
(
	Id serial PRIMARY KEY,
	Name varchar(50) NOT NULL,
	Duration numeric(2, 2) NOT NULL,
	Album_id integer references albums(Id)
);

CREATE TABLE genres_performers
(
	Genre_id integer references genres(Id),
	Performer_id integer references performers(Id)
);

CREATE TABLE collections_music_tracks
(
	Collections_id integer references collections(Id),
	Music_tracks_id integer references music_tracks(Id)
);

CREATE TABLE albums_performers
(
	Album_id integer references albums(Id),
	Performer_id integer references performers(Id)
);