use sakila;

select c.first_name, c.last_name, c.email, a.address
from customer c 
join address a on c.address_id = a.address_id and a.city_id = 312;

select f.title, f.description, f.release_year, f.rating, f.special_features, c.name as 'genre' 
from film f 
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id and c.name = 'Comedy';

select f.title, f.description, f.release_year 
from film f 
join film_actor fa on f.film_id = fa.film_id and fa.actor_id = 5;

select c.first_name, c.last_name, c.email, a.address 
from customer c
join address a on c.address_id = a.address_id and a.city_id in (1, 42, 312, 459)
where c.store_id = 1;

select f.title, f.description, f.release_year, f.rating, f.special_features 
from film f 
join film_actor fa on f.film_id = fa.film_id and fa.actor_id = 15
where f.rating = 'G' and f.special_features like '%Behind the Scenes%';

select f.film_id, f.title, a.actor_id, concat_ws(' ', a.first_name, a.last_name) as 'actor_name' 
from film f 
join film_actor fa on f.film_id = fa.film_id and f.film_id = 369
join actor a on fa.actor_id = a.actor_id;

select f.title, f.description, f.release_year, f.rating, f.special_features, c.name 'genre' 
from film f 
join film_category fc on f.film_id = fc.film_id and f.rental_rate = 2.99
join category c on fc.category_id = c.category_id and c.name = 'Drama';

select f.title, f.description, f.release_year, f.rating, f.special_features, c.name 'genre' , a.first_name, a.last_name
from film f 
join film_category fc on f.film_id = fc.film_id 
join film_actor fa on f.film_id = fa.film_id 
join actor a on fa.actor_id = a.actor_id and lower(a.first_name) = 'sandra' and lower(a.last_name) = 'kilmer'
join category c on fc.category_id = c.category_id and c.name = 'Action';
