# 1. 导包
import numpy as np

# 2. 创建Numpy的核心对象 -> ndarray(n维数组)
arr = np.arange(15).reshape(3, 5)   # 3行5列
# 3. 打印数组
print(arr)

# 4.演示Numpy的常用属性
print(f'数组的维度(轴): {arr.ndim}')      # 几维数组 -> 轴就是几
print(f'数组的形状: {arr.shape}')         # 几行几列 -> (行数, 列数)
print(f'数组的元素类型: {arr.dtype}')      # 整型
print(f'数组中每个元素占的字节数: {arr.itemsize}')  # int32 -> 4个字节, int64 -> 8个字节
print(f'数组中元素的个数: {arr.size}')     # 长度

print(f'数组的类型: {type(arr)}')         # <class 'numpy.ndarray'>