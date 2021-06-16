import plotly.figure_factory as pff
import pandas as pd

df = pd.read_csv("dataMobileAverageRating.csv")

distplot_graph = pff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
distplot_graph.show()