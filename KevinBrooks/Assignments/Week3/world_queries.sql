use world;

select c.name, l.language, l.percentage as 'language percentage' from countries c 
join languages l on c.code = l.country_code 
where l.language = 'Slovene'
order by l.percentage desc;

select c.name, count(1) as 'total cities' from countries c 
join cities ci on c.code = ci.country_code
group by c.name 
order by count(1) desc;

select c.name as 'city', c.population from cities c 
where c.country_code = 'MEX' AND c.population > 500000 ;

select c.name, l.language, l.percentage from countries c 
join languages l on c.code = l.country_code
where l.percentage > 89
order by l.percentage desc;

select c.name, c.surface_area, c.population from countries c 
where c.surface_area < 501 and c.population > 100000
order by c.population desc, c.surface_area asc;

select c.name, c.government_form, c.capital, c.life_expectancy from countries c
where c.government_form = 'Constitutional Monarchy' and c.capital > 200 and c.life_expectancy > 75
order by c.capital desc, c.life_expectancy desc;

select c.name as 'country', ci.name as 'city', ci.district, ci.population from countries c 
join cities ci on c.code = ci.country_code
where ci.district = 'Buenos Aires' and ci.population > 500000
order by ci.population desc;

select c.region, count(1) as 'total countries' 
from countries c
group by c.region
order by count(1) desc;