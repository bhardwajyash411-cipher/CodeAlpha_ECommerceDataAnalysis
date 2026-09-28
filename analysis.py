import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("products.csv")

print("\n===== DATASET =====")
print(df)

print("\n===== DATASET INFORMATION =====")
print(df.info())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Convert price into numeric value
df["Price"] = df["Price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
# Convert rating into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

print("\n===== AVERAGE PRICE =====")
print(df["Price"].mean())

print("\n===== AVERAGE RATING =====")
print(df["Rating"].mean())

# Highest priced books
print("\n===== TOP 5 EXPENSIVE PRODUCTS =====")
print(df.nlargest(5, "Price")[["Title", "Price"]])

# Rating distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Rating")
plt.title("Product Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.show()

# Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10)
plt.title("Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Products")
plt.show()

# Price vs Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Rating", y="Price")
plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price")
plt.show()