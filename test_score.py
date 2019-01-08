print("The Test Scores Program")
print()
print("Enter Test Scores")
print("'Exit' to Quit" )
banner = "====="
print(banner * 5)

test_score = 0
score_count = 0
total_score = 0

while test_score != "exit":
    test_score = input("Enter test score: ")

    if test_score.lower() == "exit":
        break

    test_score = int(test_score)
    score_count += 1
    total_score += test_score


print(banner * 5)
print(f"Number of Tests: {score_count}")
print(f"Total Score: {total_score}")
average_score = int(total_score / score_count)
print(f"Average Score: {average_score}")








