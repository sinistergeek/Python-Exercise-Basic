url = 'https://raw.githubusercontent.com/kennethleungty/Simulated-Annealing-Feature-Selection/main/data/raw/train.csv'

# Parse URL into pandas function
df = pd.read_csv(url)

# Display first 5 rows
print(df.head())
