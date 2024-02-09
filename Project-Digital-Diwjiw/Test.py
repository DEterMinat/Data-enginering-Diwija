
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("online_sales.csv")


print(df.head())
df.info()


df.dropna(inplace=True)  
df["Date"] = pd.to_datetime(df["Date"])  



df_sales = df.groupby(["Product", "ProductCategory", "Region"])["Price"].sum()


top_products = df_sales.nlargest(10)
bottom_products = df_sales.nsmallest(10)


df_monthly_sales = df.groupby(["Date", "ProductCategory"])["Price"].sum().unstack()
df_monthly_sales.plot(kind="line", figsize=(10, 6))
plt.title("Monthly Sales by Product Category")
plt.show()



sns.barplot(x=df_sales.index.get_level_values("ProductCategory"), y=df_sales.values)
plt.title("Sales by Product Category")
plt.show()


sns.heatmap(df_monthly_sales.corr(), annot=True)
plt.title("Monthly Sales Correlation")
plt.show()

