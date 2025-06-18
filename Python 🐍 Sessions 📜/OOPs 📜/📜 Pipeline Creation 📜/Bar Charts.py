import matplotlib.pyplot as plt


class CHARTS:
    def __init__(self,keys,values):
        self.keys=keys
        self.values=values
    def bar_plot(self):
        plt.bar(self.keys,self.values)
        plt.savefig('bar_chart.jpg')

