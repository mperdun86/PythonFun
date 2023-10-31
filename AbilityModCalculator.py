
score = input("Enter your ability score to get it's modifier: ")

intscore = int(score)

if intscore <= 0:
    print("Score too low!")

elif intscore >= 10:
    modifier = (intscore - 10) // 2
    print("For a score of", intscore, "the modifier is:", modifier)

elif intscore < 10:
    modifier = -((10 - intscore) // 2)
    print("For a score of", intscore, "the modifier is:", modifier)




