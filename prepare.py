from pandas import DataFrame
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def clean_telco(df):
    '''
    This functions takes in the telco_db combined into a single dataframe as an argument,
    drops duplicate values and columns, replaces values 'No phone service' and 'No internet 
    service' to 'No', updates the data type of the total_charges column, transforms object 
    type columns, minus churn, into dummies and drops parent dummy columns. Since drop_first is
    set to false, dummy no columns are dropped and senior citizen is renamed and changed its
    type for consistency purposes. Finally, the function drops 12 rows of data from missing 
    values in the total_charges column.
    '''
    df.drop_duplicates(inplace = True)
    df.replace(to_replace = {'No phone service':'No', 'No internet service':'No'}, inplace = True)
    dropped_columns = ['payment_type_id', 'internet_service_type_id', 'contract_type_id',
       'customer_id']
    df_dropped = df.drop(columns = dropped_columns)
    df_dropped = df_dropped.replace(r'^\s*$', np.nan, regex = True)
    df_dropped.total_charges = df_dropped.total_charges.astype('float64')
    obj_cols_name = df_dropped.columns[[df_dropped[col].dtype == 'object' for col in df_dropped.columns]]
    obj_cols_name = obj_cols_name.to_list()
    obj_cols_name.remove('churn')
    df_dummies = pd.get_dummies(df_dropped[obj_cols_name], drop_first = False)
    df_concat = pd.concat([df_dropped, df_dummies], axis = 1)
    df_concat = df_concat.drop(columns = obj_cols_name)
    dummy_no = [ 'partner_No', 'dependents_No', 'phone_service_No', 'multiple_lines_No', 
            'online_security_No', 'online_backup_No', 'device_protection_No', 
            'tech_support_No', 'streaming_tv_No', 'streaming_movies_No',
            'paperless_billing_No',]
    dummy_drop = df_concat.drop(columns = dummy_no)
    dummy_drop.rename(columns = {'senior_citizen':'senior_citizen_Yes'}, inplace = True)
    dummy_drop.senior_citizen_Yes = dummy_drop.senior_citizen_Yes.astype('uint8')
    df_cleaned = dummy_drop[dummy_drop.total_charges.notnull()]
    df_cleaned['monthly_avg'] = df_cleaned['total_charges']/df_cleaned['tenure'] 
    
    return df_cleaned

def train_validate_test_split(df, seed = 123):
    '''
    This functions takes in the cleanted telco dataframe as an argument and a random seed, and splits 
    the dataframe into train, validate and test samples. The test size is 20% of the data, the validate
    size is 24% of the data and the train is 56% of the data. Finally, the function returns 3 dataframes:
    train, validate and test.
    '''    
    train_and_validate, test = train_test_split(
            df, test_size = 0.2, random_state = seed, stratify = df.churn
                                                )
    train, validate = train_test_split(
            train_and_validate, 
            test_size = 0.3, 
            random_state = seed, 
            stratify = train_and_validate.churn
                                       )
    return train, validate, test


def clean_split_telco(df):
    '''
    This function runs both the clean_titanic and train_validate_test_split functions. This functins takes
    in as argument the telco dataframe from the SQL pull, cleans it, splits it, and returns 3 dataframes:
    train, validate and test.
    '''
    cleaned_df = clean_telco(df)
    train, validate, test = train_validate_test_split(cleaned_df, seed = 123)
    return train, validate, test