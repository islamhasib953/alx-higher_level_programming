-- script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres g ON s.id=g.show_id
LEFT JOIN tv_genres v ON g.genre_id=v.id
WHERE v.name = "Comedy"
ORDER BY s.title;
