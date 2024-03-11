-- breaking up the data is known as normalization. Nomalization reduce the risk of anomalies
-- anomalies are when you have data mismatch
-- update anomaly
-- delete anomaly
-- insert anomaly

-- there are 5 normal forms

-- first normal form
    -- 1. using row order to convey information is not permitted (so add an additional column). The row order should not matter. for example if the second row tells you the person is shorter than the first row. rather have it in seperate columns
    -- 2. mixing datatypes within the same column is not permitted
    -- 3. Having a table without a primary key is not permitted. The column you're choosing should be unique. E.g bank account number. They should not be null. Only one column can be a primary key.  
    -- 4. repeating groups are not permitted

    -- REMEMBER THAT YOU CANT HAVE A VALUE WITH RANGE 

-- second normal form
    -- each non-key attribute must depend on the entire primary key. If the primary key is a composite key then break it into a table with just half the composite key
    

-- third normal form
    -- every non-key attribute in a table should depend on the key, the whole key, and nothing but the key
    -- if there is an indirect dependency then create table of the non-key attribute and the attribute it does directly depend on.

-- INNER JOIN only gives common
-- LEFT JOIN gives common and items on the left (items meaning rows)
-- RIGHT JOIN gives common and items on the right
-- FULL JOIN gives everything including common itmes

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
-- % is zero or more
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
-- which ever is left of the left join in the statement, you will get extra items from there, for example, buidling in this case


-- exercise 8
SELECT name, role FROM employees WHERE BUILDING IS NULL
SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees ON building_name = building WHERE role is null


-- exercise 9
SELECT *, (domestic_sales + international_sales) / 1000000 AS sales_in_millions FROM movies JOIN boxoffice ON movies.id = boxoffice.movie_id;
select DISTINCT title, rating*10 as rating_percent from movies join boxoffice on id=movie_id
SELECT title, year FROM movies WHERE year % 2 = 0
-- ABS make it always positive

-- exercise 10
-- whenever you see the work 'each' then you'll use group by.
SELECT MAX(years_employed) as max_years FROM employees;
select role, avg(years_employed) as avg_employed from employees group by role
select building, sum(years_employed) as total_employed from employees group by building

-- exercise 11
SELECT count(role) as number_of_artists FROM employees where role="Artist"
SELECT role, count(role) as number_of_each_role FROM employees group by role
select role, sum(years_employed) as total_years_of_engineers from employees where role="Engineer"


-- exercise 12
SELECT count(title) as number_of_movies ,director FROM movies group by director;
select director, sum(domestic_sales + international_sales) as total_sales from movies join boxoffice on id=movie_id Group by director


-- exercise 13
INSERT into movies (title,director,year,length_minutes) Values ('Toy Story 4', 'Lee Unkrich', 2024 ,120);
INSERT INTO boxoffice(rating,domestic_sales,international_sales) VALUES (8.7,340000000,270000000)
-- you can also say insert into movies Values(4,'toy story 4', 'alex',2024,120)

-- exercise 14
UPDATE movies SET director= "John Lasseter" WHERE id=2
update movies set year=1999 where id=3
update movies set director="Lee Unkrich", title='Toy Story 3' where id=11

-- exercise 15
SELECT * FROM movies where year<2005;
DELETE from movies
where year<2005

SELECT * FROM movies where director="Andrew Stanton";
delete from movies
where director="Andrew Stanton"

-- exercise 16
-- difference between float, double, and real. float will give 3 decimal points, double will give 6, and real will give 12
-- character will be 4 so either male or female, varchar is for sentences(120 words) text is for paragraphs
-- we usually dont install blobs in database. Usually you install the link to the image

-- constraints
-- PRIMARY KEY (cant be null and can only be one column)
-- AUTOINCREMENT 
-- UNIQUE (can be null and can have multiple columns)
-- NOT NULL
-- CHECK(expression)
-- FOREIGN KEY

-- this is also known as a schema/  blueprint of the table:
CREATE TABLE IF NOT EXISTS database(
name TEXT,
Version FLOAT,
Download_count INTEGER
)

-- exercise 17
ALTER TABLE movies add Aspect_ratio FLOAT
alter table movies add language text default 'English'
--generally we dont remove a column
-- ALTER TABLE mytable
-- RENAME TO new_table_name;
-- ALTER TABLE mytable
-- DROP column_to_be_deleted;

-- exercise 18
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS boxoffice;

-- DDL: CREATE, ALTER, DROP. To modify the table itself
-- DML: SELECT, UPDATE, DELETE, INSERT. To modify data itself not the table

-- When creating a table its called a schema