import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scribehog",
    version="1.0.1",
    author="Marcell Endrey",
    author_email="endrey.marcell@gmail.com",
    description="Log digging helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/endreymarcell/hog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)