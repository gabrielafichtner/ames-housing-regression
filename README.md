# Project 2 - Ames Housing Data and Kaggle Challenge

Bobble Bee investment fund has the goal to study the real state market of Ames. Predictions of the price of realty were made using the realty characteristics present in Ames Housing dataset and, after that, those predictions were compared to the actual value for studying potential investment gains.
In this project, the predictions were made with linear regression exploring different strategies.

**Cleaning data:**

1. Variables that were only present in 20% or less of the dataset were not considered, since it is difficult to generalize them.
1. Variables that 90% or more of the variables fit only in one category were not considered, there is huge variability in 95% of the dataset and we cannot differentiate that when its all in one category
2. Variables considered to be ordinal that were string type were transformed to numerical.
3. Null Values in variables considered as dummies were filled with 0.
4. Null values in numerical variables were filled with the mean.


**Data set used in this project **
3. [Dataset](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

**Modeling strategies**
- Transforming the target variable to its logarithm the R2 score was 90.3%%
- After removing outliers of ground living area, the 92.3%
- Using Ridge regression with an alpha of 10 led to R2 score of 91.2% in the test set.

That is, 91.2% of the variability of sale price can be explained by the model.
