import os
import pandas as pd

if __name__ == "__main__":
    path = os.path.join(os.getcwd(), 'results')
    results = []
    for root, dirs, files in os.walk(path):
        for f in files:
            df = pd.read_csv(os.path.join(root, f), index_col=0)
            results.append(df)
    df = pd.concat(results, ignore_index=True)
    df.to_csv(os.path.join(path, 'combined.csv'), index=False)