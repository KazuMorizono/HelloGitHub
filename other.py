from traceback import print_tb
from unittest import result


# print("こんにちは, GitHub！！")

def test(name):
  return "Hello, " + name

result = test('Tom')
print(result)