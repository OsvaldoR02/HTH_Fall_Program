import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

WorldCup_data = pandas.read_csv("{FIFA_official_data.csv}")