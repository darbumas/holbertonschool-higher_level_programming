-- lists all shows in db -> 'hbtn_0d_tvshows without a genre
-- results diplay tv_shows.title - tv_show_genres.genre_id
SELECT
	tv_shows.title, tv_show_genres.genre_id
FROM
	tv_shows
LEFT JOIN
	tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE
	tv_show_genres.genre_id IS NULL
ORDER BY
	tv_shows.title, tv_show_genres.genre_id;
