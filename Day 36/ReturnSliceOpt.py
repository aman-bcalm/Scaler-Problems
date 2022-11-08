import pandas as pd

def solve(dt, rid, ph, ch, ma):

    df =    pd.DataFrame({
            "dates": dt,
            "ids": rid,
            "PHY": ph,
            "Chem": ch,
            "Math": ma
        })

    df_slice = df[df["dates"] >= "2014-05-01"]
    df_slice["avg"] = (df_slice["PHY"] + df_slice["Chem"] + df_slice["Math"]) / 3
    df_slice = df_slice.sort_values(by="avg")
    return " ".join([str(x) for x in df_slice["ids"].tolist()])