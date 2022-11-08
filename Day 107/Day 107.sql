
SELECT original_title
FROM movies
WHERE director = "Noah Baumbach"



SELECT original_title
FROM movies
WHERE vote_average > 7 AND release_year > 2014

SELECT original_title, 
       cast
FROM movies
WHERE genres = 'Comedy'


SELECT original_title,
       ROUND(((vote_count / (vote_count + 104) * vote_average) + (104/ (104 + vote_count) * 5.97)),2) AS Weighted_avg_rating
FROM movies
ORDER BY  Weighted_avg_rating DESC
LIMIT 10


SELECT original_title, director, genres
FROM movies
WHERE runtime < 120


SELECT  original_title, director, genres, cast, budget, revenue, runtime, vote_average
FROM    movies
WHERE keywords = 'sport' OR keywords = 'sequel' OR keywords = 'suspense';


select original_title, director, genres, cast, budget, revenue, runtime, vote_average 
from movies 
where keywords in ('sport', 'sequel', 'suspense');


SELECT UPPER(CONCAT(original_title, '-', tagline)) AS Title
FROM movies
ORDER BY revenue DESC
LIMIT 10


SELECT original_title, tagline, director
FROM movies
ORDER BY popularity DESC
LIMIT 5


SELECT original_title, genres, vote_average, revenue
FROM movies
WHERE release_year BETWEEN 2012 AND 2015


SELECT original_title, popularity
FROM movies
WHERE genres = "Horror"
ORDER BY popularity DESC




