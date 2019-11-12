import sys
sys.path.append('../../')
from challenge import Challenge

# Challenge(
# filename: str, 
# code: str, 
# challenge_input: str， <-- 默认不带input
# host_path=None, <-- 指定存放代码的路径，默认为当前路径
# timeout=None,  <-- 单例超时时间，默认为5s
# cpu=None, <-- CPU个数，默认为1核
# memory=None, <-- 内存限制， 默认30M
# memory_swap=None)) <-- 交换空间， 默认100M

helloWorld = Challenge(
    'helloworld.py', 
    '''print("hello world)''' # error code
    )

helloWorld.initBox()
result = helloWorld.box.run().strip()
print('result:')
print(result)
helloWorld.box.clear_file()