-- 1. What query would you run to get all the countries that speak Slovene? 
-- Your query should return the name of the country, language and language percentage. 
-- Your query should arrange the result by language percentage in descending order. (1)

select name, language, percentage
from countries
join languages
on countries.code = languages.country_code
where languages.language='Slovene'
group by languages.percentage desc;

-- 2. What query would you run to display the total number of cities for each country? 
-- Your query should return the name of the country and the total number of cities. 
-- You query should arrange the result by the number of cities in descending order. (3)

select countries.name, count(*) as 'cities' 
from countries 
join cities 
on countries.code = cities.country_code
group by countries.name 
order by count(*) desc;

-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? 
-- Your query should arrange the result by population in descending order. (1)

select name, population
from cities
where country_code = 'mex' and population > 500000
group by population desc;

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? 
-- Your query should arrange the result by percentage in descending order. (1)

select countries.name, languages.language, languages.percentage 
from countries 
join languages
on countries.code = languages.country_code
where languages.percentage > 89
order by languages.percentage desc;

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)

select name, surface_area, population
from countries
where surface_area < 501 and population > 100000;

-- 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)

select name, government_form, capital, life_expectancy
from countries
where government_form='Constitutional Monarchy' and life_expectancy>75 and capital>200;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500,000? 
-- The query should return the Country Name, City Name, District and Population. (2)

select c.name, ci.name, ci.district, ci.population
from cities ci
left join countries c
on c.code = ci.country_code
where ci.population > 500000 and ci.district='Buenos Aires';


-- 8. What query would you run to summarize the number of countries in each region? 
-- The query should display the name of the region and the number of countries. 
-- Also, the query should arrange the result by the number of countries in descending order. (2)

select region, count(*) as countries
from countries
group by region
order by count(*) desc