SELECT cd.city, cd.year, cd.avg_temp AS city_temp, gd.avg_temp AS global_temp 
FROM city_data AS cd
JOIN global_data AS gd
	ON cd.year = gd.year
WHERE cd.city LIKE 'Milwaukee'
ORDER BY cd.year ASC




Database Table Schema


City_data
year:city:country:avg_temp

City_list
city:country

Global_data
year:avg_temp


