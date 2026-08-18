
# 4. Total Bills Value
# Unsolved
# feature icon
# Get your doubts resolved blazing fast with Chat GPT Help
# Check Chat GPT
# feature icon
# Using hints except Complete Solution is Penalty free now
# Use Hint
# Problem Description

# Given the value of a single bill and the number of bills you received, print the total value of the bills.

# Note: The value of all the bills are same


# Problem Constraints

# 1 <= N <= 100
# 1 <= M <= 100


# Input Format

# The first line of the input is an integer N denoting the value of a single bill.
# The second line of the input is an integer M denoting the number of bills.


# Output Format

# Print in a single line denoting the total value of bills.


# Example Input

# Input:-
# 12
# 10


# Example Output

# Output:-
# 120


# Example Explanation

# Note: The problem constraints mean that when we test your code, the test cases used in the backend can have input values only within those constraints. You need not implement them in your code. You need to make sure your code will work for all such input values!



# #----------------------------------------


def main() :
    valueOfaSingleBill = int(input("Enter the vlaue of a single bill: "))
    numberOfBills = int(input("Enter the number of bills: "))
    print("Total value of bills : ", valueOfaSingleBill * numberOfBills)

if __name__ == "__main__":
    main()