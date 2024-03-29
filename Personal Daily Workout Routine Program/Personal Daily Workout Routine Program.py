#  This is a python program that generates personalised daily workout routines based on user preferences and fitness goals
print("\n")
def seperator(): # Seperator defined to help section the different phases of the progamme output
    print("="*103)

seperator()
print("\n") # new life operator used to format the program.
print("""Hi there! I am Personal Program Trainer also known as PPT\n\nWelcome to your personal daily workout routine program. I help generate workouts based on your BMI. I 
will also help generate workouts based on your fitness goals, workout durations and your muscle target.""")
print("\n")
seperator()

# The exercise database contains a list of exercises for each muscle group and can developed further. The databse feeds into the suggested exercised produced based on user input
exercise_database = {
    'Chest':  ['Push-ups', 'Flat Bench Press', 'Chest Fly', 'Decline Bench Press', 'Incline Bench Press', 'Cable Crossover', 'Dumbbell Flyes'],
    'Legs':   ['Squats', 'Lunges', 'Deadlifts', 'Walking Lunges', 'Calf Raises', 'Leg Press', 'Goblet Squats'],
    'Biceps': ['Hammer Curl', 'Bicep Curl', 'Concentration Curl', 'Overhead Cable Curl', 'Barbell Curl', 'Reverse Barbell Curl'],
    'Triceps':['Lying Triceps Extension', 'Triceps Dips', 'Overhead Tricep Extension', 'Tricep Push Down', 'Weighted Bench Dip'],
    'Back':   ['Deadlifts', 'Romanian Deadlifts', 'Bent-over Rows', 'Pull-ups', 'Seated Cable Rows', 'One-arm Dumbbell Row', 'Y Raises', 'Shoulder Shrug'],
    'Abs':    ['Barbell Russian Twist', 'Swiss Ball Crunch', 'Flutter Kicks', 'Leg Raises', 'Sit Ups', 'Plank'],
    'Cardio': ['Jump Rope', 'Cycling', 'Box Jumps', 'Jumping Jacks', 'Burpees', 'Mountain Climbers', 'Rowing','Cycling','swimming','Burpees','Squat Jumps']
}
print("\n")
print("Lets get started with your BMI")
print("\n")
current_weight = float(input("Firstly, enter you current weight in (kg): "))
current_height = float(input("Now enter your current height in (meters): "))
BMI = current_weight / (current_height ** 2) 
whole_num_BMI = (BMI)

