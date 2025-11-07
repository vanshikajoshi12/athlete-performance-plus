import pandas as pd
# Exercise planner based on athlete data
def suggest_exercise(heart_rate,steps):
  if heart_rate > 80:
    return "Cardio light | Streatching"
  elif steps < 8000:
    return "Increase step count | Endurance building"
  else:
    return "Maintain routine | Core exercises"
    df = pd.read_csv(../data/athletes.csv")
    df["Exercise Plan"] = df.apply(lambda)row:
    suggest_exercise(row["HeartRate"], row["Steps"]), axis=1)
    print(df[["Name", "Exercise Plan"]])
