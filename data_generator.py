import pandas as pd
import numpy as np

def generate_data():
    # Generate 6 months of hourly data
    rng = pd.date_range(start="2025-01-01", periods=24*180, freq="h")
    dorms = ["Dorm_A", "Dorm_B", "Dorm_C"]
    rows = []

    for dorm in dorms:
        usage = np.random.normal(50, 10, len(rng))

        # Add random peak spikes
        peak_indices = np.random.choice(len(rng), size=30, replace=False)
        usage[peak_indices] += np.random.randint(40, 100, size=len(peak_indices))

        rows.append(pd.DataFrame({
            "timestamp": rng,
            "dorm": dorm,
            "usage": usage
        }))

    df = pd.concat(rows)
    df.to_csv("electricity_data.csv", index=False)
    print("Data generated successfully!")

if __name__ == "__main__":
    generate_data()
