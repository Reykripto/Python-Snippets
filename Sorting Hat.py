# Sorting Hat 
# initialize each House's point to zero
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Question
print(f"Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n")
answer_1 = int(input("Input your option: "))

if answer_1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer_1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")
    exit()

# Question 2
print(f"When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n")
answer_2 = int(input("Input your option: "))

if answer_2 == 1:
    hufflepuff += 2
elif answer_2 == 2:
    slytherin += 2
elif answer_2 == 3:
    ravenclaw += 2
elif answer_2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")
    exit()

# Question 3
print(f"Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n")
answer_3 = int(input("Input your option: "))

if answer_3 == 1:
    slytherin += 4
elif answer_3 == 2:
    hufflepuff += 4
elif answer_3 == 3:
    ravenclaw += 4
elif answer_3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")
    exit()

# Determine which house has the most points
max_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if max_points == gryffindor:
    print("Congratulations! You are in Gryffindor!")
elif max_points == ravenclaw:
    print("Congratulations! You are in Ravenclaw!")
elif max_points == hufflepuff:
    print("Congratulations! You are in Hufflepuff!")
elif max_points == slytherin:
    print("Congratulations! You are in Slytherin!")
else:
    print("Error: No House with the most points!")