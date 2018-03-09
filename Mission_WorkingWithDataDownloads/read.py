import pandas

contents = pandas.read_csv("/home/dq/scripts/data/CRDC2013_14.csv")
#print (contents.head())
print (contents.columns.tolist())
