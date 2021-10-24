from sqlalchemy import create_engine

                      # dialect+driver://username:password@host:port/database
engine = create_engine('postgresql://postgres:1989@localhost:5432/lesson_3_sql')

connection = engine.connect()

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
