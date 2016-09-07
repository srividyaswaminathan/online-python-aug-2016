-- 1.What query would you run to get all the customers inside city_id = 312? 
-- Your query should return customer first name, last name, email, and address.
SELECT first_name, last_name, email, CONCAT_WS(', ', address, district, city, postal_code) AS address
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city_id =312;

-- 2.What query would you run to get all comedy films? 
-- Your query should return film title, description, release year, rating, special features, and genre.
SELECT title, description, release_year, rating, special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'comedy';

-- 3.What query would you run to get all the films joined by actor_id=5? 
-- Your query should return the film title, description, and release year.
SELECT first_name AS actor, title, description, release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

-- 4.What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.
SELECT 
    store_id,
    city.city_id,
    first_name,
    last_name,
    email,
    CONCAT_WS(', ',
            address,
            district,
            city,
            postal_code) AS address
FROM
    customer
        JOIN
    address ON customer.address_id = address.address_id
        JOIN
    city ON address.city_id = city.city_id
WHERE
    (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459) AND store_id = 1;

-- 5.What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rate, and special feature. 
SELECT first_name, title, description, release_year, rating, special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE rating = 'G' AND special_features LIKE '%behind the scenes%' AND actor.actor_id = 15;

-- 6.What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.
SELECT film.film_id, title, actor.actor_id, UPPER(CONCAT_WS(' ',first_name, last_name)) AS actor_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

-- 7.What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, and genre.
SELECT title, description, release_year, rating, special_features, category.name AS genre, rental_rate
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE category.name = 'drama' AND rental_rate = 2.99;

-- 8.What query would you run to get all the action films which are joined by SANDRA KILMER? 
-- Your query should return film title, description, release year, rating, special features, genre, and actor's first name and last name.
SELECT UPPER(CONCAT_WS(' ', first_name, last_name)), title, description, release_year, rating, special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'action' AND first_name = 'sandra' AND last_name = 'kilmer';
