--1. Лысые злодеи 90х годов
SELECT name,FIRST_APPEARANCE,APPEARANCES
FROM MarvelCharacters
WHERE ALIGN = 'Bad Characters' AND HAIR = 'Bald' AND YEAR BETWEEN 1990 AND 1999
ORDER BY name DESC, FIRST_APPEARANCE DESC,APPEARANCES DESC, year DESC
--2. Герои с тайной идентичностью и необычными глазами
SELECT name, FIRST_APPEARANCE, EYE
FROM MarvelCharacters
WHERE identify = 'Secret Identity' AND EYE NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes')
ORDER BY name DESC, FIRST_APPEARANCE DESC, EYE DESC
--3. Персонажи с изменяющимся цветом волос
SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair'
ORDER BY name DESC, HAIR DESC
--4. Женские персонажи с редким цветом глаз
SELECT name, EYE
FROM MarvelCharacters
WHERE SEX = 'Female Characters' AND EYE IN ('Gold Eyes', 'Amber Eyes')
ORDER BY name DESC, EYE DESC
--5. Персонажи без двойной идентичности, сортированные по году появления
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE identify = 'No Dual Identity'
ORDER BY FIRST_APPEARANCE DESC
--6. Герои и злодеи с необычными прическами
SELECT name, ALIGN,HAIR
FROM MarvelCharacters
WHERE HAIR NOT IN ('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair')
ORDER BY name ASC, ALIGN,HAIR
--7. Персонажи, появившиеся в определённое десятилетие
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE YEAR BETWEEN 1960 AND 1969
ORDER BY FIRST_APPEARANCE ASC,name
--8. Персонажи с уникальным сочетанием цвета глаз и волос
SELECT name, EYE,HAIR
FROM MarvelCharacters
WHERE EYE = 'Yellow Eyes' AND HAIR = 'Red Hair'
ORDER BY name ASC
--9. Персонажи с ограниченным количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < 10
ORDER BY name DESC, APPEARANCES DESC
--10. Персонажи с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5
--11. Персонажи, появившиеся только в одном десятилетии
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE YEAR BETWEEN 2000 AND 2009
ORDER BY FIRST_APPEARANCE ASC
--12. Персонажи с самыми редкими цветами глаз
SELECT name, EYE
FROM MarvelCharacters
WHERE EYE IN ('Magenta Eyes', 'Pink Eyes',  'Violet Eyes')
ORDER BY name DESC, EYE
--13. Герои с публичной идентичностью, сортированные по году
SELECT name,identify, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE identify = 'Public Identity'
ORDER BY FIRST_APPEARANCE ASC
--14. Персонажи с конкретным цветом волос и глаз, упорядоченные по имени
SELECT name, EYE,HAIR
FROM MarvelCharacters
WHERE EYE = 'Green Eyes' AND HAIR = 'Black Hair'
ORDER BY name ASC
--15. Злодеи с нестандартными физическими характеристиками
SELECT name, SEX
FROM MarvelCharacters
WHERE ALIGN = 'Bad Characters' AND SEX NOT IN('Female Characters','Male Characters')
ORDER BY name ASC
--16. Название: Персонажи с наибольшим числом появлений по полу
SELECT name, SEX, APPEARANCES
FROM MarvelCharacters
WHERE SEX IN ('Female Characters','Male Characters')
GROUP BY SEX
ORDER BY APPEARANCES DESC,SEX DESC
--17. Название: Сравнение популярности персонажей по цвету волос и глаз
SELECT name, EYE,HAIR,count(*) as count
FROM MarvelCharacters
GROUP BY EYE,HAIR
ORDER BY count DESC
--18. Название: Персонажи с максимальным количеством появлений в десятилетие
SELECT year,name,MAX(APPEARANCES) max_appearances
FROM MarvelCharacters
WHERE year > 1940
GROUP BY year
ORDER BY year ASC, max_appearances DESC
--19. Название: Герои и злодеи 80-х
SELECT ALIGN,count(*) as count
FROM MarvelCharacters
WHERE year BETWEEN 1980 AND 1989 AND ALIGN IN ('Good Characters', 'Bad Characters')
GROUP BY ALIGN
ORDER BY count DESC
--20. Название: Самые популярные прически супергероев
SELECT HAIR,count(*) as count,APPEARANCES
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY APPEARANCES DESC,HAIR DESC,count DESC
LIMIT 3

