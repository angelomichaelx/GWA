#Michael Angelo P. Biag
#BSCPE 1-4
# Write a Python program that read a file containing the name of 20 students together with their GWA. The program will outputs the name of the student who got the highest GWA (including the GWA).

#before we start we need to add the list of students with grade
with open("studentlist.txt", "r") as file:
    for line in file:   

#Create two variables with empty and no initial values to which we will append the values after analyzing each line of the text.
        highest_gwa = None
        best_student = ""

#create two part, one is for student and the second one is for their grades
name, gwa = line.strip().split(" - ")
gwa = float(gwa)

#compute and pick the highest gwa in all 20 student
if highest_gwa is None or gwa < highest_gwa:
            highest_gwa = gwa
