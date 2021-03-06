
# ETL-- Project

## A scientific research conducted in response to the Corona Virus (CO-VID19) and Ebola disease.

What we are looking to do is compare the amount of scientific research conducted in response to the Corona Virus (CO-VID19) and Ebola disease. Starting from day 1 of the outbreak, we want to compare how many cases of each virus there were, and how many articles of published research was released by that time. The purpose of doing this is to see if there was a change in the rate of how quickly each disease was spreading as related to the time of article published. We also want to compare how many confirmed cases there are and the amount of confirmed deaths.

## Extraction

The data source for both the Corona Virus and the Ebola Virus was extracted on Kaggle.They have updated CSV files where the resources were pulled from various sources such as WHO, CDC, NHC, DXY. Other source of data was from PubMed. 

![image](https://user-images.githubusercontent.com/57304123/90667639-d2f0d800-e203-11ea-9e05-ad07df8b9789.png)

![image](https://user-images.githubusercontent.com/57304123/90667918-18150a00-e204-11ea-8c51-62fbeca535df.png)

## Transformation

Data extracted were cleaned and merge to show the Date, total # of cases, and total # of deaths. Because we are looking at this from a global standpoint, we need to group everything by each date.
Also, the web scarpping that was done on PubMed website was only on articles related to the Ebola virus and Corona virus.

![image](https://user-images.githubusercontent.com/57304123/90668189-878af980-e204-11ea-9715-2779ad1eeb02.png)

## Loading

We loaded the data into SQL database and joined the data on date, to compare the total number of confirm cases and total death

![image](https://user-images.githubusercontent.com/57304123/90668668-46471980-e205-11ea-8aa9-1f8e71a0ea20.png)
