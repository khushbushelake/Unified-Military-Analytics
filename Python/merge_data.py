import pandas as pd

military = pd.read_csv("military_cleaned.csv")
country_info = pd.read_csv("country_info.csv")
continents = pd.read_csv("continents2.csv")
master_df = military.merge(
    country_info,
    on="country",
    how="left"
)
master_df = master_df.merge(
    continents,
    left_on="country",
    right_on="name",
    how="left"
)
master_df.to_csv("military_master.csv", index=False)
