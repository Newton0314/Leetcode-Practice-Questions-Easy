def palindrome(x):
    x = str(x)
    if x[::-1] == x:
        return True
    else:
        return False

print(palindrome(-121))

#follow-up question remains unsorted (solving the question without converting to strings)
