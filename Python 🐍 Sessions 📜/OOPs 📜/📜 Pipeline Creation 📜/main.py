from load_data import DATA_READ
from frequency_tables import Tables
from Bar_charts import CHARTS

df=DATA_READ("Visadataset.csv").read_csv()
keys,values,table_data=Tables(df,'continent').table_df()
CHARTS(keys,values).bar_plot()
