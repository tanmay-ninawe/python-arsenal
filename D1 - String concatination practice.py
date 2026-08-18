

# Q3. A says Hi to B
# Unsolved
# feature icon
# Get your doubts resolved blazing fast with Chat GPT Help
# Check Chat GPT
# feature icon
# Using hints except Complete Solution is Penalty free now
# Use Hint
# Problem Description
# Take two names A and B as input from the user, print "A says Hi to B" (Without quotations), where A and B are the names in input.

# Problem Constraints

# 1 <= len(A), len(B) <= 15
# Characters in A and B are in lowercase English Alphabets.


# Input Format

# There are two input lines
# The first line has a string A.
# The second line has a string B.


# Output Format

# Print in a single line A says Hi to B.


# Example Input

# Input:-
# Ram
# Shyam


# Example Output

# Output:-
# Ram says Hi to Shyam


#========================================

def main():
    firstName = str(input("Enter your first name: "))
    secondName = str(input("Enter your second name: "))
    print(firstName + " says Hi to " + secondName)

if __name__ == "__main__":
    main()