import pandas as pd
import sys

filename = sys.argv[1]
outfile = sys.argv[2]
proc_outfile = sys.argv[3]

df = pd.read_excel(filename)
print("file read")
df = df.pivot(index="Temperature", columns="Well Position", values="Fluorescence")


alpha = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O", "P"]
num = df.columns.size
num = num/16
num = max(int(num),1)
labels = []
for i in range(num):
    for letter in alpha:
        string = letter + str(i+9)
        labels.append(string)

df = df.reindex(labels, axis="columns")

df.to_excel(outfile)
print("file written")

def normalize(x, max, min):
    y = (x-min)/(max-min)
    return y

for (column, items) in df.iteritems():
    min = items.min()
    max = items.max()
    norm = max - min
    items = items.subtract(min)
    items = items.divide(norm)
    df[column] = items

df.to_excel(proc_outfile)
print("processed file written")
