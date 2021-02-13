# Take input of you and your neighbor
my_first = input("What is your name?")
neigh_first = input("What is your name?")

# Take how long each of you have been coding
my_codetime = int(input(F"How long has {my_first} been coding?"))
neigh_codetime = int(input(f"How long has {neigh_first} been coding?"))

# Add total month
total_codetime = neigh_codetime + my_codetime

# Print results
print(f"{my_first} and {neigh_first} have been coding for {total_codetime} months")

