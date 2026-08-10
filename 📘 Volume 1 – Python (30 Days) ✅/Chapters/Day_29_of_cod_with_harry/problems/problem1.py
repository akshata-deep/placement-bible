# 1. Positive or Negative

# Take a number from the user and store "Positive" if the number is greater than or equal to 0, otherwise store "Negative".


marks = int(input("Enter the marks: "))
result = "Excellent" if marks<=100 and marks>=90 else "Very good" if marks>=75 and marks<=89 else "Good" if marks>=50 and marks<=74 else "Need Improvement" if marks<50 and marks>0 else "invalid marks"
print(result)