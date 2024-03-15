-- script uses the hbtn_0d_tvshows database to lists all genres of show Dexter
-- Results must be sorted in ascending order by the genre name
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres m ON tv_genres.id = m.genre_id
INNER JOIN tv_shows s ON m.show_id = s.id
WHERE s.title = 'Dexter' ORDER BY tv_genres.name ASC;
