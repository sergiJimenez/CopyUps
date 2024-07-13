from setuptools import setup, find_packages

setup(
    name='copyUps',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'gitpython',
        'keyboard'
    ],
    scripts=['main.py'],
    package_data={
        'scripts': ['*.py'],
    },
    entry_points={
        'console_scripts': [
            'copyUps = main:main',
        ],
    },
    include_package_data=True,
)
