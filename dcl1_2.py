SEB = []
Badminton = []
Cricket = []
Football = []

def remove_dup(d):
    return list(set(d))

def input_students(activity_list, activity_name, inputs):
    n = int(inputs.pop(0))  # Simulated input for number of students
    for i in range(1, n + 1):
        s = inputs.pop(0)  # Simulated input for student names
        activity_list.append(s)
    print(f"Students playing {activity_name}: {activity_list}")
    return remove_dup(activity_list)

def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def subtract(lst1, lst2):
    return list(set(lst1) - set(lst2))

def symmetric_difference(lst1, lst2):
    return list(set(lst1) ^ set(lst2))

# Simulated inputs for testing
inputs = ["3", "Alice", "Bob", "Charlie", "2", "Bob", "Diana", "3", "Charlie", "Eve", "Frank"]

Badminton = input_students(Badminton, "Badminton", inputs)
Cricket = input_students(Cricket, "Cricket", inputs)
Football = input_students(Football, "Football", inputs)

flag = True
while flag:
    print("\n****** MENU ******")
    print("1. List of students who play both Cricket and Badminton")
    print("2. List of students who play either Cricket or Badminton but not both")
    print("3. List of students who play neither Cricket nor Badminton")
    print("4. List of students who play Cricket and Football but not Badminton")
    print("5. Exit")
    
    if inputs:
        choice = int(inputs.pop(0))  # Simulated input for menu choice
    else:
        break

    if choice == 1:
        print("Students who play both Cricket and Badminton:", intersection(Badminton, Cricket))
    elif choice == 2:
        print("Students who play either Cricket or Badminton but not both:", symmetric_difference(Badminton, Cricket))
    elif choice == 3:
        print("Students who play neither Cricket nor Badminton:", subtract(SEB, union(Badminton, Cricket)))
    elif choice == 4:
        print("Students who play Cricket and Football but not Badminton:", subtract(intersection(Cricket, Football), Badminton))
    elif choice == 5:
        flag = False
        print("Thank you for using the program!")
    else:
        print("Wrong choice! Try again.")