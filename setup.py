import setuptools


setuptools.setup(
    version="0.0.1",
    license='mit',
    name="pool",
    author='nathan todd-stone',
    author_email='me@nathants.com',
    url='http://github.com/nathants/pool',
    install_requires=open('requirements.txt').readlines(),
    packages=setuptools.find_packages(),
)