# coding: utf-8

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hunter_package",
    version="1.0.0",
    author="Hunter Zhang",
    author_email="zhangyunfang0302@gmail.com",
    description="A test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZhangYunfang/PythonPackage",
    project_urls={
        "Bug Tracker": "https://github.com/ZhangYunfang/PythonPackage/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src', exclude=(), include=('*',)),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        # 依赖包
        # 'pandas',
    ],
)
