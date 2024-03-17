
import pandas as pd
import numpy as np


class Original():
    def __init__(self):
        
        # numericals that are actually category features
        self.cat_features = ['ms_subclass', 'mo_sold']
        
        # to filter columns when the class is called
        self.train_columns = ['land_contour', 'bsmt_qual', 'bsmtfin_sf_2', 'screen_porch', 'lot_area', 'overall_qual',\
                          'full_bath', 'totrms_abvgrd', 'mo_sold', 'exter_cond', 'ms_subclass', 'heating_qc',\
                          '1st_flr_sf', 'bsmtfin_type_2', 'neighborhood', 'kitchen_qual', 'exterior_2nd',\
                          'central_air', 'garage_qual', 'garage_type', 'half_bath', 'bldg_type', 'lot_config',\
                          'functional', 'exterior_1st', 'garage_cars', 'exter_qual', 'open_porch_sf',\
                          'bsmt_exposure', 'alley', 'electrical', 'bedroom_abvgr', 'bsmt_full_bath',\
                          'condition_1', '2nd_flr_sf', 'fence', 'garage_area', 'mas_vnr_type', 'fireplace_qu',\
                          'overall_cond', 'bsmt_cond', 'enclosed_porch', 'bsmt_half_bath', 'ms_zoning',\
                          'fireplaces', 'paved_drive', 'bsmtfin_type_1', 'foundation', 'roof_style',\
                          'garage_finish', 'lot_frontage', 'lot_shape', 'bsmt_unf_sf', 'year_built',\
                          'bsmtfin_sf_1', 'gr_liv_area', 'sale_type', 'house_style', 'mas_vnr_area',\
                          'total_bsmt_sf', 'wood_deck_sf', 'yr_sold', 'saleprice', 'id']

        # to filter columns when the class is called
        self.x_columns = ['land_contour', 'bsmt_qual', 'bsmtfin_sf_2', 'screen_porch', 'lot_area', 'overall_qual',\
                          'full_bath', 'totrms_abvgrd', 'mo_sold', 'exter_cond', 'ms_subclass', 'heating_qc',\
                          '1st_flr_sf', 'bsmtfin_type_2', 'neighborhood', 'kitchen_qual', 'exterior_2nd',\
                          'central_air', 'garage_qual', 'garage_type', 'half_bath', 'bldg_type', 'lot_config',\
                          'functional', 'exterior_1st', 'garage_cars', 'exter_qual', 'open_porch_sf',\
                          'bsmt_exposure', 'alley', 'electrical', 'bedroom_abvgr', 'bsmt_full_bath',\
                          'condition_1', '2nd_flr_sf', 'fence', 'garage_area', 'mas_vnr_type', 'fireplace_qu',\
                          'overall_cond', 'bsmt_cond', 'enclosed_porch', 'bsmt_half_bath', 'ms_zoning',\
                          'fireplaces', 'paved_drive', 'bsmtfin_type_1', 'foundation', 'roof_style',\
                          'garage_finish', 'lot_frontage', 'lot_shape', 'bsmt_unf_sf', 'year_built',\
                          'bsmtfin_sf_1', 'gr_liv_area', 'sale_type', 'house_style', 'mas_vnr_area',\
                          'total_bsmt_sf', 'wood_deck_sf', 'yr_sold', 'id']         
        
        
        # features that will have outliers removed
        self.outliers_features = {'gr_liv_area': 4000, 'bsmtfin_sf_1': 3000, 'wood_deck_sf': 1000,\
                                   '1st_flr_sf': 3500, 'lot_frontage': 250, 'lot_area':100000,\
                                   'total_bsmt_sf': 4000}
        
        
        # features that have more than 10% of observations with zero
        self.zero_features = ['bsmtfin_sf_1', 'bsmtfin_sf_2', 'enclosed_porch', 'open_porch_sf', 'wood_deck_sf', \
                              'mas_vnr_area', 'screen_porch', '2nd_flr_sf']  
       
        
        
    def zeros(self, dataset):
        for feature in self.zero_features:
            mask = dataset[feature] == 0
            dataset.loc[mask, feature] = np.nan
            dataset.loc[mask, feature] = dataset[feature].mean()
        return dataset
    
    
    def outliers(self, dataset):
        for feature, threshold in self.outliers_features.items():
            mask = (dataset[feature] <= threshold) | (dataset[feature].isnull())
            dataset = dataset[mask]
        return dataset

    
    def __call__(self, dataset):
        df = dataset.copy()
        #standardizing columns names
        df.columns = df.columns.str.lower().str.replace(' ','_')
        df[self.cat_features] = df[self.cat_features].astype('category')
        if ['id', 'pid'] in list(df.columns):
            df = df.drop(['id', 'pid'], axis=1)
        return df


# Class filtering columns
class Train_Columns(Original):
    def __call__(self, dataset):
        df = super().__call__(dataset)
        df = df[self.train_columns]
        return df


# Class filtering columns and outliers
class Train_Outliers(Train_Columns):
    def __call__(self, dataset):
        df = super().__call__(dataset)
        df = self.outliers(df)
        return df


# Class filtering columns and changing zeros
class Train_Zeros(Train_Columns):
    def __call__(self, dataset):
        df = super().__call__(dataset)
        df = self.zeros(df)
        return df

class X_Columns(Original):
    def __call__(self, dataset):
        df = super().__call__(dataset)
        df = df[self.x_columns]
        df = self.outliers(df)
        return df
