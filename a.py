def myzip(*args):
  iters = map(iter, args)
  while iters:
    res = [next(i) for i in iters]
    yield tuple(res)
print(list(myzip('12', '34')))

# 注意这段代码在python2和python3中不同的执行结果
# 在python2中这段代码输出［（‘1’， ‘3’）， （‘2’， ‘4’）］，其实bool（iters）一直为真，直到next（i）抛出了StopIteration
# 结束了while循环

# 在python3中 iters是一个单次可迭代对象，而不是python2中的列表
# 也就是说for i in iters只能执行一次，最终的结果是（‘1’， ‘3’）， 然后是空元祖无限循环；
