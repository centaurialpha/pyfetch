from setuptools import setup


setup(
    name='pyfetch',
    version='0.1',
    description='System information tool',
    author='?',
    author_email='acostadariogabriel@gmail.com',
    license='GPLv3+',
    packages=['pyfetch'],
    package_dir={'': 'src'},
    scripts=['bin/pyfetch'],
    # install_requires=['pyqt5'],
    # extras_require={
    #     'test': ['flake8', 'pycodestyle', 'pytest', 'pytest-cov'],
    #     'dev': ['ipython'],
    # }
)
