# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what the grade is for a particular score. Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

for x in range(0,3):
    print "Enter your score"
    score = input()
    if (score>59 and score<=100) :
        if score>60 and score<70:
            print "Score:",score,"Your Grade is D"
        elif score>=70 and score<80:
            print "Score:",score,"Your Grade is C"
        elif score>=80 and score<90:
            print "Score:",score,"Your Grade is B"
        elif score>=90 and score<=100:
            print "Score:",score,"Your Grade is A"

    else:
        print "Enter scores between 60 to 100"
raw_input("\n\n End of the program.Bye!")
