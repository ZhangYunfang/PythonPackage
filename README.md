Welcome to your new python project!
欢迎创建新Python项目

### 1、目录/文件 - 说明

- src: Python包源文件
- venv: 虚拟环境
- LICENSE: 版本授权
- pyproject.toml: 编译系统
- README.md: 描述文件
- setup.py: 编译脚本

### 2、打包方法

- 2.1 安装 build & twine
<pre>pip install build twine</pre>

- 2.2 构建测试包
<pre>python -m build</pre>

- 2.3 安装测试
<pre>pip install .\dist\hunter_package-1.0.0.tar.gz</pre>

- 2.4 发布至PiPy
<pre>
python -m twine upload dist/*
python -m twine upload dist/* --skip-existing
python -m twine upload dist/* --skip-verbose
</pre>