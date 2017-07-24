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
    py_modules=[
                'parenthetics',
                'scrabble_best_word',
                'summarize_ranges',
                'pauls_misery',
                'pairing_brackets',
                'no_zeros_for_heros',
                'where_my_anagrams_at',
                'string_pyramid'],
    package_dir={'': 'src'},
    install_requires=dependences,
    extras_require=extra_packages
)
