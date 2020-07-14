-- join

SELECT cities.id, cities.name, states.name FROM states JOIN cities ON cities.id = states.id ORDER BY cities.id;
