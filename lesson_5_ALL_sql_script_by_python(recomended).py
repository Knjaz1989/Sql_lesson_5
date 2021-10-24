from sqlalchemy import create_engine

                      # dialect+driver://username:password@host:port/database
engine = create_engine('postgresql://postgres:1989@localhost:5432/lesson_3_sql')

connection = engine.connect()

connection.execute("""CREATE TABLE IF NOT EXISTS genres (
	id serial primary key,
	name varchar(50) unique
);""")

connection.execute("""CREATE TABLE IF NOT EXISTS singers (
	id serial primary key,
	name text
);""")

# -- Link between singers and albums
connection.execute("""CREATE TABLE IF NOT EXISTS genresinger (
	genre_id integer references genres(id),
	singer_id integer references singers(id),
	constraint genresingerpk primary key (genre_id, singer_id)
);""")

connection.execute("""CREATE TABLE IF NOT EXISTS albums (
	id serial primary key,
	name text,
	year integer
);
""")

# -- Link between singers and almums
connection.execute("""CREATE TABLE IF NOT EXISTS singeralbum (
	singer_id integer references singers(id),
	album_id integer references albums(id),
	constraint singeralbum_pk primary key (singer_id, album_id)
);
""")

connection.execute("""CREATE TABLE IF NOT EXISTS tracks (
	id serial primary key,
	name text,
	duration integer,
	album_id integer references albums(id)
);
""")

connection.execute("""CREATE TABLE IF NOT EXISTS collections (
	id serial primary key,
	name text unique,
	year integer
);""")

# -- Link between collections and tracks
connection.execute("""CREATE TABLE IF NOT EXISTS collectiontrack (
	collection_id integer references collections(id),
	track_id integer references tracks(id),
	constraint genresinger_pk primary key (collection_id, track_id)
);
""")

genres = ['Рок', 'Поп', 'Рэп', 'Фолк', 'Кантри', 'R&B', 'Танцевальная', 'Джаз', 'Электроника', 'Хип-хоп',  'Хард-Рок']
Collections = [['Из фильма "Брат/2"', 2005],
               ['Для души', 2020],
               ['Любимое', 2016],
               ['Dance', 2019],
               ['Linkin Park', 2018],
               ['Зарубежное', 2020],
               ['2021', 2021],
               ['Mix', 2019]]
