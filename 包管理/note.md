# 1. 模块
- 一个模块就是包含python代码的文件, 后缀名为 .py, 模块就是一个python文件
- 为什么要使用模块
    - 程序代码臃肿, 编写维护不方便, 需要拆分
    - 增加代码重复利用的方式
    - 当作命名空间使用, 避免冲突
- 如何定义模块
    - 常规 python 代码书写方式
    - 根据模块的规范, 需在模块中编写以下内容
        - 函数: 单一功能
        - 类: 相似功能的组合, 或业务模块
        - 测试代码

- 使用模块
    - 模块导入
    - 假如模块直接以数字开头， 需要借助于 importlib 包
    - 语法

            import module_name
            module_name.function_name
            module_name.class_name
    - 案例参见 01， 02， p01， p02
    - import 模块 as 别名
        - 导入模块的同时起一个别名
        - 其他语法跟第一种相同
        - 案例 p03

    - from module_name import function_name, class_name
        - 按上述方法有选择性的导入, 不需要前缀
        - 案例 p04

    - from module_name import *
        - 导入模块的所有内容
        - 案例 p05

- 'if __name__ == __main__' 的使用
    - 可以有效避免模块代码导入的时候被动执行的问题
    - 所有程序以此代码作为入口

# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的时候, 系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
        # 案例 p06.py
- 添加搜索路径

        sys.path.append(dir)
- 模块加载的顺序
    1. 上搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索 sys.path 路径


# 3. 包
- 包是一种组织管理代码的方式, 包里面存放的是模块
- 用将模块包含在一起的文件夹就是包
- 自定义包的结构

        /---包
        /---/--- __init__.py  包的标志性文件
        /---/--- 模块1
        /---/--- 模块2
        /---/--- 子包(子文件夹)
        /---/---/--- __init__.py 包的标志文件
        /---/---/--- 子包模块1
        /---/---/--- 子包模块2

- 包的导入操作
    - import package_name
        - 直接导入一个包: 可以使用 __init__.py 中的内容
        - 使用方式:

                package_name.func_name
                package_name.class_name.func_name()
        - 这种方式访问的内容是:
        - 案例 pkg01, p07.py
    - import package_name as p
        - 具体用法及作用方式, 与上述简单导入一致
        - 需注意的是这种方法是默认对 __init__.py 的导入

    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法

                package.module.func_name
                package.module.class.func()
                package.module.class.var
         - 案例 p08.py

    - import package.module as pm

- from ... import 导入
    - from package import module1, module2, module3, ...
    - 这种导入方法不执行 '__init__.py' 中的内容

            from pkg01 import p01
            p01.sayHello()
    - from package import *
        - 导入当前包 '__init__.py' 文件中所有的函数和类
        - 使用方法:

                func_name()
                class_name.func_name()
                class_name.var

        - 案例 p09.py: 注意这种导入的具体内容

- from package.module import *
    - 导入包中指定的模块的所有内容
    - 使用方法

            func_name()
            class_name.func_name()

- 在开发环境中经常会使用其他模块， 可以在当前包中直接导入其他模块的内容
    - import 完整的包或者路径

- '__all__' 的用法
    - 在使用 from package import * 的时候, * 可以导入的内容
    - '__init__.py' 中如果文件为空, 或者没有 '__all__', 那么只可以把 '__all__' 中的内容导入
    - '__init__' 如果设置了 '__all__' 的值, 那么则按照 '__all__' 指定的子包或者模块进行导入
    如此则不会载入 '__init__' 中的内容
    - '__all__=['module', 'module2', 'package1', .......]'


# 4. 明明空间
- 用于区分不同位置不同功能但名称相同的函数或者变量的一个特定前缀
- 作用是防止命名冲突

         setName()
         Student.setName()
         Dog.setName()