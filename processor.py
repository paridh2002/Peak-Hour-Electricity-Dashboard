import pandas as pd
from sklearn.linear_model import LinearRegression

def load_and_process():
    df = pd.read_csv("electricity_data.csv", parse_dates=["timestamp"])

    # Smooth data using moving average
    df["smoothed"] = df.groupby("dorm")["usage"].transform(
        lambda x: x.rolling(window=3, center=True).mean()
    )

    df.dropna(inplace=True)
    return df

def train_model(df):
    df["hour"] = df["timestamp"].dt.hour

    X = df[["hour"]]
    y = df["smoothed"]

    model = LinearRegression()
    model.fit(X, y)

    return model
