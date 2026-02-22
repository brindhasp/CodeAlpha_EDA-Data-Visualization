import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("quotes_data.csv")

print(df.head())
print(df.info())
print(df.describe(include="all"))

# Quotes per author
author_count = df["Author"].value_counts().head(10)

plt.figure()
author_count.plot(kind="bar")
plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quote length distribution
df["Quote_Length"] = df["Quote"].apply(len)

plt.figure()
sns.histplot(df["Quote_Length"], bins=20)
plt.title("Distribution of Quote Lengths")
plt.xlabel("Length of Quote")
plt.ylabel("Frequency")
plt.show()