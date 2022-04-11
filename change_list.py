todos = [
  "get groceries",
  "get haircut",
  "cook dinner",
  "feed cat"
]

todos.append("wash car")

todos.insert(1, "mop the floor")
todos[0] = "return groceries"
del todos[1]
print(todos)