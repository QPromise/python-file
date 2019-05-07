import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

print('兩個都大寫？', str1.isupper() and str2.isupper())
print('有一個大寫？', str1.isupper() or str2.isupper())
print('都不是大寫？', not (str1.isupper() or str2.isupper()))