--Fill out the genre table
INSERT INTO genres VALUES(1, 'Рок');
INSERT INTO genres VALUES(2, 'Поп');
INSERT INTO genres VALUES(3, 'Рэп');
INSERT INTO genres VALUES(4, 'Фолк');
INSERT INTO genres VALUES(5, 'Кантри');
INSERT INTO genres VALUES(6, 'R&B');
INSERT INTO genres VALUES(7, 'Танцевальная');
INSERT INTO genres VALUES(8, 'Джаз');
INSERT INTO genres VALUES(9, 'Электроника');
INSERT INTO genres VALUES(10, 'Хип-хоп');
INSERT INTO genres VALUES(11, 'Хард-Рок');

--Fill out the singer table
INSERT INTO singers VALUES(1, 'Linkin Park');
INSERT INTO singers VALUES(2, 'Океан Ельзи');
INSERT INTO singers VALUES(3, 'Дима Билан');
INSERT INTO singers VALUES(4, 'Zivert');
INSERT INTO singers VALUES(5, 'The Weekend');
INSERT INTO singers VALUES(6, 'Sting');
INSERT INTO singers VALUES(7, 'Frank Sinatra');
INSERT INTO singers VALUES(8, 'Black Eyed Peas');
INSERT INTO singers VALUES(9, 'Skrillex');
INSERT INTO singers VALUES(10, 'Kanye West');

--Fill out the genresinger table
INSERT INTO genresinger VALUES(1, 1);
INSERT INTO genresinger VALUES(1, 2);
INSERT INTO genresinger VALUES(1, 6);
INSERT INTO genresinger VALUES(2, 3);
INSERT INTO genresinger VALUES(2, 4);
INSERT INTO genresinger VALUES(2, 5);
INSERT INTO genresinger VALUES(2, 6);
INSERT INTO genresinger VALUES(2, 7);
INSERT INTO genresinger VALUES(2, 8);
INSERT INTO genresinger VALUES(3, 5);
INSERT INTO genresinger VALUES(3, 9);
INSERT INTO genresinger VALUES(3, 10);
INSERT INTO genresinger VALUES(6, 5);
INSERT INTO genresinger VALUES(6, 8);
INSERT INTO genresinger VALUES(7, 9);
INSERT INTO genresinger VALUES(8, 7);
INSERT INTO genresinger VALUES(8, 8);
INSERT INTO genresinger VALUES(9, 9);
INSERT INTO genresinger VALUES(10, 5);
INSERT INTO genresinger VALUES(10, 8);
INSERT INTO genresinger VALUES(10, 9);
INSERT INTO genresinger VALUES(10, 10);

--Fill out the albums table
INSERT INTO albums VALUES(1, 'Hybrid Theory', 2000);
INSERT INTO albums VALUES(2, 'Meteora', 2003);
INSERT INTO albums VALUES(3, 'Там, де нас нема', 1998);
INSERT INTO albums VALUES(4, 'Янанебібув', 2000);
INSERT INTO albums VALUES(5, 'Dolce Vita', 2010);
INSERT INTO albums VALUES(6, 'Believe', 2009);
INSERT INTO albums VALUES(7, 'Vinyl #1', 2019);
INSERT INTO albums VALUES(8, 'Vinyl #2', 2021);
INSERT INTO albums VALUES(9, 'After Hours', 2020);
INSERT INTO albums VALUES(10, 'Symphonicities', 2010);
INSERT INTO albums VALUES(11, '57th & 9th', 2016);
INSERT INTO albums VALUES(12, 'Elephunk', 2003);
INSERT INTO albums VALUES(13, 'Monkey Business', 2003);
INSERT INTO albums VALUES(14, 'The E.N.D.', 2009);
INSERT INTO albums VALUES(15, 'Recess', 2014);
INSERT INTO albums VALUES(16, 'Jesus Is King', 2019);
INSERT INTO albums VALUES(17, 'Donda', 2021);

--Fill out the singeralbum table
INSERT INTO singeralbum VALUES(1, 1);
INSERT INTO singeralbum VALUES(1, 2);
INSERT INTO singeralbum VALUES(2, 3);
INSERT INTO singeralbum VALUES(2, 4);
INSERT INTO singeralbum VALUES(2, 5);
INSERT INTO singeralbum VALUES(3, 6);
INSERT INTO singeralbum VALUES(4, 7);
INSERT INTO singeralbum VALUES(4, 8);
INSERT INTO singeralbum VALUES(5, 9);
INSERT INTO singeralbum VALUES(6, 10);
INSERT INTO singeralbum VALUES(6, 11);
INSERT INTO singeralbum VALUES(8, 12);
INSERT INTO singeralbum VALUES(8, 13);
INSERT INTO singeralbum VALUES(8, 14);
INSERT INTO singeralbum VALUES(9, 15);
INSERT INTO singeralbum VALUES(10, 16);
INSERT INTO singeralbum VALUES(10, 17);

