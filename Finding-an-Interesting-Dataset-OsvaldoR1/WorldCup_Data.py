import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

WorldCup_data = pandas.read_csv("{international_matches.csv}")