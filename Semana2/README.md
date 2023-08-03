# Tarea 2

## Lesson 1
### Enum 1: Find the title of each film
### Sol 1: SELECT title FROM movies;
### Enum 2: Find the director of each film
### Sol 2: SELECT director FROM movies;
### Enum 3: Find the title and director of each film
### Sol 3: SELECT title, director FROM movies;
### Enum 4: Find the title and year of each film
### Sol 4: SELECT title, year FROM movies;
### Enum 5: Find all the information about each film
### Sol 5: SELECT * FROM movies;

## Lesson 2
### Enum 1: Find the movie with a row id of 6
### Sol 1: SELECT * FROM movies where Id = 6;
### Enum 2: Find the movies released in the years between 2000 and 2010
### Sol 2: SELECT * FROM Movies WHERE Year BETWEEN '2000' AND '2010';
### Enum 3: Find the movies not released in the years between 2000 and 2010
### Sol 3: SELECT * FROM Movies WHERE Year NOT BETWEEN '2000' AND '2010';
### Enum 4: Find the first 5 Pixar movies and their release year
### Sol 4: SELECT * FROM Movies LIMIT 5;

## Lesson 3
### Enum 1: Find all the Toy Story movies
### Sol 1 : SELECT * FROM Movies where Title LIKE 'Toy Story%';
### Enum 2: Find all the movies directed by John Lasseter
### Sol 2: SELECT * FROM Movies where Director LIKE 'John Lasseter';
### Enum 3: Find all the movies (and director) not directed by John Lasseter
### Sol 3: SELECT Title,Director FROM Movies where Director not LIKE 'John Lasseter';
### Enum 4: Find all the WALL-* movies
### Sol 4: SELECT * FROM Movies where Title LIKE 'WALL-%';

## Lesson 4
### Enum 1: List all directors of Pixar movies (alphabetically), without duplicates
### Sol 1: SELECT Director FROM movies group by Director ORDER BY Director;
### Enum 2: List the last four Pixar movies released (ordered from most recent to least)
### Sol 2: SELECT * FROM movies Order By Year DESC LIMIT 4;
### Enum 3: List the first five Pixar movies sorted alphabetically
### Sol 3: SELECT * FROM movies Order By Title ASC LIMIT 5;
### Enum 4: List the next five Pixar movies sorted alphabetically
### Sol 4: 

## Lesson 5
### Enum 1: List all the Canadian cities and their populations
### Sol 1: SELECT * FROM north_american_cities where Country = 'Canada';
### Enum 2: Order all the cities in the United States by their latitude from north to south
### Sol 2: SELECT * FROM north_american_cities where Country = 'United States' ORDER BY latitude DESC;
### Enum 3: List all the cities west of Chicago, ordered from west to east
### Sol 3: SELECT * FROM north_american_cities WHERE longitude < ( SELECT longitude FROM north_american_cities WHERE city = 'Chicago') ORDER BY longitude ASC;
### Enum 4: List the two largest cities in Mexico (by population)
### Sol 4: SELECT * FROM north_american_cities WHERE country = 'Mexico' ORDER BY population DESC LIMIT 2;
### Enum 5: List the third and fourth largest cities (by population) in the United States and their population
### Sol 5: 

## Lesson 10
### Enun 1: Find the longest time that an employee has been at the studio ✓
### Sol 1: SELECT MAX(Years_employed) FROM Employees;
### Enum 2: For each role, find the average number of years employed by employees in that role ✓
### Sol 2: SELECT Role,AVG(Years_employed) FROM Employees GROUP BY Role;
### Enum 3: Find the total number of employee years worked in each building ✓
### Sol 3: SELECT building, SUM(Years_Employed) FROM Employees GROUP BY building;

## Lesson 11
### Enum 1: Find the number of Artists in the studio (without a HAVING clause)
### Sol 1: SELECT role, COUNT(*) as Number_of_artists FROM employees WHERE role = "Artist";
### Enum 2: Find the number of Employees of each role in the studio
### Sol 2: SELECT role, COUNT(*) as Number_of_artists FROM employees GROUP BY role;
### Enum 3: Find the total number of years employed by all Engineers
### Sol 3: SELECT role, SUM(years_employed) FROM employees GROUP BY role HAVING role = "Engineer";

## Lesson 12
### Enum 1: Find the number of movies each director has directed ✓
### Sol 1: SELECT director, COUNT(id) as Num_movies_directed FROM movies GROUP BY director;
### Enum 2: Find the total domestic and international sales that can be attributed to each director ✓
### Sol 2: SELECT director, SUM(domestic_sales + international_sales) FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id GROUP BY director;

## Lesson 13
### Enum 1: Add the studio's new production, Toy Story 4 to the list of movies (you can use any director) ✓
### Sol 1: INSERT INTO Movies (Id, Title, Director, Year, Length_minutes) VALUES (15, "Toy Story 4", "Lee Unkrich", 2014, 115);
### Enum 2: Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table. ✓
### Sol 2: INSERT INTO Boxoffice (Movie_id, Rating, Domestic_sales, International_sales) VALUES (15, 8.7,340000000,270000000);

## Lesson 14
### Enum 1: The director for A Bug's Life is incorrect, it was actually directed by John Lasseter ✓
### Sol 1: UPDATE Movies SET Director = "John Lasseter" WHERE Title = "A Bug's Life";
### Enum 2: The year that Toy Story 2 was released is incorrect, it was actually released in 1999 ✓
### Sol 2: UPDATE Movies SET Year = 1999 WHERE Title = "Toy Story 2";
### Enum 3: Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich ✓
### Sol 3: UPDATE movies SET title = "Toy Story 3", director = "Lee Unkrich" WHERE id = 11;

## Lesson 15
### Enum 1: This database is getting too big, lets remove all movies that were released before 2005.
### Sol 1: DELETE FROM Movies WHERE Year < 2005;
### Enum 2: Andrew Stanton has also left the studio, so please remove all movies directed by him.
### Sol 2: DELETE FROM Movies WHERE Director = "Andrew Stanton";

## Lesson 16
### Enum 1:
### Sol 1: CREATE TABLE Database { Name TEXT, Version FLOAT, Download_count INTEGER };
