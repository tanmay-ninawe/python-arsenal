# Q5. Calculate Currency Change
# Unsolved
# feature icon
# Get your doubts resolved blazing fast with Chat GPT Help
# Check Chat GPT
# feature icon
# Using hints except Complete Solution is Penalty free now
# Use Hint
# Problem Description

# Your friend Rahul plans to visit exotic countries all around the world. Sadly, Rahul's math skills aren't good enough. Take the amount of money Rahul has before the currency exchange and the amount of money that is spent from his savings as input, print the amount of money that remains in his savings.

# Input Format

# The first line contains an integer N denoting the total savings, the amount of money before exchange.
# The second line contains an integer M denoting the exchanging amount, denoting the amount of money that is spent from the savings.
# Output Format

# Print a single line denoting the amount of money that is left in his savings.
# Problem Constraints

# 1 <= N <= 1000
# 1 <= M <= N
# Example Input

# Input:-
# 116
# 12
# Example Output

# Output:-
# 104
# Note: The problem constraints mean that when we test your code, the test cases used in the backend can have input values only within those constraints. You need not implement them in your code. You must ensure your code will work for all such input values!


# ===============================


def main():
    theValueofMoneybeforeExchange = int(input("Enter the total savings: "))
    theValueofMoneySpent = int(input("Enter the amount spent: "))
    print("Amount left in savings: ", theValueofMoneybeforeExchange - theValueofMoneySpent)

if __name__ == "__main__":
    main()