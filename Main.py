import DataNormalization

data = DataNormalization.Data("data/results.csv")
data.open_csv_file()
data.calc_avg_and_deviation()
data.normalize("data/results_nor.csv")