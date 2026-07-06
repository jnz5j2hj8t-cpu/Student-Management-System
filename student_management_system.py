names = ["Eri", "Momoko", "John"]
ielts_scores = [6.5, 7.0, 5.5]

def show_students(names, ielts_scores):
    print("===== Student List =====")
    print()
    for i in range(len(names)):

        score = ielts_scores[i]
        result = get_result(score)

        print(f"Student {i + 1}")
        print(f"Name : {names[i]}")
        print(f"IELTS : {ielts_scores[i]}")
        print(f"Result : {result}")
        print("---------------")

def add_student(names, ielts_scores):
    add_name = input("Enter student's name: ")
    add_score = float(input("Enter student's score: "))

    names.append(add_name)
    ielts_scores.append(add_score)

    print("Student added!")

def remove_student(names, ielts_scores):
    remove_name = input("Enter student's name: ")
    if remove_name in names:
        index = names.index(remove_name)
        del names[index]
        del ielts_scores[index]
        print("Student removed!")
    else:
        print("Student not found.")

def get_result(score):
    if score >= 7.0:
        result = "Excellent"
    elif score >= 6.0:
        result = "Good"
    elif score >= 5.5:
        result = "Average"
    else:
        result = "Need Improvement"
    return result
    
def search_student(names, ielts_scores):
    search_name = input("Enter student's name: ")
    if search_name in names:
        index = names.index(search_name)
        score = ielts_scores[index]
        result = get_result(score)

        print("===== Student Found =====")
        print()
        print(f"Name : {search_name}")
        print(f"IELTS : {score}")
        print(f"Result : {result}")
        print()
        print("---------------")

    else:
        print("Student not found.")

def show_average_score(ielts_scores):
    average_scores = sum(ielts_scores) / len(ielts_scores)
    rounded_average_scores = round(average_scores, 2)
    print(f"Average IELTS Score: {rounded_average_scores}")

def update_score(names, ielts_scores):
    name = input("Enter student's name: ")
    
    if name in names:
        new_score = float(input("Enter new IELTS score: "))
        index = names.index(name)
        ielts_scores[index] = new_score

        print("Score updated!")
    
    else:
        print("Student not found.")

def show_statistics(names, ielts_scores):
    print()
    print("===== Statistics =====")
    print()
    number_students = len(names)
    print(f"Number of students : {number_students}")
    print()
    show_average_score(ielts_scores)
    print()
    highest_score = max(ielts_scores)
    highest_index = ielts_scores.index(highest_score)
    print(f"Highest IELTS Score : {highest_score}")
    print(f"Student            : {names[highest_index]}")
    print()
    lowest_score = min(ielts_scores)
    lowest_index = ielts_scores.index(lowest_score)
    print(f"Lowest IELTS Score : {lowest_score}")
    print(f"Student            : {names[lowest_index]}")


choice = 0

while choice != 8:
    print()
    print("===== Student Management System =====")
    print()
    print("1. Show students")
    print("2. Add student")
    print("3. Remove student")
    print("4. Search student")
    print("5. Show average IELTS score")
    print("6. Update IELTS score")
    print("7. Show statistics")
    print("8. Exit")
    print()
    choice = int(input("Choose: "))

    if choice == 1:
        show_students(names, ielts_scores)

    elif choice == 2:
        add_student(names, ielts_scores)

    elif choice == 3:
        remove_student(names, ielts_scores)

    elif choice == 4:
        search_student(names, ielts_scores)

    elif choice == 5:
        show_average_score(ielts_scores)

    elif choice == 6:
        update_score(names, ielts_scores)

    elif choice == 7:
        show_statistics(names, ielts_scores)

    elif choice == 8:
        print("Goodbye!")

    else:
        print("Invalid choice.")