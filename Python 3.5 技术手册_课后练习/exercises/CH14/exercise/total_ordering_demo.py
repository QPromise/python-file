from exercise1 import total_ordering

@total_ordering
class Some:
     def __init__(self, x):
         self.x = x
     def __eq__(self, other):
         return self.x == other.x
     def __gt__(self, other):
         return self.x > other.x

s1 = Some(10)
s2 = Some(20)
print(s1 >= s2)
print(s1 <= s2)

