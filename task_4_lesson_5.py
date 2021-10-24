from pprint import pprint
from sqlalchemy import create_engine

                      # dialect+driver://username:password@host:port/database
engine = create_engine('postgresql://postgres:admin@localhost:5432/lesson_3_sql')

connection = engine.connect()

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

