"""Script to generate comparisons."""

import pandas

df = pandas.read_csv("plans.csv")
df = df.drop(df.columns[[6, 7]], axis=1)
df["Price per GB"] = (
    round(df["Price"] / df["Fair Usage (GB)"], 2) if df["Fair Usage (GB)"].any() else ""
)
df = df.sort_values(by=["Price per GB"])
df["Price per Mbps (Download)"] = round(df["Price"] / df["Download Speed (Mbps)"], 2)
df["Price per Mbps (Upload)"] = (
    round(df["Price"] / df["Upload Speed (Mbps)"], 2)
    if df["Upload Speed (Mbps)"].any()
    else ""
)

print(df)
df.to_csv("comparison.csv", index=False)
