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
    '''print("hello world")'''
    )

helloWorld.initBox()
result, _ = helloWorld.box.run()
print('stdout:')
print(result["stdout"])
print("stderr:")
print(result["stderr"])
print(helloWorld.box.clear_file())