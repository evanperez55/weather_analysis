# Weather Analysis

## Steps Taken
1. The following SQL query was written to pull the information from both the city_data table and global_data table using a JOIN and giving each table an alias instead of writing multiple queries. There is also a WHERE clause to only pull the temperature data that is associated with the city of Milwaukee and an ORDER BY ASC statement to order the data by year in ascending order. (See SQL query file in this repository which includes query and database schema from which the data was pulled from)
3. Once the data was pulled into a CSV file I imported it into Google Sheets
4. In Google Sheets I calculated the 10-year moving average by finding the average of the first ten years in a separate column and dragging the formula down to replicate it for all of the years for both Milwaukee’s temperature as well as the global temperature from the years 1750-2000 and labeled the columns Milwaukee and Global.
5. To get a better idea of the difference between Milwaukee and global temperature I created a column subtracting global from Milwaukee (Milwaukee being higher in temperature) where I then found the Min and Max and applied the Average function to determine the average difference.
6. After I had the moving averages for both temperatures I selected the city, year, Milwaukee, and Global columns and inserted a line graph.
7. I then added a suiting title as well as labeled the horizontal and vertical axes appropriately.

*Please see next page for the Line Graph as well as the Observations








## Observations
1. Milwaukee’s moving average temperature on average was 1.8 degrees warmer than the global moving average temperature.
2. The changes in Milwaukee’s temperature tends to spike and drop much more than the global temperature, especially between 1850-2000 where the global temperature gradually rises.
3. When looking at both of the temperatures it would seem that the temperature is climbing overall when looking at Milwaukee or globally.
4. When looking for a correlation and possible relationship between the Milwaukee temperature as well as the global the two trends had a Correlation Coefficient of 0.90 which means there is a strong positive correlation between the two trends.





