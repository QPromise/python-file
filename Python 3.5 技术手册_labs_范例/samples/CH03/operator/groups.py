import sys

admins = {'Justin', 'caterpillar'}
users = set(sys.argv[1:])
print('站長：{}'.format(admins & users))
print('非站長：{}'.format(users - admins))
print('全部使用者：{}'.format(admins | users))
print('身份不重複使用者：{}'.format(admins ^ users))
print('站長群包括使用者群？{}'.format(admins > users))
print('使用者群包括站長群？{}'.format(admins < users))

