# Programmer: Lesdy Galvez
# Course: CS151, Dr. Rajeev
# Date: 10/27/2021
# Programming Assignment: 3
# Program Inputs: What type of sport;
# football:(completions,passing yards,touchdown passes, attempts, interceptions)
# Quidditch: (Goals,snitch)
# Program Inputs: Gymnast:(difficulty score, execution 1 score, execution 2 score...
# execution 3 score,execution 4 score, execution 5 score)

# Program Outputs: Figure out if or if not quarterback is a perfect passer and scores of all three sports

# Ask user what type of sport they want
def menu():
    menu_choice=input("enter sport type:")
    return menu_choice.lower()

#check if user input is a integer value
def int_check(value):
    while not value.isdigit():
        print("Error,Not an integer")
        value=input("enter an integer")
    value=int(value)
    return value

# function for choice:Football
def football():
    completion=input("enter number of completions:")
    int_check(completion)
    completion=int_check(completion)
    passing_yards=input("enter number of passing_yards:")
    int_check(passing_yards)
    passing_yards=int_check(passing_yards)
    attempts=input("enter number of attempts:")
    int_check(attempts)
    attempts=int_check(attempts)
    interceptions=input("enter number of interceptions:")
    int_check(interceptions)
    interceptions=int_check(interceptions)
    touchdown_passes=input("enter number of touchdown_passes:")
    int_check(touchdown_passes)
    touchdown_passes=int_check(touchdown_passes)
    football_score = 100*((5 * (completion/attempts-0.3))+(0.25*(passing_yards/attempts-3))+(20*(touchdown_passes/attempts))+2.375-(25 * interceptions/attempts))/6
    return football_score
# function for choice: Quidditch
def quidditch():
    goals=input("enter number of goals:")
    int_check(goals)
    goals=int_check(goals)
    quidditch_score= 10*(goals)
    snitch=input("did you catch the snitch? Yes or no?:")
    if snitch=="yes":
        quidditch_score+=30
    elif snitch=="no":
        quidditch_score+=0
    else:
        print("Invalid answer")
        snitch=input("did you catch the snitch?Yes or no?")
    return quidditch_score

# function for choice: Gymnast
def gymnast():
    difficulty=float(input("enter difficulty score:"))
    execution_1=float(input("enter execution_1 score:"))
    execution_2=float(input("enter execution_2 score:"))
    execution_3=float(input("enter execution_3 score:"))
    execution_4=float(input("enter execution_4 score:"))
    execution_5=float(input("enter execution_5 score:"))
    calculate_minimum=min(execution_1,execution_2,execution_3,execution_4,execution_5)
    calculate_maximum=max(execution_1,execution_2,execution_3,execution_4,execution_5)
    avg_executions=((execution_1+execution_2+execution_3+execution_4+execution_5)-(calculate_minimum+calculate_maximum))/3
    Gymnast_score=(difficulty+avg_executions)
    return Gymnast_score

# main function
def main():
    print("The program will calculate the sport scores for user depending on user's choice of sport")
    menu_choice=menu()
    if menu_choice.lower()=="football":
        football_qb=football()
        print("your football quarterback rating is:",football_qb)
        if football_qb>=158.3:
            print("you are a perfect passer")
        else:
            print("sorry, you are not a perfect passer")
    elif menu_choice.lower()=="quidditch":
        quidditch_s=quidditch()
        print("your quidditch score is",quidditch_s)
    elif menu_choice.lower()=="gymnast":
        gymnast_s=gymnast()
        print("your final gymnast score is:",gymnast_s)

    print("Thank you for using my program")

main()







