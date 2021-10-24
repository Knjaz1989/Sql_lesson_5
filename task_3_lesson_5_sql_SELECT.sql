SELECT name, year FROM albums
	WHERE year = 2018;

SELECT name, duration FROM tracks
	ORDER BY duration DESC
	LIMIT 1;

SELECT name FROM tracks
	WHERE duration >= 210;

SELECT name FROM collections
	WHERE year BETWEEN 2018 and 2020;

SELECT name FROM singers
	WHERE array_length(regexp_split_to_array(name, '\s+'), 1) = 1;

SELECT name FROM tracks
	WHERE name LIKE '%%my%%';

