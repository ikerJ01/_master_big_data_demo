""" Importar datos en crudo desde la fuente de datos
    Se renombrarán las columnas para estandarizar las variables a lo largo del análisis
    """
import pandas as pd

url = 'https://www.dropbox.com/s/cntx8m0uubigrsi/python_data_converter_repository.xlsx?dl=1'

table_title_1 = 'clicks'
table_title_2 = 'sales'
table_title_3 = 'views'
table_title_4 = 'product_list'
table_title_5 = 'master_data'
table_title_6 = 'states_timer'
table_title_7 = 'findability'

table_clicks = pd.read_excel(url,sheet_name = table_title_1)
df_table_clicks = pd.DataFrame(table_clicks)
df_table_clicks.rename(columns = {'idmaster_data':'idMaster', 'idSurvey':'survey_id','idCell':'cell_id','sequence':'sequence_clicks', 'time':'time_clicks'}, inplace = True)
df_table_clicks['idMaster'] = df_table_clicks['idMaster'].apply(str)
df_table_clicks['survey_id'] = df_table_clicks['survey_id'].apply(str)
df_table_clicks['idProduct'] = df_table_clicks['idProduct'].apply(str)

table_sales = pd.read_excel(url,sheet_name = table_title_2)
df_table_sales = pd.DataFrame(table_sales)
df_table_sales.rename(columns = {'idmaster_data':'idMaster', 'idSurvey':'survey_id','idCell':'cell_id','sequence':'sequence_sales', 'time':'time_sales'}, inplace = True)
df_table_sales['idMaster'] = df_table_sales['idMaster'].apply(str)
df_table_sales['survey_id'] = df_table_sales['survey_id'].apply(str)
df_table_sales['idProduct'] = df_table_sales['idProduct'].apply(str)

table_views = pd.read_excel(url,sheet_name = table_title_3)
df_table_views = pd.DataFrame(table_views)
df_table_views.rename(columns = {'idmaster_data':'idMaster', 'idSurvey':'survey_id','idCell':'cell_id','sequence':'sequence_views', 'timer':'timer_views_raw','was_viewed':'was_viewed_raw'}, inplace = True)
df_table_views['idMaster'] = df_table_views['idMaster'].apply(str)
df_table_views['survey_id'] = df_table_views['survey_id'].apply(str)
df_table_views['idProduct'] = df_table_views['idProduct'].apply(str)

table_product_list = pd.read_excel(url,sheet_name = table_title_4)
df_product_list = pd.DataFrame(table_product_list)
df_product_list.rename(columns = {'idCell':'cell_id'}, inplace = True)
df_product_list['idProduct'] = df_product_list['idProduct'].apply(str)
df_product_list['index_pd'] = df_product_list['index_pd'].apply(str)

table_master_data = pd.read_excel(url,sheet_name = table_title_5)
df_table_master_data = pd.DataFrame(table_master_data)
df_table_master_data.rename(columns = {'idSurvey':'survey_id','idCell':'cell_id','idmaster_data':'idMaster'}, inplace = True)
df_table_master_data['survey_id'] = df_table_master_data['survey_id'].apply(str)
df_table_master_data['idMaster'] = df_table_master_data['idMaster'].apply(str)

table_states_timer = pd.read_excel(url,sheet_name = table_title_6)
df_table_states_timer = pd.DataFrame(table_states_timer)
df_table_states_timer.rename(columns = {'idSurvey':'survey_id','idCell':'cell_id','idmaster_data':'idMaster'}, inplace = True)
df_table_states_timer['survey_id'] = df_table_states_timer['survey_id'].apply(str)
df_table_states_timer['idMaster'] = df_table_states_timer['idMaster'].apply(str)

table_findability = pd.read_excel(url,sheet_name = table_title_7)
df_table_findability = pd.DataFrame(table_findability)
df_table_findability.rename(columns = {'idmaster_data':'idMaster', 'idSurvey':'survey_id','idCell':'cell_id','sequence':'sequence_findability', 'timer':'timer_findability'}, inplace = True)
df_table_findability['idMaster'] = df_table_findability['idMaster'].apply(str)
df_table_findability['survey_id'] = df_table_findability['survey_id'].apply(str)
df_table_findability['idProduct'] = df_table_findability['idProduct'].apply(str)
df_table_findability['target_idProduct'] = df_table_findability['target_idProduct'].apply(str)
