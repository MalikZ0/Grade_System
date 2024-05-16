# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name : P.G.M.D.Kumara 
# Date: 04.21.2023

# PART 4
# Function for get credits in pass,defer and fail
# And loop until input credits are in range 
# And no ValueError input

def get_credits(credit_type):
    while True:
        try:
            credit = int(input(f"Please enter your credits at {credit_type}: "))
            if credit not in range(0, 121, 20):
                print("Out of range.")
                print()
                continue
            return credit
        except ValueError:
            print("Integer required")
            print()

# A function for calculate outcomes and credits

def calculate_outcome(pass_credits, defer_credits, fail_credits):
    if (pass_credits + defer_credits + fail_credits) != 120:
        return "Total incorrect."
    elif pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif (pass_credits == 80) or (pass_credits == 60) or (pass_credits == 40 and defer_credits >= 20) or \
            (pass_credits == 20 and defer_credits >= 40) or (pass_credits == 0 and defer_credits >= 60):
        return "Module retriever"
    else:
        return "Exclude"

# Function for student id

def student_id():
    while True:
        id_num = (input("Enter your UOW number starting with w :"))
        if len(id_num) != 8:
            print("Required '7' numbers starting with 'w' letter")
            continue
        else:
            return id_num


# Check Validation

count_of_progress = 0
count_of_trailer = 0
count_of_retriever = 0
count_of_exclude = 0
progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []
outcome_dictionary = {}
while True:
    Id_num = student_id()
    Pass_credits = get_credits("PASS")
    Defer_credits = get_credits("DEFER")
    Fail_credits = get_credits("FAIL")
    result = calculate_outcome(Pass_credits, Defer_credits, Fail_credits)
    print(result)
    if result != "Total incorrect.":
        if result == "Progress":
            count_of_progress += 1
            progress_list.append([Pass_credits, Defer_credits, Fail_credits])
            outcome_dictionary[Id_num] = f"Progress - {Pass_credits}, {Defer_credits}, {Fail_credits}"
        elif result == "Progress (module trailer)":
            count_of_trailer += 1
            trailer_list.append([Pass_credits, Defer_credits, Fail_credits])
            outcome_dictionary[Id_num] = f"Progress (module trailer) - {Pass_credits}, {Defer_credits}, {Fail_credits}"
        elif result == "Module retriever":
            count_of_retriever += 1
            retriever_list.append([Pass_credits, Defer_credits, Fail_credits])
            outcome_dictionary[Id_num] = f"Module retriever - {Pass_credits}, {Defer_credits}, {Fail_credits}"
        elif result == "Exclude":
            count_of_exclude += 1
            exclude_list.append([Pass_credits, Defer_credits, Fail_credits])
            outcome_dictionary[Id_num] = f"Exclude - {Pass_credits}, {Defer_credits}, {Fail_credits}"
        # Check multiple outcomes
        while True:
            multiple_outcomes = input(
                "Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: ").lower()
            print()
            if multiple_outcomes in ["y", "q"]:
                break
            else:
                print("Wrong input!")
                print("You should enter 'y' or 'q'")
                continue
        if multiple_outcomes == "y":
            continue
        if multiple_outcomes == "q":
            break
    # else:
    #     continue

# Histogram
print("-------------------------------------------------------------------------------------------------------------------------------")
print("Histogram")
print(f"Progress {count_of_progress}", ":", "*" * count_of_progress)
print(f"Trailer  {count_of_trailer}", ":", "*" * count_of_trailer)
print(f"Retriever {count_of_retriever}", ":", "*" * count_of_retriever)
print(f"Excluded {count_of_exclude}", ":", "*" * count_of_exclude)
print(count_of_progress + count_of_trailer + count_of_retriever + count_of_exclude, "outcomes in total.")
print()
print("-------------------------------------------------------------------------------------------------------------------------------")
print("part 2")
# Creating lists
for i in progress_list:
    print(f"progress", "-", str(i).strip("[]"))
for i in trailer_list:
    print(f"Progress (module trailer)", "-", str(i).strip("[]"))
for i in retriever_list:
    print(f"Module retriever", "-", str(i).strip("[]"))
for i in exclude_list:
    print(f"Exclude", "-", str(i).strip("[]"))
print()
print("-------------------------------------------------------------------------------------------------------------------------------")
f = open("students_credits.txt", "w")
f.write("Part 3:\n")
# File handling
for i in progress_list:
    f.write(f"Progress - {i[0]}, {i[1]}, {i[2]}\n")
for i in trailer_list:
    f.write(f"Progress (module trailer) - {i[0]}, {i[1]}, {i[2]}\n")
for i in retriever_list:
    f.write(f"Module retriever - {i[0]}, {i[1]}, {i[2]}\n")
for i in exclude_list:
    f.write(f"Exclude - {i[0]}, {i[1]}, {i[2]}\n")
f.close()
f = open("students_credits.txt", "r")
print(f.read())
f.close()
print("-------------------------------------------------------------------------------------------------------------------------------")
print("Part 4")
# Creating dictionary
for Id_num, outcomes in outcome_dictionary.items():
    print(f"{Id_num} : {outcomes}", end="  ")
print()
print("-------------------------------------------------------------------------------------------------------------------------------")
