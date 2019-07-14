import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='google_currency',
    version='1.0.3',
    packages=['google_currency'],
    author="Hariom Tiwari",
    author_email="hariom.tiwari.006@gmail.com",
    description="A simple library to convert the currency of one country to other, it supports 153 countries' currency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/om06/google-currency",
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
