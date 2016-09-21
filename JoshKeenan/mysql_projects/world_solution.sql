-- select * from languages;
-- select * from cities;
-- select * from countries;
-- 
-- SELECT countries.name AS Country, languages.language AS Language, languages.percentage AS Percent
-- FROM countries
-- LEFT JOIN languages on countries.id = languages.country_id
-- WHERE languages.language = 'Slovene'
-- ORDER BY languages.percentage DESC

-- SELECT countries.name, COUNT(cities.id) AS cities_amt
-- FROM countries
-- JOIN cities ON countries.id = cities.country_id
-- GROUP BY countries.id
-- ORDER BY cities_amt DESC;

-- SELECT countries.name AS Country, cities.name AS City, cities.population as Population
-- FROM countries
-- LEFT JOIN cities ON countries.id = cities.country_id
-- WHERE countries.name = 'Mexico' AND cities.population > 500000
-- ORDER BY cities.population DESC;

-- SELECT countries.name, languages.percentage, languages.language
-- FROM countries
-- LEFT JOIN languages ON countries.id = languages.country_id
-- WHERE languages.percentage > 89.00
-- ORDER BY languages.percentage DESC;

-- SELECT countries.name, countries.surface_area, countries.population
-- FROM countries
-- WHERE countries.surface_area < 501 AND countries.population > 100000

-- SELECT countries.name, countries.government_form, countries.life_expectancy, countries.capital
-- FROM countries
-- WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75

-- SELECT countries.name AS Country, cities.name AS City, cities.district AS District, cities.population AS Population
-- FROM countries
-- LEFT JOIN cities ON countries.id = cities.country_id
-- WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000
-- ORDER BY cities.population DESC

SELECT countries.region, COUNT(countries.id) as country_num
FROM countries
GROUP BY countries.region
ORDER BY country_num DESC;