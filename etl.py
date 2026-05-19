import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'salary': [2500, 3000, 3500],
}

df = pd.DataFrame(data)
df['salary_after_bonus'] = df['salary'] * 1.1

df.to_csv('output.csv', index=False)

print("ETL process completed successfully.")
