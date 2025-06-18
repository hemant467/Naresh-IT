import pandas as pd

class Tables:
    def __init__(self,df,col):
        self.df=df
        self.col=col
    def table_df(self):
        
        keys=self.df[self.col].value_counts().keys()
        values=self.df[self.col].value_counts().values
        table_data=pd.DataFrame(zip(keys,values))
        return(keys,values,table_data)