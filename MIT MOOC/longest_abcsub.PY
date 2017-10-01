s = "sometext"
substr, longest = s[0], s[0]

for i in range(len(s) - 1):
    
    if s[i] <= s[i + 1]:
        substr += s[i + 1]
        if len(substr) > len(longest):
            longest = substr
    else:
        substr = s[i + 1]
        
print("Longest substring in alphabetical order is:",longest)