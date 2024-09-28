import pandas as pd


df = pd.read_parquet(r"C:\Users\Logeshwaran\Downloads\emotion_detection\Resources\test-00000-of-00001.parquet")


df.to_csv(r"C:\Users\Logeshwaran\Downloads\emotion_detection\Resources\test_dataset(onlylabels).csv", index=False)

print("Parquet file successfully converted to CSV!")

import pandas as pd


# df = pd.read_csv(r"C:\Users\Logeshwaran\Downloads\converted_test_dataset.csv")


# df.to_parquet(r"C:\Users\Logeshwaran\Downloads\converted_test_dataset.parquet", index=False)

# print("CSV file successfully converted to Parquet!")

