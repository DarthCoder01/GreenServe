import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# ==========================================
# YOUR WATTTIME CREDENTIALS
# ==========================================

USERNAME = "Ashith_Rao_K"
PASSWORD = "ccbd@123"

# ==========================================
# LOGIN
# ==========================================

print("Logging into WattTime...")

login_response = requests.get(
    "https://api.watttime.org/login",
    auth=HTTPBasicAuth(USERNAME, PASSWORD)
)

if login_response.status_code != 200:
    print("Login failed!")
    print(login_response.text)
    exit()

TOKEN = login_response.json()["token"]

print("Login successful!")
print()

# ==========================================
# GET FORECAST
# ==========================================

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

params = {
    "region": "CAISO_NORTH",
    "signal_type": "co2_moer"
}

forecast_response = requests.get(
    "https://api.watttime.org/v3/forecast",
    headers=headers,
    params=params
)

if forecast_response.status_code != 200:
    print("Forecast request failed!")
    print(forecast_response.text)
    exit()

data = forecast_response.json()

forecast = data["data"]

# ==========================================
# CLEAN DATA
# ==========================================

times = []
values = []

for point in forecast:

    value = point["value"]

    # Ignore weird 0 values
    if value <= 0:
        continue

    times.append(point["point_time"])
    values.append(value)

df = pd.DataFrame({
    "time": times,
    "carbon": values
})

# ==========================================
# SUMMARY
# ==========================================

print("========== FORECAST SUMMARY ==========")
print()

print(f"Region: {data['meta']['region']}")
print(f"Signal: {data['meta']['signal_type']}")
print(f"Units : {data['meta']['units']}")

print()

print(f"Lowest Carbon Value : {df['carbon'].min():.2f}")
print(f"Highest Carbon Value: {df['carbon'].max():.2f}")
print(f"Average Carbon Value: {df['carbon'].mean():.2f}")

print()

# ==========================================
# CURRENT STATUS
# ==========================================

current_value = df["carbon"].iloc[0]
average_value = df["carbon"].mean()

print("========== SCHEDULER DECISION ==========")
print()

print(f"Current Carbon Intensity: {current_value:.2f}")

if current_value > average_value:

    print("DIRTY ENERGY PERIOD")
    print("Recommendation:")
    print("Delay low-priority inference jobs")
    print("Serve only latency-sensitive requests")

else:

    print("GREEN ENERGY PERIOD")
    print("Recommendation:")
    print("Run queued batch requests")
    print("Increase batch size for better efficiency")

print()

# ==========================================
# BEST TIME TO RUN
# ==========================================

best_row = df.loc[df["carbon"].idxmin()]

print("========== BEST EXECUTION WINDOW ==========")
print()

print("Cleanest forecast point:")

print(f"Time   : {best_row['time']}")
print(f"Carbon : {best_row['carbon']:.2f}")

print()

# ==========================================
# SAVE CSV
# ==========================================

df.to_csv("carbon_forecast.csv", index=False)

print("Saved forecast to carbon_forecast.csv")

# ==========================================
# GRAPH
# ==========================================

# Convert to datetime
df["time"] = pd.to_datetime(df["time"], utc=True)

# Convert UTC -> IST
df["time"] = df["time"].dt.tz_convert("Asia/Kolkata")

# ==========================
# PLOT
# ==========================

plt.figure(figsize=(14, 6))

plt.plot(
    df["time"],
    df["carbon"],
    linewidth=2
)

plt.title(
    "Carbon Intensity Forecast - CAISO North",
    fontsize=16,
    pad=15
)

plt.xlabel(
    "Date & Time (IST)",
    fontsize=12
)

plt.ylabel(
    "Carbon Intensity (lbs CO₂/MWh)",
    fontsize=12
)

ax = plt.gca()

# Show tick every 2 hours
ax.xaxis.set_major_locator(
    mdates.HourLocator(interval=2)
)

# Presentation-friendly format
ax.xaxis.set_major_formatter(
    mdates.DateFormatter(
        "%d %b\n%I:%M %p",
        tz=df["time"].dt.tz
    )
)

plt.xticks(rotation=0)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.show()
