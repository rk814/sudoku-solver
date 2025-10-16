from setuptools import setup, find_packages

setup(
    name="sudoku-solver",
    version="0.1.0",
    description="Sudoku solver and brute force creator",
    author="Rafał Krawczyk",
    author_email="r.krawczyk@live.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [],
    },
    # extras_require={
    #     'test': ['pytest'],
    # },
    test_suite='test',
)
