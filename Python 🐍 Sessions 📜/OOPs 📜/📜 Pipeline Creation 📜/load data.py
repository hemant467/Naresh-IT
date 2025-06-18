import pandas as pd

class DATA_READ:
    def __init__(self,data):
        self.data=data
    def read_csv(self):
        df=pd.read_csv(self.data)
        return(df)

if __name__=="__main__":
    df=DATA_READ("Visadataset.csv").read_csv()
    print(df.head())