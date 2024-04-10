/*Seleccionar todos los datos de la tabla Peliculas:*/
SELECT * FROM Peliculas;
/*Seleccionar solo el título y el año de todas las películas:*/
SELECT titulo, año FROM Peliculas;
/*Seleccionar películas del año 2000 o posteriores:*/
SELECT * FROM Peliculas WHERE año >= 2000;
/*Seleccionar películas del género "Drama":*/
SELECT * FROM Peliculas WHERE genero = 'Drama';
/*Seleccionar películas dirigidas por "Quentin Tarantino":*/
SELECT * FROM Peliculas WHERE autor = 'Quentin Tarantino';
/*Seleccionar películas del género "Crimen" dirigidas por "Martin Scorsese":*/
SELECT * FROM Peliculas WHERE autor = 'Martin Scorsese' AND genero = 'Crimen';
/*Seleccionar películas ordenadas por año de forma descendente:*/
SELECT * FROM Peliculas ORDER BY año DESC;
/*Contar la cantidad total de películas en la tabla:*/
SELECT COUNT(*) FROM Peliculas;
/*Encontrar la película más antigua:*/
SELECT * FROM Peliculas ORDER BY año ASC LIMIT 1;
/*Encontrar la película más reciente:*/
SELECT * FROM Peliculas ORDER BY año DESC LIMIT 1;