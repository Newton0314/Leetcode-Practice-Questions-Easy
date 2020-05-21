# Longest common prefix
def LCP(x):
    longest_common_prefix = ''
    # s stands for the shortest string
    s = min(x)
    for possible_common_prefix in range(1, len(s) + 1):
        n = 0
        for allElements in x:
            if (s[:possible_common_prefix] in allElements) and (s[0] == allElements[0]):
                n += 1
                continue
        else:
            if n == len(x) and (len(s[:possible_common_prefix]) >= len(longest_common_prefix)):
                longest_common_prefix = s[:possible_common_prefix]

    print(longest_common_prefix)


print(LCP(['flower', 'flight', 'flow']))




