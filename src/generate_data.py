import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "temperature": np.random.randint(50, 100, 200),
    "vibration": np.random.uniform(1, 10, 200),
    "current": np.random.uniform(8, 20, 200)
}

df = pd.DataFrame(data)

# Rule-based failure label
df["failure"] = (
    (df["temperature"] > 80) |
    (df["vibration"] > 7)
).astype(int)

df.to_csv("data/iot_sensor_data.csv", index=False)

print("Dataset created successfully!")