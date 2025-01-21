# author: cwb
# date: 2025/1/21

from setuptools import setup,find_packages

setup(
    #给每行加上注释
    # 包名
    name="cwb_helpers",
    # 版本
    version="0.1.0",
    # 包
    packages=find_packages(),
    # 依赖
    install_requires=["pytest"],
    # 描述
    description="cwb_helpers",
    # 作者
    author="cwb",
    # 作者邮箱
    author_email="cwb@example.com",
    # 许可证
    license="MIT",
    classifiers=[
        # 编程语言
        "Programming Language :: Python :: 3",
        # 许可证
        "License :: OSI Approved :: MIT License",
        # 操作系统
        "Operating System :: OS Independent",
    ],
    # 支持的python版本
    python_requires = ">3.6",
  

)

