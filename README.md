# Ames Housing Data and Kaggle Challenge

The Ames housing market is the subject of study for a real estate investment firm seeking to identify undervalued properties with potential for investment and subsequent gains.
This project's objective is to analyze the market dynamics of Ames to pinpoint opportunities for strategic investment. By identifying properties that are undervalued relative to their market potential, the firm aims to capitalize on opportunities for profitable real estate investments.

This identification was performed creating a linear model with the highest R2 score and comparing to current sale price in the market.

**Data set used in this project**: [Dataset](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

## Cleaning data:
- Unique identifiers were removed from the model, since they are not to be used in the model.
- Features that had more than 95% of observations having one unique value were selected to test further for model improvement. Variables with such high concentration do not have much variability that translates to variability of the target variable.
- Features with outliers and their respective limit value were selected to test further for model improvement.
- Target's distribution was right long-tailed and was log transformed to fit a more normal distribution while modelling.
- Multicollinearity was explored by analyzing correlation between variables, variables that presented a correlation higher than 50% had the variance inflaction factor (VIF) calculated to check for multicollinearity. Three variables (year_built, year_remod/add and garage_yr_blt) presented high VIF and keeping the variable with highest correlation to the target (year_built) was tested for model improvement.

## Suggested Modifications
Classes with the suggested modifications were created to test R2 score.<br>
(1) Original Data<br>
(2) Filtered columns: columns with >95% of observations having one unique value and multicollinear columns<br>
(3) 2 + removing ourliers<br>
(4) 2 + replacing zeros in features with many zeros<br>

## Modeling strategies
- Applied Linear Regression to the different classes created: the class with filtered columns and outliers removed had the best r2 score using cross validation with 5 fold.
- Tested different imputation methods for both categorical and numerical variables. For categorical, filling with 'missing' and filling with the most frequent value were tested, where the latter perform slightly better. For numerical, mean, mode, iterative imputer with default parameters and KNN imputer with weights being uniform and distance were tested. Filling with the mean led to the best r2 score.
- Tested Ridge and Lasso Regression using randomized search for alpha parameter with cross validation with 5 fold

## Best Model
Ridge Regression with alpha = 20 had a R2 score of 95%. That is, 95% of the variability of sale price can be explained by the model.

## Investment Gains 
Based on the model, there are realty that would lead to the gains of investment ranging between 350,000 and 500,000 dollars. These realty had the actual saleprice much cheaper than predicted, so I would recommend to take a closer look at them.
