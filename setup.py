import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='Coresets-Tests',
     version='0.1',
     author="Ben Mussay",
     author_email="bengordoncshaifa@gmail.com",
     description="Test a coreset using backpropagation",
     url="https://github.com/BenMussay/Coresets-Tests",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )