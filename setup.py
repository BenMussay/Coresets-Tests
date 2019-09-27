import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coreset_test",
    version="0.0.1",
    author="Ben Mussay",
    author_email="bengordoncshaifa@gmail.com",
    description="A method for testing coresets using backpropagation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenMussay/Coresets-Tests",
    packages=["."],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)