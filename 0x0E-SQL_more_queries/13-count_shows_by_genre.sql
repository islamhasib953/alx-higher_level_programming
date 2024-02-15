-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT t.name AS `genre`, COUNT(g.genre_id) AS `number_of_shows`
FROM tv_genres t
JOIN tv_show_genres g
ON t.id = g.genre_id
GROUP BY genre
ORDER By number_of_shows DESC;
