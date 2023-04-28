#Michael Angelo P. Biag
#BSCPE 1-4
# Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#Create two variables with empty and no initial values to which we will append the values after analyzing each line of the text.
highest_gwa = None
best_student = ""

#before we start we need to add the list of students with grade
with open("studentlist.txt", "r") as A:
    for line in A:   

#create two part, one is for student and the second one is for their grades
        name, gwa = line.strip().split(" - ")
        gwa = float(gwa)

#compute and pick the highest gwa in all 20 student
        if highest_gwa is None or gwa < highest_gwa:
            highest_gwa = gwa

# the student who got the highest grade will be printed to the student who got the highest gwa
            best_student = name

#print with color/highlight design

print("\033[48;5;225m" + best_student + "\033[0m""\033[1;35mis the student with the highest GWA of\033[0m", "\033[48;5;225m" + str(highest_gwa), "\033[0m")