
#######################################################################
#    VIEWS DATA SOURCE TABLE
#######################################################################
# Applies the following logics:
#           If a product is hovered more than 0.5 seconds then it will be counted as was_viewed
#           If a product is hovered less than 0.5 seconds but was clicked, it will be considered as was_viewed and attibute a timer of 0.5 seconds
#           Scrip will compensate those clicks without views and create the new entries in the final data frame attributing a was_viewed and a timer of 0.5 seconds

import pandas as pd

exec(open("02_source_tables_cleanup.py").read())

#%% md
# Join clicks & views tables | outter join is kept to compensate clickes not viewed
# #---------------------

views_merge_1 = pd.merge(clicks_data_clean_df,
                         views_data_clean_df,
                         left_on=['idMaster', 'survey_id', 'cell_id','idProject','idProduct', 'description', 'price', 'outlier', 'index_pd', 'brand', 'product_category'],
                         right_on=['idMaster', 'survey_id', 'cell_id','idProject','idProduct', 'description', 'price', 'outlier', 'index_pd', 'brand', 'product_category'],
                         how = 'outer')

df_views_merge_1 = pd.DataFrame(views_merge_1).fillna(0)


# Function to add to the was_viewed variable those products that were clicked
# #---------------------
def was_viewed_adjuster(df_views_merge_1):
    if df_views_merge_1['was_clicked'] == 1 and df_views_merge_1['was_viewed_raw'] == 0:
        return  1
    elif df_views_merge_1['was_clicked'] == 1 and df_views_merge_1['was_viewed_raw'] == 1:
        return df_views_merge_1['was_viewed_raw']
    elif df_views_merge_1['was_clicked'] == 0 and df_views_merge_1['was_viewed_raw'] == 1 and df_views_merge_1['timer_views_raw'] >= 0.5:
        return df_views_merge_1['was_viewed_raw']
    else:
        return 0

df_views_merge_1['was_viewed'] = df_views_merge_1.apply(was_viewed_adjuster, axis=1)


# Function to add to the timer variable those products that were clicked
# #---------------------
def timer_views_adjuster(df_views_merge_1):
    if df_views_merge_1['was_clicked'] == 1 and df_views_merge_1['was_viewed_raw'] == 0:
        return 0.5
    elif df_views_merge_1['was_clicked'] == 1 and df_views_merge_1['was_viewed_raw'] == 1 and df_views_merge_1['timer_views_raw'] >= 0.5:
        return df_views_merge_1['timer_views_raw']
    elif df_views_merge_1['was_clicked'] == 1 and df_views_merge_1['was_viewed_raw'] == 1 and df_views_merge_1['timer_views_raw'] < 0.5:
        return 0.5
    elif df_views_merge_1['was_clicked'] == 0 and df_views_merge_1['was_viewed_raw'] == 1 and df_views_merge_1['timer_views_raw'] >= 0.5:
        return df_views_merge_1['timer_views_raw']
    else:
        return 0

df_views_merge_1['timer_views'] = df_views_merge_1.apply(timer_views_adjuster, axis=1)

# Cleaning the views data frame from redundant columns
# #---------------------
df_views_cleanup = df_views_merge_1[['idMaster','cell_id','survey_id','idProject','idProduct','was_viewed','timer_views', 'description', 'price', 'outlier', 'index_pd', 'brand', 'product_category']]

views_data_clean_final_df = df_views_cleanup[df_views_cleanup['was_viewed'] == 1]

