-- join

SELECT cities.id, cities.name, states.name FROM states JOIN cities ON states.id = cities.id ORDER BY cities.id;
