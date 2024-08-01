
# Ames Housing Market Analysis Project
# Project Overview
The Ames Housing Market Analysis Project is designed to assist a real estate investment firm in identifying undervalued properties in Ames with potential for significant investment returns. By analyzing market dynamics and identifying properties undervalued relative to their market potential, the project aims to facilitate strategic investments in the real estate market.
<br>
**Data set used in this project**: [Dataset](https://jse.amstat.org/v19n3/decock/DataDocumentation.txt)
<Br>

# Project Objectives
- Market Analysis: Analyze the Ames housing market to identify undervalued properties.
- Feature Engineering: Refine the dataset by removing or transforming features that do not contribute to predicting the target variable.
- Model Development: Develop and refine predictive models to estimate property sale prices.
- Investment Strategy: Identify properties with the greatest potential for profitable investment based on model predictions.
# Data Preprocessing
Feature Selection and Transformation
- Low Variability Features: Features with 95% or more observations showing the same value were removed due to their lack of predictive power.
- Categorical Features: ms_subclass and mo_sold were treated as categorical variables since their numerical values do not imply a quantitative hierarchy.
- Outliers: Outliers were identified and potentially removed to improve model accuracy.
- Zero-Value Features: Features with a high frequency of zero values were examined for their impact on the target variable.
- Target Distribution: A log transformation was applied to the target variable (sale price) to better fit a normal distribution.
(2) Collinearity
- Multicollinearity Check: Collinear features were identified using a heatmap and Variance Inflation Factor (VIF). High collinearity among year_remod/add, garage_yr_blt, and year_built led to retaining only the feature with the highest correlation to the target variable.

# Dataset Transformation
Several variations of the dataset were prepared for model training: <Br>
(1) Standardized Columns: Basic standardization.<Br>
(2) Filtered Columns: Standardization with removal of low-variability features.<Br>
(3) Outlier Removal: Further refinement by removing outliers.<Br>
(4) Zero-Value Adjustment: Adjusting zero values in the dataset.<Br>
The third variation (standardization, filtering, and outlier removal) demonstrated the best performance and was selected for final model development.

# Model Development
## Model Selection
- Linear Regression Models: Linear Regression, Ridge, and Lasso regularizations were tested.
- Best Performing Model: Ridge Regression with an alpha of 20 provided the best results, achieving an R² score of 95% in cross-validation.
- Imputation Techniques: <Br>
Categorical Data: Missing values were filled with the mode, which provided better performance than filling with 'missing'. <br>
Numerical Data: Imputation with the mean was selected as the best technique.
## Results and Insights
The Ridge Regression model predicted property sale prices with high accuracy (R² score of 95%). The model identified properties that, according to its predictions, could yield significant returns on investment, with predicted gains ranging from $350,000 to $500,000. However, the discrepancy between predicted and actual sale prices suggests further investigation is needed to ensure the reliability of these investment opportunities.

# Conclusion
This project provided valuable insights into the Ames housing market, highlighting potential investment opportunities. The high accuracy of the predictive model supports its utility in strategic decision-making for real estate investments. Future work may include refining the model further, investigating the causes of discrepancies in predictions, and exploring additional factors that influence property values.