--Fill out the tracks table
INSERT INTO tracks VALUES(1, 'In the End', 216, 1);
INSERT INTO tracks VALUES(2, 'One Step Closer', 156, 1);
INSERT INTO tracks VALUES(3, 'A Place for My Head', 185, 1);
INSERT INTO tracks VALUES(4, 'Numb', 188, 2);
INSERT INTO tracks VALUES(5, 'Breaking the Habit', 196, 2);
INSERT INTO tracks VALUES(6, 'Там, де нас нема', 209, 3);
INSERT INTO tracks VALUES(7, 'Коли тебе нема', 197, 4);
INSERT INTO tracks VALUES(8, 'Там, де нас нема', 209, 4);
INSERT INTO tracks VALUES(9, 'Янанебібув', 199, 4);
INSERT INTO tracks VALUES(10, 'Небо над Дніпром', 256, 5);
INSERT INTO tracks VALUES(11, 'На лінії вогню', 181, 5);
INSERT INTO tracks VALUES(12, 'Believe', 180, 6);
INSERT INTO tracks VALUES(13, 'Life', 188, 7);
INSERT INTO tracks VALUES(14, 'DEL MAR', 220, 8);
INSERT INTO tracks VALUES(15, 'Forever Young', 180, 8);
INSERT INTO tracks VALUES(16, 'Heartless', 198, 9);
INSERT INTO tracks VALUES(17, 'Englishman in New York', 263, 10);
INSERT INTO tracks VALUES(18, 'I Can''t Stop Thinking About You', 210, 11);
INSERT INTO tracks VALUES(19, 'Inshallah', 294, 11);
INSERT INTO tracks VALUES(20, 'Let’s Get It Started', 219, 12);
INSERT INTO tracks VALUES(21, 'Hey Mama', 215, 12);
INSERT INTO tracks VALUES(22, 'Where Is the Love?', 294, 12);
INSERT INTO tracks VALUES(23, 'Pump It', 213, 13);
INSERT INTO tracks VALUES(24, 'My Humps', 326, 13);
INSERT INTO tracks VALUES(25, 'I Gotta Feeling', 290, 14);
INSERT INTO tracks VALUES(26, 'Recess', 237, 15);
INSERT INTO tracks VALUES(27, 'Stranger', 289, 15);
INSERT INTO tracks VALUES(28, 'Doompy Poomp', 205, 15);
INSERT INTO tracks VALUES(29, 'God Is', 203, 16);
INSERT INTO tracks VALUES(30, 'Hands On', 203, 16);
INSERT INTO tracks VALUES(31, 'Remote Control', 199, 17);
INSERT INTO tracks VALUES(32, 'Heaven and Hell', 145, 17);
INSERT INTO tracks VALUES(33, 'New Again', 183, 17);

--Fill out the collections table
INSERT INTO collections VALUES(1, 'Из фильма "Брат/2"', 2005);
INSERT INTO collections VALUES(2, 'Для души', 2020);
INSERT INTO collections VALUES(3, 'Любимое', 2016);
INSERT INTO collections VALUES(4, 'Dance', 2019);
INSERT INTO collections VALUES(5, 'Linkin Park', 2018);
INSERT INTO collections VALUES(6, 'Зарубежное', 2020);
INSERT INTO collections VALUES(7, '2021', 2021);
INSERT INTO collections VALUES(8, 'Mix', 2019);

--Fill out the collectiontrack table
INSERT INTO collectiontrack VALUES(1, 6);
INSERT INTO collectiontrack VALUES(1, 7);
INSERT INTO collectiontrack VALUES(3, 4);
INSERT INTO collectiontrack VALUES(3, 5);
INSERT INTO collectiontrack VALUES(3, 15);
INSERT INTO collectiontrack VALUES(3, 17);
INSERT INTO collectiontrack VALUES(3, 20);
INSERT INTO collectiontrack VALUES(4, 26);
INSERT INTO collectiontrack VALUES(4, 27);
INSERT INTO collectiontrack VALUES(4, 28);
INSERT INTO collectiontrack VALUES(5, 1);
INSERT INTO collectiontrack VALUES(5, 2);
INSERT INTO collectiontrack VALUES(5, 3);
INSERT INTO collectiontrack VALUES(5, 4);
INSERT INTO collectiontrack VALUES(5, 5);
INSERT INTO collectiontrack VALUES(6, 1);
INSERT INTO collectiontrack VALUES(6, 2);
INSERT INTO collectiontrack VALUES(6, 3);
INSERT INTO collectiontrack VALUES(6, 8);
INSERT INTO collectiontrack VALUES(6, 9);
INSERT INTO collectiontrack VALUES(6, 18);
INSERT INTO collectiontrack VALUES(6, 27);
INSERT INTO collectiontrack VALUES(7, 31);
INSERT INTO collectiontrack VALUES(7, 32);
INSERT INTO collectiontrack VALUES(7, 33);
INSERT INTO collectiontrack VALUES(8, 2);
INSERT INTO collectiontrack VALUES(8, 12);
INSERT INTO collectiontrack VALUES(8, 16);
INSERT INTO collectiontrack VALUES(8, 19);
INSERT INTO collectiontrack VALUES(8, 23);
INSERT INTO collectiontrack VALUES(8, 24);
INSERT INTO collectiontrack VALUES(8, 25);

