import pandas as pd
from env import host, user, password


def get_connection(db, user = user, host = host, password = password):
    '''
    This function takes in as arguments the database, username, host, and password for 
    the mysql database and returns a string that can be used to open a connection to the server
    and query the db in the read_sql function. 
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def telco_data():
    '''
    This function reads the telco data from the Codeup db into a df,
    write it to a csv file, and returns the df.
    '''
    # Create SQL query.
    sql_query = """
                SELECT * FROM customers
                JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING(internet_service_type_id)
                JOIN payment_types USING(payment_type_id);
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df


def save_telco_data():
    '''
    This function takes the telco data from the Codeup db, saves it to a csv file and if it does not exist
    in the local drive, saves the file as a csv.
    '''
    
    if os.path.isfile('telco.csv'):
        # If telco DataFrame is saved to local drive, the file is read from the local drive
        df = pd.read_csv('telco.csv', index_col = 0)
        
    else:
        # Read telco data from Codeup db
        df = telco_data()
        
        # Save DataFrame to CSV file
        df.to_csv('telco.csv')
        
    return df
        
