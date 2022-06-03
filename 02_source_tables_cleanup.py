""" Actualización de todas las tablas de interacciones para descartar los outlier
    Se actualizarán todas las tablas para incluir la información sobre cada producto (Price, Description, Brand, Category)
    """

import pandas as pd

exec(open("01_source_tables.py").read())

final_outliers = pd.read_csv('final_outliers.csv')
final_outliers = pd.DataFrame(final_outliers)
final_outliers['idMaster'] = final_outliers['idMaster'].apply(str)
final_outliers['survey_id'] = final_outliers['survey_id'].apply(str)

# Master Data Update
#----------
master_data_df = pd.merge(df_table_master_data,
                          final_outliers,
                          left_on= ['idMaster', 'cell_id', 'survey_id'],
                          right_on= ['idMaster', 'cell_id', 'survey_id'],
                          how='left').reset_index().fillna('0')
master_data_df.drop(columns='index', inplace=True)



# Sales Data Update
#----------
sales_data_clean_df = pd.merge(df_table_sales,
                               master_data_df,
                               left_on= ['idMaster', 'cell_id', 'survey_id'],
                               right_on= ['idMaster', 'cell_id', 'survey_id'],
                               how='outer').reset_index().fillna('0')

sales_data_clean_df = sales_data_clean_df[sales_data_clean_df['outlier'] != 1]
sales_data_clean_df.drop(columns='index', inplace=True)

sales_data_clean_df = pd.merge(sales_data_clean_df,
                               df_product_list,
                               left_on= ['cell_id', 'idProduct', 'idProject'],
                               right_on= ['cell_id', 'idProduct', 'idProject'],
                               how='left').reset_index()

sales_data_clean_df['total_spend'] = sales_data_clean_df['units_sold'] * sales_data_clean_df['price']
sales_data_clean_df.drop(columns='index', inplace=True)

# Clicks Data Update
#----------
clicks_data_clean_df = pd.merge(df_table_clicks,
                                master_data_df,
                                left_on= ['idMaster', 'cell_id', 'survey_id'],
                                right_on= ['idMaster', 'cell_id', 'survey_id'],
                                how='outer').reset_index().fillna('0')

clicks_data_clean_df = clicks_data_clean_df[clicks_data_clean_df['outlier'] != 1]
clicks_data_clean_df.drop(columns='index', inplace=True)

clicks_data_clean_df = pd.merge(clicks_data_clean_df,
                                df_product_list,
                                left_on= ['cell_id', 'idProduct', 'idProject'],
                                right_on= ['cell_id', 'idProduct', 'idProject'],
                                how='left').reset_index()

clicks_data_clean_df.drop(columns='index', inplace=True)

# Views Data Update
#----------
views_data_clean_df = pd.merge(df_table_views,
                               master_data_df,
                               left_on= ['idMaster', 'cell_id', 'survey_id'],
                               right_on= ['idMaster', 'cell_id', 'survey_id'],
                               how='outer').reset_index().fillna('0')

views_data_clean_df = views_data_clean_df[views_data_clean_df['outlier'] != 1]
views_data_clean_df.drop(columns='index', inplace=True)

views_data_clean_df = pd.merge(views_data_clean_df,
                               df_product_list,
                               left_on= ['cell_id', 'idProduct', 'idProject'],
                               right_on= ['cell_id', 'idProduct', 'idProject'],
                               how='left').reset_index()

views_data_clean_df.drop(columns='index', inplace=True)

# Findability Data Update
#----------

findability_data_clean_df = pd.merge(df_table_findability,
                                     df_product_list,
                                     left_on= ['cell_id', 'idProduct', 'idProject'],
                                     right_on= ['cell_id', 'idProduct', 'idProject'],
                                     how='left').reset_index()

findability_data_clean_df.drop(columns='index', inplace=True)


def correct_find(findability_data_clean_df):
    if findability_data_clean_df['idProduct'] == findability_data_clean_df['target_idProduct']:
        return  True
    return False

findability_data_clean_df['validator'] = findability_data_clean_df.apply(correct_find, axis= 1)

# Master Data Final Update
#----------
master_data_df = master_data_df[master_data_df['outlier'] != 1]