# Using zip for Parallel Iteration:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
study=['bcs','cse','eee']

for name, age,s in zip(names, ages,study):
    print(name, age,s)
