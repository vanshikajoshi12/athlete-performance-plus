#Simple athlete to-do list generator
athlete_todos = {
  "A1": ["Morning run", "Healthy breakfast", "Accuracy drills"],
  "A2": ["Hydration", "Speed sprints", "Check stats"],
  "A3": ["Stretching", "Speed training", "Balanced meal"],
  "A4": ["Endurance workout", "Fruit snack", "Team activity"],
  "A5": ["Steps goal", "Core exercise", "Review data"]
}
for athlete, todos in
athlete_todos.items():
  print(f"{athletes}'s to-do list: {', '.join(todos)}")
