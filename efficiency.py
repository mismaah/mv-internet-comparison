"""Script to generate comparisons."""

import pandas

df = pandas.read_csv("plans.csv")
df = df.drop(df.columns[[5, 6]], axis=1)
df["Price per GB"] = round(df["Price"] / df["Fair Usage"], 2)
df = df.sort_values(by=["Price per GB"])
df["Price per Mbps (Download)"] = round(df["Price"] / df["Download Speed"], 2)
df["Price per Mbps (Upload)"] = round(df["Price"] / df["Upload Speed"], 2)

print(df)
df.to_csv("comparison.csv", index=False)
