from setuptools import setup, find_packages

setup(
    name='plotnn',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List any required dependencies here
        # 'numpy',
        # 'matplotlib',
        # etc.
    ],
    author='Charles Shan',
    author_email='charles.shht@gmail.com',
    description='Test',
    license='MIT'
)

# python setup.py sdist
# openssl sha256 /Users/kimshan/Public/library/plotnn/src/dist/plotnn-0.1.0.tar.gz