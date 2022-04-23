# PANAMSTERDAM 
THE PARIS BIKE REVOLUTION (2018-2025) 

<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>


## Project Description



xx

## Workflow

1. Data Collection - Building a database with the historical data on bike counters, cycling network and accidents in Paris.
   - Counter of number of bikes in Paris (2018 to Apr-22) on an hourly basis per counter (Paris Open Data  <https://opendata.paris.fr>)
   - Cycling network in Paris from 2000 to 2021 (Paris Open Data <https://opendata.paris.fr>)
   - Annual databases of road traffic injuries from 2017 to 2020 (<https://data.gouv.fr>)
   - Weather data [OPEN link]
   - Bike user's comments from last Barometer of cyclable cities in France (<https://opendata.parlons-velo.fr>) 
2. Data Cleaning and Processing
   - selection of specific years and Paris area
   - cleaning and processing of each dataset for Tableau data 
   - cleaning and processing of data for Time Series Analysis and modelling 
3. Time Series Analysis
4. Modelling
5. Creating Dashboard
6. Preparing deliverables (readme file, Git-Hub repository, presenation).

## 01 - Data Collection

### Counter & Infrastructure

The counter data and cycling network were collected using:
<https://www.data.gouv.fr/fr/datasets/comptage-velo-historique-donnees-compteurs-et-sites-de-comptage/>
<https://www.data.gouv.fr/fr/datasets/plan-de-voirie-pistes-cyclables-et-couloirs-de-bus/>

Data are provided at counter level, on an hourly basis

### Traffic injuries

Accidents data were collected using <https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/>.  
Data are provided at accident level, with detailed information on the characteristics of accident (location, gravity, number of peoples involved etc.).

### Weather

Meteo data were collected using <https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/export/?q.timerange.date=date:%5B2017-12-31T23:00:00Z+TO+2022-04-18T21:59:59Z%5D&q=paris&refine.nom=ORLY> taking the closer to Paris location (Orly).

### Qualitative data 

Corpus of more than 3900 comments made by parisian bike users regarding their daily riding experience in the city. Collected from <https://opendata.parlons-velo.fr/datasets/75056.zip>.


## 02 - Data Cleaning

In order to be consistent between datasets we decided to analyze, we selected years 2018 till now when data were available by filtering on Python. The idea was to be able to use cleaned and ready-to-use data for tableau vizualisation. 
For qualitative data, we tried different libraries for cleaning, normalizing, lemmatizing in order to be able to implement a sentiment analysis on comments.  


## 03 - Time Series Analysis

We tried different approaches on time series analysis. In fact, main problem was about the non like-for-like perimeter of counters which creates imbalanced growth throughout the period (45 in 2018 vs. 107 in 2022). In order to be consistent, we decided to plot a counting hourly average.
As we had seasonality, exceptional events with Covid, we decided to run Prophet model which is able to take into account this kind of parameters. 

We isolated french holidays as well as first Covid lockdown (17/03/2020 to 03/05/2020) in order to be as precise as possible. 
Prophet is an additive forecasting model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday/exceptional events effects.

Prophet uses a decomposable time series model with three main model components: trend, seasonality, and holidays. They are combined in the following equation:
y(t) = g(t) + s(t) + h(t) + e(t)

-g(t) is a trend function which models the non-periodic changes. It can be either a linear function or a logistic function.

-s(t) represents a periodic changes i.e weekly, monthly, yearly. An yearly seasonal component is modeled using Fourier series and weekly seasonal component using dummy variables.

- h(t) is a function that represents the effect of holidays which occur on irregular schedules.(n≥1 days)

- The term e(t) represents error changes that are not accommodated by the model.

We present final forecast in a plotly graph, as well as components of the time series. 


# 04 - EDA

Exploratory Data Analysis was divided into two parts:

- firstly, the historical data were analysed and compared
- secondly, the results of Time Series with the forecast for 2023-2024 were analysed.

The appropriate graphs were prepared on Tableau and plotly.


## 05 - Machine Learning

We decided to run a TPOT Classifier to perform the search over the best marchine learning model for modelling accidents gravity.
We were looking for a correct model to predict the accident class, focusing on the main gravity of accidents: unharmed vs. slight injury (excludint hospitalized injured and killed people as they represent c.100 person out of 3800)

Best model has an accuracy of 69% on train data and 68% on test data:
exported_pipeline = make_pipeline(
    VarianceThreshold(threshold=0.01),
    DecisionTreeClassifier(criterion="entropy", max_depth=7, 
                           min_samples_leaf=16, min_samples_split=15))


## 06 - Tableau Dashboard

The Tableau story can be visited here:

[Tableau story](<https://public.tableau.com/app/profile/masson8212/viz/Panamsterdam_finalstory/FinalPresentation?publish=yes>)


## Conclusions

- xx

## Links

[Dashboard](x)

[Repository](x)

[Trello](https://trello.com/b/Vb4Buvk8/finalproject)