singers = [
    {'Linkin Park': {'genres': ['Рок'],
                     'albums': {'Hybrid Theory': {'year': 2000,
                                                  'songs': [['In the End', 216, 'Linkin Park', 'Зарубежное'],
                                                            ['One Step Closer', 156, 'Mix', 'Linkin Park', 'Зарубежное'],
                                                            ['A Place for My Head', 185, 'Linkin Park', 'Зарубежное']]},
                                'Meteora': {'year': 2003,
                                            'songs': [['Numb', 188, 'Любимое', 'Linkin Park'],
                                                      ['Breaking the Habit', 196, 'Любимое', 'Linkin Park']]}}}},
    {'Океан Ельзи': {'genres': ['Рок'],
                     'albums': {'Там, де нас нема': {'year': 1998,
                                                     'songs': [['Там, де нас нема', 209, 'Из фильма "Брат/2"']]},
                                'Янанебібув': {'year': 2000,
                                               'songs': [['Коли тебе нема', 197, 'Из фильма "Брат/2"'],
                                                         ['Там, де нас нема', 209, 'Зарубежное'],
                                                         ['Янанебібув', 199, 'Зарубежное']]},
                                'Dolce Vita': {'year': 2009,
                                               'songs': [['На лінії вогню', 181],
                                                         ['Небо над Дніпром', 256]]}}}},
    {'Дима Билан': {'genres': ['Поп'],
                    'albums': {'Believe': {'year': 2009,
                                           'songs': [['Believe', 180, 'Mix']]}}}},
    {'Zivert': {'genres':['Поп'],
                'albums': {'Vinyl #1': {'year': 2019,
                                        'songs': [['Life', 188]]},
                           'Vinyl #2': {'year': 2021,
                                        'songs': [['DEL MAR', 220],
                                                  ['Forever Young', 180, 'Любимое']]}}}},
    {'The Weekend': {'genres': ['Поп', 'Рэп', 'R&B', 'Хип-хоп'],
                     'albums': {'After Hours': {'year': 2020,
                                                'songs': [['Heartless', 198, 'Mix']]}}}},
    {'Sting': {'genres': ['Поп','Рок'],
               'albums': {'Symphonicities': {'year': 2010,
                                             'songs': [['Englishman in New York', 263, 'Любимое']]},
                          '57th & 9th': {'year': 2016,
                                         'songs': [["I Can't Stop Thinking About You", 210, 'Зарубежное'],
                                                   ['Inshallah', 294, 'Mix']]}}}},
    {'Frank Sinatra': {'genres': ['Поп','Джаз'],
                       'albums': {}, 'songs': [[]]}},
    {'Black Eyed Peas': {'genres': ['Поп','Джаз', 'R&B', 'Хип-хоп'],
                         'albums': {'Elephunk': {'year': 2003,
                                                 'songs': [['Let’s Get It Started', 219, 'Любимое'],
                                                           ['Hey Mama', 215],
                                                           ['Where Is the Love?', 294]]},
                                    'Monkey Business': {'year': 2003,
                                                        'songs': [['Pump It', 213, 'Mix'],
                                                                  ['My Humps', 326, 'Mix']]},
                                    'The E.N.D.': {'year': 2009,
                                                   'songs': [['I Gotta Feeling', 290, 'Mix']]}}}},
    {'Skrillex': {'genres': ['Танцевальная', 'Электроника', 'Рэп' , 'Хип-хоп'],
                  'albums': {'Recess': {'year': 2014,
                                        'songs': [['Recess', 237,'Dance'],
                                                  ['Stranger', 289, 'Dance', 'Зарубежное'],
                                                  ['Doompy Poomp', 205, 'Dance']]}}}},
    {'Kanye West': {'genres': ['Рэп' , 'Хип-хоп'],
                    'albums': {'Jesus Is King': {'year': 2019,
                                                 'songs': [['God Is', 203],
                                                           ['Hands On', 203]]},
                               'Donda': {'year': 2021,
                                         'songs': [['Remote Control', 199, '2021'],
                                                   ['Heaven and Hell', 145, '2021'],
                                                   ['New Again', 183, '2021']]}}}}]

# Загружаем данные в таблицу genres
number_list = iter(range(1, len(genres) + 1))
for genre in genres:
    number = next(number_list)
    connection.execute(f"INSERT INTO genres VALUES({number},'{genre}')")

# Загружаем данные в таблицу collections
for i in range(1, len(Collections) + 1):
    connection.execute(f"INSERT INTO collections VALUES({i}, '{Collections[i - 1][0]}', '{Collections[i - 1][1]}')")

# Загружаем данные в таблицу singers, albums, tracks и связи между таблицами
album_number = 1
track_number = 1
for i in range(1, len(singers) + 1):
    singer_number = i
    connection.execute(f"INSERT INTO singers VALUES({singer_number},'{list(singers[i - 1].keys())[0]}')")
    for value in singers[i - 1].values():
        # Связываем жанты и с певцом
        for genre in value['genres']:
            # Вытягиеваем номер жанра из таблицы
            genre_id = connection.execute(f"SELECT id FROM genres WHERE name = '{genre}';").fetchall()[0][0]
            # Соединяем жанры с певцами
            connection.execute(f"INSERT INTO genresinger VALUES ({genre_id}, {i});")
        # Добавляем альбомы в albums
        for album in value['albums']:
            album_year = value['albums'][album]['year']
            connection.execute(f"INSERT INTO albums VALUES ({album_number}, '{album}', {album_year});")
            # Соединяем aльбом с певцом
            connection.execute(f"INSERT INTO singeralbum VALUES ({singer_number}, {album_number});")
            # Добавляем треки и соединяем с альбомом
            for song in value['albums'][album]['songs']:
                if "'" in song[0]:
                    song[0] = song[0].replace("'", "''")
                connection.execute(f"INSERT INTO tracks VALUES ({track_number}, '{song[0]}', {song[1]}, {album_number});")
                song_in_collections = song[2:]
                for s_coll in song_in_collections:
                    # Вытягиваем номер коллекции
                    collection_id = connection.execute(f"""
                        SELECT id FROM collections WHERE name = '{s_coll}';""").fetchall()[0][0]
                    # Соединяем треки и сборники
                    connection.execute(f"""
                        INSERT INTO collectiontrack VALUES ({collection_id}, {track_number});""")
                track_number += 1
            album_number += 1

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


