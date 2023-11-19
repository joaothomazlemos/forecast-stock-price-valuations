#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Joao Thomaz Lemos",
    author_email='joaothomazlemos@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Time series machine learning project to aid investor decisions based on maket at weekly, monthly and yearly rates.",
    entry_points={
        'console_scripts': [
            'predict_stock_price_valuations=predict_stock_price_valuations.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='predict_stock_price_valuations',
    name='predict_stock_price_valuations',
    packages=find_packages(include=['predict_stock_price_valuations', 'predict_stock_price_valuations.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/joaothomazlemos/predict_stock_price_valuations',
    version='0.1.0',
    zip_safe=False,
)
