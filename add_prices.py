import pandas as pd
import random

df = pd.read_csv('supplement_info.csv')

# Generate random prices between 250 and 1200
prices = [random.randint(250, 1200) for _ in range(len(df))]

# Add price column
df['price'] = prices

# Save to CSV
df.to_csv('supplement_info.csv', index=False)

print("Prices added successfully!")
print(df[['supplement name', 'price']].head(10))
