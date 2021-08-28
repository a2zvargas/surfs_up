# Surfs Up!

## Overview of the analysis: 

The purpose of this analysis is to calculate temperature trends for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Results: 

June Temps | Dec Temps
:-------------------------:|:-------------------------:
![June_Temps](https://user-images.githubusercontent.com/85706721/131226354-d318e54e-50b0-42b0-973b-c163e3be4876.png)|![Dec_Temps](https://user-images.githubusercontent.com/85706721/131226357-e698f93b-de0b-4733-b8d6-bee6e33417f1.png)

* The data shows that although we are looking at summer vs winter months, the temperatures are very similar across the board.
* The largest difference is in the minimum temperatures where in June it hit a low of 64 and Dec a low of 56, an 8 degree difference.
* The average temperatures between the two months are only 3-4 degrees apart.

## Summary: 

With the temperatures being so close between June and December, it looks like a surf and ice cream shop business is sustainable year-round.


## Additional queries: 

I also wanted to do a comparison on what I consider to be the peak of summer and winter, by looking at the temperatures on the Summer and Winter Solstices.  The average temperatures once again are very close, but we have a greater max temp difference of 4 degrees.

Summer Solstice Temps | Winter Solstice Temps
:-------------------------:|:-------------------------:
![Summer_Solstice_Temps](https://user-images.githubusercontent.com/85706721/131227766-ba29560c-5f62-4b7b-a061-b64cbaeadbb1.png) | ![Winterer_Solstice_Temps](https://user-images.githubusercontent.com/85706721/131227771-0fe9cf88-ae48-4424-b498-9c1ff97b651c.png)

Summer Solstice Query
```
summer_sol_results = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==6).filter(extract('day', Measurement.date)==21).all()
summer_sol_df = pd.DataFrame(summer_sol_results, columns=['Date','Summer Solstice Temps'])
summer_sol_df.describe()
```

Winter Solstice Query
```
winter_sol_results = session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date)==12).filter(extract('day', Measurement.date)==21).all()
winter_sol_df = pd.DataFrame(winter_sol_results, columns=['Date','Winter Solstice Temps'])
winter_sol_df.describe()
```