# .2f in the print statement ensures that the BMI, when displayed to the user, is shown with two decimal places for better readability and precision. 
print(f"Your BMI is: {BMI:.2f}")
print("\n")
if whole_num_BMI < 18.5:
    print("According to NHS BMI Healthy Weight Category, a BMI below 18.5 is classified as underweight.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("According to NHS BMI Healthy Weight Category, a BMI of 18.5 to 24.9 is classified as a healthy weight.")
elif BMI >= 25 and BMI <= 29.9:
    print("According to NHS BMI Healthy Weight Category, a BMI of 25 to 29.9 is classified as overweight.")
elif BMI >= 30:
    print("According to NHS BMI Healthy Weight Category, a BMI of 30 or more is classified as obese.")
else:
    print("Your input doesn't fall into the defined categories. Please double-check your values or consult a\nhealthcare professional for personalized advice.")

print("\n")
seperator()
print("\n")
fitness_goal = input("Enter your fitness goal: ")
workout_duration = int(input("Enter your preferred workout duration in minutes: "))
targeted_muscle_group = input("Enter the muscle group you want to target: ")
print("\n")
seperator()
print("\n")
import random #import random function is  used to random pull exercises from catergorised database and feed into print function when providing suggested exercises

def generate_workout(fitness_goal, workout_duration, targeted_muscle_group, BMI):
    if BMI < 18.5:  #For indivuals who fall into the Underweight category
        print(f"Based on your BMI of {BMI:.2f} and fitness goal to {fitness_goal}, here is your personalsied workout plan:")
        print("\n")
        print(f"Your workout duration is: {workout_duration} minutes")
        print(f"Your target muscle group is: {targeted_muscle_group.capitalize()}")
        print("Suggested workout routines for gaining strength and muscle building:")
        print("Carry out 3 sets per muscle exercise 8 - 12 reps")
        print("\n")
        seperator()
        print("\n")
        print(" Based on your BMI I also suggest some workouts below to help you gain healthy weight and muscle mass:")
        print("\n")
        print("Legs: ", random.sample(exercise_database['Legs'],k=2))
        print("Abs: ", random.sample(exercise_database['Abs'],k=2))
        print("Back: ", random.sample(exercise_database['Back'],k=2))
        print("Biceps: ",random.sample(exercise_database['Biceps'],k=2))
        print("Carry out 3 sets per muscle exercise 8 - 12 reps")
        

    elif BMI >= 18.5 and BMI <= 24.9:  #For individuals whp fall into the Healthy weight category
        print(f"Based on your BMI of {BMI:.2f} and fitness goal to {fitness_goal}, here is your personalsied workout plan:")
        print("\n")
        print(f"Your workout duration is: {workout_duration} minutes")
        print(f"Your target muscle group is: {targeted_muscle_group.capitalize()}")
        print("Carry out 3 sets per muscle exercise 8 - 12 reps")
        print("\n")
        seperator()
        print("\n")
        print("Based on your BMI I also suggest some workouts below to maintain your healthy weight and mass:")
        print("\n")
        print("Legs: ", random.sample(exercise_database['Legs'],k=2))
        print("Abs: ", random.sample(exercise_database['Abs'],k=2))
        print("Back: ", random.sample(exercise_database['Back'],k=2))
        print("Biceps: ", random.sample(exercise_database['Biceps'],k=2))
        print("Cardio: ", random.sample(exercise_database['Cardio'],k=2))
        print("Carry out 3 sets per muscle exercise 8 - 12 reps")


    elif BMI >= 25 and BMI <= 29.9:  #For individuals who fall into the Overweight category
        print(f"Based on your BMI of {BMI:.2f} and fitness goal to {fitness_goal}, here is your personalsied workout plan:")
        print("\n")
        print(f"Your workout duration is: {workout_duration} minutes")
        print(f"Your target muscle group is: {targeted_muscle_group.capitalize()}")
        print("Carry out 3 sets per muscle exercise 8 - 12 reps")
        print("\n")
        seperator()
        print("\n")
        print("Based on your BMI I also suggest some workouts below to lose weight and body mass:")
        print("Legs: ", random.sample(exercise_database['Legs'],k=2))
        print("Abs: ", random.sample(exercise_database['Abs'],k=2))
        print("Back: ", random.sample(exercise_database['Back'],k=2))
        print("Cardio: ", random.sample(exercise_database['Cardio'],k=2))
        print("Carry out 3 sets per muscle exercise 10 - 15 reps. Remember to use light weight. Your exercise should be focused on endurance!")

    elif BMI >= 30:  #For individuals who fall into the Obese category
        print(f"Based on your BMI of {BMI:.2f} and fitness goal to {fitness_goal}, here is your personalsied workout plan:")
        print("\n")
        print(f"Your workout duration is: {workout_duration} minutes")
        print(f"Your target muscle group is: {targeted_muscle_group.capitalize()}")
        print("Carry out 3 sets per muscle exercise 8 - 12 reps")
        print("\n")
        seperator()
        print("\n")
        print("Based on your BMI I also suggest some workouts below to lose weight and body mass:")
        print("\n")
        print("Cardio: ", random.sample(exercise_database['Cardio'],k=2))
        print("Back: ", random.sample(exercise_database['Back'],k=2))
        print("Legs: ", random.sample(exercise_database['Legs'],k=2))
        print("Abs: ", random.sample(exercise_database['Abs'],k=2))
        print("Carry out 3 sets per muscle exercise 10 - 15 reps. Remember to use light weight. Your exercise should be focused on endurance!")

    else:  # For any other value
        print("Your input doesn't fall into the defined categories.")


generate_workout(fitness_goal, workout_duration, targeted_muscle_group, BMI)

print("\n")
print("Keep track of you progress And remember consistency is key for results!")
print("\n")






