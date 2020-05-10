# Python import

假设有如下目录结构：

```text
-- dir0
　　| file1.py
　　| file2.py
　　| dir3
　　　| file3.py
　　| dir4
　　　| file4.py
```

dir0 文件夹下有 file1.py、file2.py 两个文件和 dir3、dir4 两个子文件夹，dir3 中有 file3.py 文件，dir4 中有 file4.py 文件。

## 导入同级模块

python导入同级模块（在同一个文件夹中的py文件）直接导入即可。

```python
import xxx
```

如在 file1.py 中想导入 file2.py，注意无需加后缀 ".py"：

```python
import file2
# 使用 file2 中函数时需加上前缀 "file2."，即：
# file2.fuction_name()
```

## 导入下级模块

导入下级目录模块也很容易，需在下级目录中新建一个空白的 `__init__.py` 文件再导入：

```python
from dirname import xxx
```

如在 file1.py 中想导入 dir3 下的 file3.py，首先要在 dir3 中新建一个空白的 `__init__.py` 文件。

```text
-- dir0
　　| file1.py
　　| file2.py
　　| dir3
　　　| __init__.py
　　　| file3.py
　　| dir4
　　　| file4.py
```

再使用如下语句：

```python
# plan A
from dir3 import file3
```

或是

```python
# plan B
import dir3.file3
# import dir3.file3 as df3
```

但使用第二种方式则下文需要一直带着路径 dir3 书写，较为累赘，建议可以另起一个别名。

## 导入上级模块

要导入上级目录下模块，可以使用 `sys.path`： 　

```python
import sys 
sys.path.append("..") 
import xxx　
```

如在 file4.py 中想引入 import 上级目录下的 file1.py：

```python
import sys 
sys.path.append("..") 
import file1
```

**sys.path** 的作用：当使用 import 语句导入模块时，解释器会搜索当前模块所在目录以及sys.path 指定的路径去找需要 import 的模块，所以这里是直接把上级目录加到了 sys.path 里。

**".."** 的含义：等同于 linux 里的".."，表示当前工作目录的上级目录。实际上 python 中的 "." 也和 linux 中一致，表示当前目录。

## 导入隔壁文件夹下的模块

如在 file4.py 中想引入 import 在 dir3 目录下的 file3.py。

这其实是前面两个操作的组合，其思路本质上是将上级目录加到 sys.path 里，再按照对下级目录模块的方式导入。

同样需要被引文件夹也就是dir3下有空的 `__init__.py` 文件。

```text
-- dir
　　| file1.py
　　| file2.py
　　| dir3
　　　| __init__.py
　　　| file3.py
　　| dir4
　　　| file4.py
```

同时也要将上级目录加到 sys.path 里：

```python
import sys
sys.path.append("..")
from dir3 import file3
```

## 常见错误及 import 原理

在使用直接从上级目录引入模块的操作时：

```python
from .. import xxx
```

经常会报错:

```python3
ValueError: attempted relative import beyond top-level package
```

这是由于相对导入时，文件夹实质上充当的是 package，也就是包的角色（比如我们常用的numpy、pandas 都是包）。如果 python 解释器没有认同该文件夹是 package，那么这就是一个普通的文件夹，无法实现相对导入。

文件夹作为 package 需要满足如下两个条件：

1. 文件夹中必须存在有 `__init__.py` 文件，可以为空。
2. 不能作为顶层模块来执行该文件夹中的 py 文件。

## 实践

```bash
% tree .
.
├── README.md
├── __init__.py
├── dir1
│   ├── __init__.py
│   ├── dir2
│   │   ├── __init__.py
│   │   ├── dir3
│   │   │   ├── __init__.py
│   │   │   └── test4_1.py
│   │   ├── test3_1.py
│   │   └── test3_2.py
│   ├── test2_1.py
│   └── test2_2.py
├── test1_1.py
└── test1_2.py

3 directories, 12 files
%
```
