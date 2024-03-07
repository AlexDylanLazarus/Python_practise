-- breaking up the data is known as normalization. Nomalization reduce the risk of anomalies
-- anomalies are when you have data mismatch
-- update anomaly
-- delete anomaly
-- insert anomaly

-- there are 5 normal forms

-- first normal form
    -- 1. using row order to convery information is not permitted (so add an additional column)
    -- 2. mixing datatypes within the same column is not permitted
    -- 3. Having a table without a primary key is not permitted. The column you're choosing should be unique. E.g bank account number. They should not be null. Only one column can be a primary key.  
    -- 4. repeating groups are not permitted

    -- REMEMBER THAT YOU CANT HAVE A VALUE WITH RANGE 

-- second normal form
    -- each non-key attribute must depend on the entire primary key. If the primary key is a composite key then break it into a table with just half the composite key

-- third normal form
    -- every non-key attribute in a table should depend on the key, the whole key, and nothing but the key
    -- if there is an indirect dependency then create table of the non-key attribute and the attribute it does directly depend on.



-- exercise 1 
SELECT title FROM movies;
SELECT director FROM movies; 
SELECT title, director FROM movies; 
SELECT title, year FROM movies; 
SELECT * FROM movies; 

-- exercise 2
-- BETWEEN is inclusive unlike python
SELECT id, title FROM movies WHERE id = 6;
SELECT title, year FROM movies WHERE year BETWEEN 2000 AND 2010;
SELECT title, year FROM movies WHERE year < 2000 OR year > 2010;
SELECT title, year FROM movies WHERE year <= 2003;


-- exercise 3
--  _ is exactly one 
-- % is one or more
SELECT * FROM movies WHERE title LIKE "Toy%" ;
SELECT * FROM movies WHERE director LIKE "%Las%" ;
SELECT * FROM movies WHERE title NOT LIKE "%Lass%" 
SELECT * FROM movies WHERE title LIKE "%WAll%"

-- exercise 4
SELECT DISTINCT(director) FROM movies ORDER BY director ASC;
SELECT * FROM movies ORDER BY year DESC LIMIT 4;
SELECT * FROM movies ORDER BY title ASC LIMIT 5;
SELECT title FROM movies ORDER BY title ASC LIMIT 5 OFFSET 5;

--  exercise 5
SELECT * FROM north_american_cities WHERE country="Canada" ;
SELECT * FROM north_american_cities WHERE country="United States" ORDER BY latitude DESC  ;
SELECT * FROM north_american_cities where longitude < (SELECT longitude from north_american_cities where city="Chicago") ORDER BY longitude ASC;
SELECT * FROM north_american_cities WHERE Country = "Mexico" ORDER BY population DESC LIMIT 2;
SELECT * FROM north_american_cities WHERE Country = "United States" ORDER BY population DESC LIMIT 2 OFFSET 2;

-- exercise 6
SELECT title, domestic_sales, international_sales FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id;
SELECT title, domestic_sales, international_sales FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id WHERE international_sales > domestic_sales
SELECT title, rating FROM movies INNER JOIN boxoffice ON movies.id = boxoffice.movie_id ORDER BY rating DESC;

-- exercise 7
SELECT DISTINCT building FROM employees;
SELECT * FROM buildings;
SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees ON building_name = building;
--when you want to include empty then have left/right

-- exercise 8
SELECT name, role FROM employees WHERE BUILDING IS NULL
SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees ON building_name = building WHERE role is null