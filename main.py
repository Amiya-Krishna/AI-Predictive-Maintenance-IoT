import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report

# 1. SIMULATE DATA (In industry, this comes from sensors)
def generate_iot_data(n_engines=10):
    data = []
    for engine_id in range(1, n_engines + 1):
        # Every engine runs for a random number of cycles before failing
        max_cycles = np.random.randint(100, 200)
        for cycle in range(1, max_cycles + 1):
            # Sensors show "noise" + "increasing trend" (degradation)
            temp = 200 + (cycle * 0.5) + np.random.normal(0, 5)
            pressure = 150 + (cycle * 0.2) + np.random.normal(0, 2)
            vibration = 1 + (cycle * 0.01) + np.random.normal(0, 0.1)
            
            # Label: If within 20 cycles of failure, Label = 1 (Risk)
            label = 1 if (max_cycles - cycle) < 20 else 0
            data.append([engine_id, cycle, temp, pressure, vibration, label])
            
    return pd.DataFrame(data, columns=['engine_id', 'cycle', 'temp', 'pressure', 'vibration', 'label'])

# 2. IMPLEMENTATION
print("--- Initializing IoT Predictive Maintenance Pipeline ---")
df = generate_iot_data(50)

# Feature Engineering: Adding Rolling Average
df['temp_rolling'] = df.groupby('engine_id')['temp'].transform(lambda x: x.rolling(5).mean())
df = df.dropna()

# Split Data
X = df[['cycle', 'temp', 'pressure', 'vibration', 'temp_rolling']]
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("\n--- Model Performance ---")
print(classification_report(y_test, y_pred))

# 3. VISUALIZATION (Crucial for Proof of Work)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df[df['engine_id']==1], x='cycle', y='temp', label='Temperature')
plt.axvline(x=df[df['engine_id']==1]['cycle'].max() - 20, color='red', linestyle='--', label='Failure Warning Zone')
plt.title("Sensor Degradation Profile (Engine #1)")
plt.xlabel("Operating Cycles")
plt.ylabel("Sensor Reading")
plt.legend()
plt.savefig('outputs/failure_prediction_graph.png')
print("\nGraph saved to outputs/failure_prediction_graph.png")