# task 1 количество исполнителей в каждом жанре
collection_id = connection.execute(f"""SELECT g.name, COUNT(s.name)
FROM genres g JOIN genresinger gs ON g.id = gs.genre_id
JOIN singers s ON gs.singer_id = s.id
GROUP BY g.name
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 2 количество треков, вошедших в альбомы 2019-2020 годов
collection_id = connection.execute(f"""SELECT COUNT(t.name)
FROM tracks t JOIN albums a ON t.album_id = a.id
WHERE a.year BETWEEN 2019 and 2020
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 3 средняя продолжительность треков по каждому альбому
collection_id = connection.execute(f"""SELECT a.name, AVG(t.duration)
FROM tracks t JOIN albums a ON t.album_id = a.id
GROUP BY a.name
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 4 все исполнители, которые не выпустили альбомы в 2020 году
collection_id = connection.execute(f"""SELECT DISTINCT s.name 
FROM singers s JOIN singeralbum sa ON s.id = sa.singer_id
JOIN albums a ON sa.album_id = a.id 
WHERE a.name NOT IN (SELECT name FROM albums
                         WHERE year = 2020)
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 5 названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
collection_id = connection.execute(f"""SELECT DISTINCT c.name
FROM collections c JOIN collectiontrack ct ON c.id = ct.collection_id
JOIN tracks t ON ct.track_id = t.id
JOIN albums a ON t.album_id = a.id
JOIN singeralbum sa ON a.id = sa.album_id
JOIN singers s ON sa.singer_id = s.id
WHERE s.name = 'Linkin Park'
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 6 название альбомов, в которых присутствуют исполнители более 1 жанра
collection_id = connection.execute(f"""SELECT a.name
FROM albums a JOIN singeralbum sa ON a.id = sa.album_id
JOIN singers s ON sa.singer_id = s.id
JOIN genresinger gs ON s.id = gs.singer_id
JOIN genres g ON gs.genre_id = g.id
GROUP BY a.name
HAVING COUNT(g.name) > 1
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 7 наименование треков, которые не входят в сборники
collection_id = connection.execute(f"""SELECT t.name
FROM collections c JOIN collectiontrack ct ON c.id = ct.collection_id
Right JOIN tracks t ON ct.track_id = t.id
WHERE c.id is NULL
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 8 исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько)
collection_id = connection.execute(f"""SELECT s.name, t.name, t.duration
FROM tracks t JOIN albums a ON t.album_id = a.id
JOIN singeralbum sa ON a.id = sa.album_id
JOIN singers s ON sa.singer_id = s.id
WHERE t.duration = (SELECT MIN(duration) FROM tracks)
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

# task 9 название альбомов, содержащих наименьшее количество треков
collection_id = connection.execute(f"""SELECT a.name
FROM tracks t JOIN albums a ON t.album_id = a.id
GROUP BY a.name
HAVING COUNT(t.name) = (SELECT COUNT(t.name)
                          FROM tracks t JOIN albums a ON t.album_id = a.id
                          GROUP BY a.name
                          ORDER BY COUNT(t.name)
                          LIMIT 1)
;""").fetchall()
pprint(collection_id)
print('-----------', '-----------', sep='\n')

