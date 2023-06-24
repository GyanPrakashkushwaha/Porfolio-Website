from setuptools import setup, find_packages

with open(file='README.md', mode='r', encoding='utf-8') as file:
    long_description = file.read()

__version__ = '0.0.1'

REPO_NAME = 'MyProfolioWebsite'
AUTHOR_USER_NAME = 'GyanPrakashkushwaha'
SRC_REPO = 'Porfolio-Website'
AUTHOR_EMAIL = 'gyanprakashkushwaha95@gmail.com'

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Text summarizer',
    url=f"https://github.com/GyanPrakashkushwaha/{SRC_REPO}",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    long_description=long_description
)

