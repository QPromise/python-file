import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

print('"{0}" > "{1}"? {2}'.format(str1, str2, str1 > str2))
print('"{0}" == "{1}"? {2}'.format(str1, str2, str1 == str2))
print('"{0}" < "{1}"? {2}'.format(str1, str2, str1 < str2))