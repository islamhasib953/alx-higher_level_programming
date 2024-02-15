-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT s.title title, g.genre_id genre_id
    FROM tv_shows s
    join tv_show_genres g
    ON s.id=g.show_id
ORDER BY s.title and g.genre_id;
