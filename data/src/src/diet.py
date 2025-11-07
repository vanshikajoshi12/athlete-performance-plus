import pandas as pd
# Simple diet planner for athletes based on stamina level
def suggest_diet(stamina):
  if stamina >= 8:
    return "High protein | Hydration | Balanced carbs"
  elif stamina >= 8:
    return "Regular protein | Fruits | Veggies"
  else:
    return "Protein boost | Vitamin supplements"
    df = pd.read_csv("../data/athletes.csv")
    df["Diet Plan"] = df["Stamina"].apply(suggest_diet)
    print(df[["Name", "Diet Plan"]])
