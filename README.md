# PANAMSTERDAM 
THE PARIS BIKE REVOLUTION (2018-2025) 

<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>


## Content
[table des matière]

## Project Description

xx

xx

## Workflow

1. Data Collection - Building a database with the historical data on bike counters, cycling network and accidents in Paris.
   - Counter of number of bikes in Paris (2018 to Apr-22) on an hourly basis per counter (Paris Open Data  <https://opendata.paris.fr>)
   - Cycling network in Paris from 2000 to 2021 (Paris Open Data <https://opendata.paris.fr>)
   - Annual databases of road traffic injuries from 2017 to 2020 (<https://data.gouv.fr>)
   - Weather data [OPEN link]
2. Data Cleaning and Processing
   - selection of specific years and Paris area
   - cleaning and processing of each dataset for Tableau data 
   - cleaning and processing of data for Time Series Analysis and Machine Learning
  
5. Time Series Analysis
6. Machine Learning
7. Models testing.
8. Comparison of air pollution in Paris with different cities in Europe.
9. Creating Dashboard.
10. Preparing deliverables (readme file, Git-Hub repository, presenation).

## 01 - Data Collection

### Counter & Infrastructure

The counter data and cycling network were collected using <https://opendata.paris.fr>.  
Data are provided at counter level, on an hourly basis

### Traffic injuries

Accidents data were collected using <https://data.gouv.fr>.  
Data are provided at accident level, with detailed information on the characteristics of accident ++++.


## 04 - Data Cleaning

In order to be consistent between datasets we decided to analyze, we selected years 2018 till now when data were available by filtering on Python.


_______________________________________________________________________________________________________________
The selected data for two cities Paris and Lyon, where cleaned and processed before Time Series and Supervised Machine Learning Analysis. This process was divided into two parts, as for Time Series Analysis only the data for Air Pollution was needed, while for building the Supervised Learning Model was more focused on the weather data.

### Cleaning for Time Series Analysis and EDA

The columns which presented relevant information for Time Series analysis were the columns containing the air pollution and date information, i.e. : 'datetime', 'pm25', 'pm10', 'o3', 'no2', 'so2' and 'co'.

The process of data cleaning and processing included:

- converting datetime column into datetime type.
- missing values processing:
  - columns 'so2' and 'co' were deleted due to the high number of missing values
  - separate missing values were replaced by the average values of each pollutant for the specified month and year.
  - for Paris there was a period of 3 months of missing data in 2017. In this case I decided to input the missing values of each day and each pollutant as an average of these values in 2016 and 2018.
  - for Lyon there was a period of 6 months missing in the second half of 2021. Fortunately, these values, were presented in the other csv file at the air quality data source. Therefore, I imputed the missing values from the different file.
- Outliers. In order to check for outliers, I draw a boxplot graph for each pollutant. Basing on that visual representation of the data I could state that there were no outliers in data recorded both in Paris and Lyon.

### Cleaning for Supervised ML and EDA

The aim of second stage of cleaning was to prepare the data for Supervised Machine Learning and EDA. This process included:

- exchanging columns with information about air quality for the clean ones from the previous stage of cleaning
- changing date type to datetime 
- dropping columns 'latitude', 'longitude', 'address', 'datetimeEpoch', 'description' as they contain wither the same information or too various information, so they are not useful for machine learning model
- Missing values processing:
  - columns 'snow', 'snowdepth', 'solarradiation', and 'solarenergy' were dropped due to the high number of missing values.
  - 1 missing value for precipitation was filled with 0, as from other columns it was clear that it did not rain that day.
  - 'windgust' contained 1 missing value and it was dropped due to the high correlation with windspeed column
  - 1 missing value of pressure was filled with the value from the proceeding day as it presented similar weather conditions.
- 'Conditions' column needed encoding as it was the only categorical column. The column was encoded by creating columns with 0/1 values for each weather condition.
- New columns containing information about month and day of the week were created, as they might be useful for ML model. After that column with date information was dropped.
- The data was checked for collinearity between columns. The correlation matrix was created and one by one columns with the correlation above 90% were dropped. This included: 'tempmax', 'tempmin' (high correlation to 'temp').
- Outliers. The boxplot for numerical columns were drawn. Basing on this visual representation I can conclude that all of the values are in the reasonable range and there were no outliers.
- Column with a target variable was created basing on the recorded values of PM2.5 concentration. This pollutant is often used as an air quality indicator as its concentration is related to the concentration of other pollutants. Therefore, I created three classes basing on the values of PM2.5:
  - Class 0: day with good air quality, PM2.5 concentration below 50 µg/m³.
  - Class 1: day with moderate air quality, PM2.5 concentration between 50 and 100 µg/m³.
  - Class 2: day with bad air quality, PM concentration above 100 µg/m³.
- After creating the target column, the columns with the concentration of pollutants ('pm25', 'pm10', 'o3' and 'no2') were dropped, but this was done before ML, as they were also used for EDA.

The cleaned data ready for Time Series and ML was saved in the separate files.

*Using : python, pandas, numpy, matplotlib, seaborn*

## 05 - Time Series

Time Series Analysis was performed separately for each pollutant (PM2.5, PM10, ozone and nitrogen dioxide) in each city.
The analysis included:

- Stationarity test - all analysed time series data was stationary.
- Autocorrelation check - graphs showing autocorrelation and partial autocorrelation were drawn for each pollutant. These graphs pointed that there is similarity between values for high number of lags.
- Decomposition to see trend line.
- Train/test split in proportion 80/20 to evaluate chosen model.
- Implementation of model proposed by FbProphet liabry firstly for tarin data.
- Calculation of a model error (RMSE - Root Mean Square Deviation)
- Fitting the model on the whole available data.
- Forecasting pollutant concentration for 2022.
- Plotting important figures.

The results of the Time Series Analysis are presented here: <https://air-quality-final-project.herokuapp.com>

The model errors for each model are given in the Table below:

|       | Paris | Lyon |
|-------|-------|------|
| PM2.5 | 20.6  | 19.9 |
| PM10  | 18.2  | 9.2  |
| Ozone | 9.2   | 9    |
| NO2   | 14.7  | 4.2  |

The comparison of the created models with the real data points that the predictions of the model are correct.

*Using : python, pandas, numpy, matplotlib, seaborn, statmodels, pdmarima, fbprohet*

## 06 - Machine Learning

The purpose of this part of the project was to create a supervised machine learning model, which would correctly predict the air quality class (Good, Moderate or Bad) basing on the weather conditions during that day.
For the Supervised Machine Learning part 4 models were evaluated:

- Logistic Regression,
- Random Forest Classifier,
- Balanced Random Forest Classifier, and
- pipeline with models proposed by TPOT library.

The process of Machine Learning Analysis included:

- random train/test split of data in proportion 80/20.
- standardization of the data for Logistic Regression model.
- Features selection using Select From Model, Recursive Feature Elimination and Recursive Feature Elimination with Cross-Validation.
  - The results of feature selection for all models were similar. They proposed following features which were further used for models: 'temp', 'humidity', 'precip', 'windspeed', 'pressure', 'cloudcover', 'visibility', 'uvindex'.
- Hyperparameters Tunning using grid search and randomized search. Interestingly the logistic regression and random forest classifier models were giving better performance using default parameters than the ones proposed from hyperparameters tunning for Paris data, therefore default parameters were used for these models evaluation for Paris. On the other hand, for Lyon the results for hyperparameters tunning were used.
- Evaluations of the Logistic Regression, Random Forest Classifier and Balanced Random Forest Classifier models.
- TOPT implementation:
  - Paris: TPOT proposed Stacking Estimator using Extra Trees Classifier and GaussianNB
  - Lyon: TPOT proposed Stacking Estimator using Extra Trees Classifier and XGBClassifier
- Comparison of obtained results.

For both cities also Unsupervised Machine Learning models (KMeans, Agglomerative Clustering and DBSCAN) were checked in order to verify if data can be properly clustered from the perspective of air pollution. However, the obtain results were not satisfying (Silhouette Coefficient below 0.3). Thus, this part of the project was not developed further.

### Results

#### Paris

The comparison of different models is presented in the Table below and in the Figure showing confusion matrix.

| Model                    | Accuracy, % | Balanced Accuracy, % | f1_score, % |
|--------------------------|-------------|----------------------|-------------|
| Logistic Regression      | 76.2        | 67.7                 | 75.3        |
| Random Forest Classifier | 77.05       | 64.9                 | 76.2        |
| Balanced RF              | 71.8        | 78.5                 | 72.1        |
| Stacking Estimator       | 69.7        | 74.7                 | 70.3        |

![Paris_CM](06_ML/Figures/Paris_cm.png)

Basing on the obtained results I picked Balanced random Forest as the best model for Paris data, as it has high accuracy and the highest balanced Accuracy. Looking at the confusion matrix, this model correctly classified the highest number of days with bad air quality. Thus, I recommend using this model to predict air quality from weather data in Paris.

#### Lyon

The comparison of different models is presented in the Table below and in the Figure showing confusion matrix.

| Model                    | Accuracy, % | Balanced Accuracy, % | f1_score, % |
|--------------------------|-------------|----------------------|-------------|
| Logistic Regression      | 79.1        | 69.1                 | 78.3        |
| Random Forest Classifier | 81.7        | 69.9                 | 81.1        |
| Balanced RF              | 76.9        | 79.3                 | 76.7        |
| Stacking Estimator       | 83.4        | 73.2                 | 83.4        |

![Lyon_CM](06_ML/Figures/Lyon_cm.png)

The similar case as for Paris can be observed for Lyon. Here the highest balanced accuracy was obtained with Balanced random Forest model. However, the model proposed by TPOT i.e. Stacking Estimator also shows very good results. Therefore, I would recommend one of these two models to predict air quality in Lyon using weather data.

*Using : python, pandas, numpy, matplotlib, seaborn, sklearn, imblearn, tpot, yellowbrick*

## 07 - EDA

Exploratory Data Analysis was divided into two parts:

- firstly, the historical data on air pollution and weather in Paris and Lyon was analysed and compared
- secondly, the results of Time Series with the forecast for 2022 were analysed.

The appropriate graphs were prepared. They can be found in the Jupyter notebook as well as on the Streamlit dashboard.

*Using : python, pandas, matplotlib, seaborn, plotly, folium*

## 08 - Streamlit Dashboard

The results of EDA were used in order to prepare a dashboard app using Streamlit library.

The app can be visited here:

[Stramlit_App](https://air-quality-final-project.herokuapp.com)

*Using : Streamlit, plotly, pillow*

#### Deploying to Heroku

The prepared dashboard/app was published using Heroku

```bash
heroku git:remote -a air-quality-final-project
git subtree push --prefix "08 - Streamlit" heroku main
```

![Dashboard](08_Streamlit/Figures/Dashboard.png)

*Using : git, heroku*

## Conclusions

- xx

## Links

[Dashboard](x)

[Repository](x)

[Trello](https://trello.com/b/Vb4Buvk8/finalproject)


