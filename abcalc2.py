score = input("Enter your ability score to get its modifier: ")

intscore = int(score)

if intscore <= 0:
    print("Score too low!")
else:
    modifier = (intscore - 10) // 2
    print("For a score of", intscore, "the modifier is:", modifier)