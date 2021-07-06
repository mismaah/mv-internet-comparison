"""Script to generate comparisons."""

import pandas

df = pandas.read_csv("packages.csv")
df = df.drop(df.columns[[6, 7]], axis=1)
df["Price per GB"] = (
    round(df["Price"] / df["Fair Usage (GB)"], 2) if df["Fair Usage (GB)"].any() else ""
)
df["Price per Mbps (Download)"] = round(df["Price"] / df["Download Speed (Mbps)"], 2)
df["Price per Mbps (Upload)"] = (
    round(df["Price"] / df["Upload Speed (Mbps)"], 2)
    if df["Upload Speed (Mbps)"].any()
    else ""
)
df = df.sort_values(by=["Price per GB"])
# df = df.sort_values(by=["Price per Mbps (Download)"])

print(df)
df.to_csv("comparison[sorted-price-per-GB].csv", index=False)
# df.to_csv("comparison[sorted-price-per-Mbps].csv", index=False)
