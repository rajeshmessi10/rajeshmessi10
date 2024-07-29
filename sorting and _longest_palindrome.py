def srt(lis):
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i] > lis[j]:
                lis[i] , lis[j] = lis[j] , lis[i]
    return lis
print(srt([5,2,8,7,1,1]))


str1 = "kadmadammalayalamgeeksskeeg"

str1 = "kadmadammaayalamsaippuakivikauppias"
# Initialize variables
longest_palindrome = ""

# Loop through each character in the string
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        # Get the substring
        substring = str1[i:j+1]
        print(substring)
        # Check if the substring is a palindrome and longer than the current longest
        if substring == substring[::-1] and len(substring) > len(longest_palindrome):
            longest_palindrome = substring

print(longest_palindrome)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(9, 3)

p3 = p1+p2

print(p3)
# Output: (3,5)