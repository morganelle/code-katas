"""Setup file for Mailroom Madness package."""
from setuptools import setup


dependences = ['pytest', 'tox']
extra_packages = {
    'testing': ['pytest-watch', 'pytest-cov']
}


setup(
    name='Day of Code',
    description='401 Python code katas',
    version='1.0',
    author='Morgan Nomura',
    author_email='morganelle@gmail.com',
    license='MIT',
    py_modules=['scrabble_best_word'],
    package_dir={'': 'scrabble-best-word'},
    install_requires=dependences,
    extras_require=extra_packages
)
