from pathlib import Path
from setuptools import find_packages, setup

# Load version number
__version__ = ''
version_file = Path(__file__).parent.absolute() / 'SyntheMol' / '_version.py'

with open(version_file) as fd:
    exec(fd.read())

# Load README
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SyntheMol',
    version=__version__,
    author='Kyle Swanson',
    author_email='swansonk.14@gmail.com',
    description='SyntheMol',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swansonk14/SyntheMol',
    download_url=f'https://github.com/swansonk14/SyntheMol/archive/refs/tags/v_{__version__}.tar.gz',
    license='MIT',
    packages=find_packages(),
    package_data={'SyntheMol': ['py.typed']},
    install_requires=[  # TODO: add chem_utils here
        'chemprop',
        'descriptastorus',
        'matplotlib',
        'numpy',
        'pandas',
        'rdkit-pypi',
        'scikit-learn',
        'scipy',
        'tqdm',
        'typed-argument-parser'
    ],
    python_requires='>=3.10',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Typing :: Typed"
    ],
    keywords=[
        'machine learning',
        'drug design',
        'generative models',
        'synthesizable molecules'
    ]
)
