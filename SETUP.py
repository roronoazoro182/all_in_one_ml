Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    authors="Jaimin Patel","Aayush Sangani","Samar Save","Rishabh Shetty","Abhishek Swain"
    authors_email="jaimin.vs.p@gmail.com","aayushsangani@gmail.com","samar.save1@gmail.com","rpshetty27@gmail.com","abhishekswain182@gmail.com",
    description="all in one machine learning package",
    long_description="This package contains all the essential aspects of machine learning.This package will help the user to build basic machine learning projects.",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)  
