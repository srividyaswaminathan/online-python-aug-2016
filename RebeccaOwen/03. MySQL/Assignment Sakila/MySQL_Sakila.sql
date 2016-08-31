-- What query would you run to get all the customers inside city_id = 312? 
-- Your query should return customer first name, last name, email, and address.

select c.first_name, c.last_name, c.email, a.address, ci.city, a.postal_code
from address a
join customer c
on c.address_id = a.address_id
join city ci
on ci.city_id = a.city_id
where a.city_id = 312;

-- What query would you run to get all comedy films? 
-- Your query should return film title, description, release year, rating, special features, and genre.

select f.title, f.description, f.release_year, f.rating, f.special_features, category.name as genre
from film f
join film_category
on film_category.film_id = f.film_id
join category
on category.category_id = film_category.category_id
where category.name = 'Comedy';

-- What query would you run to get all the films joined by actor_id=5? 
-- Your query should return the film title, description, and release year.

select a.actor_id, concat(a.first_name, ' ', a.last_name) as actor, f.title, f.description, f.release_year
from film f
join film_actor fa
on fa.film_id = f.film_id
join actor a
on a.actor_id = fa.actor_id
where a.actor_id = 5;

-- What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.

select c.store_id, a.city_id, c.first_name, c.last_name, c.email, a.address
from customer c
join address a
on a.address_id = c.address_id
where c.store_id = 1 and a.city_id in (1, 42, 312, 459);

-- What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rate, and special feature. 
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.

select f.title, f.description, f.release_year, f.rating, f.special_features
from film f 
join film_actor fa
on fa.film_id = f.film_id
where f.rating = 'G' and f.special_features like '%behind the scenes%' and fa.actor_id = 15;

-- What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.

select film.film_id, film.title, actor.actor_id, concat(actor.first_name, ' ', actor.last_name)
from film
join film_actor
on film_actor.film_id = film.film_id
join actor
on actor.actor_id = film_actor.actor_id
where film.film_id = 369;

-- What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, and genre.

select film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, film.rental_rate, category.name as genre
from film
join film_category
on film.film_id = film_category.film_id
join category
on category.category_id = film_category.category_id
where category.name = 'Drama' and film.rental_rate = 2.99;

-- What query would you run to get all the action films which are joined by SANDRA KILMER? 
-- Your query should return film title, description, release year, rating, special features, genre, and actor's first name and last name.

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, concat(actor.first_name, ' ', actor.last_name) as actor
from film
join film_category
on film.film_id = film_category.film_id
join category
on category.category_id = film_category.category_id
join film_actor
on film_actor.film_id = film.film_id
join actor
on actor.actor_id = film_actor.actor_id
where category.name = 'Action' and actor.first_name = 'Sandra' and actor.last_name = 'Kilmer';
