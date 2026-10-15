import pandas as pd
df = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "text"], encoding="latin-1")
df.head()
df["label"].value_counts(normalize=True)
df.duplicated().sum()