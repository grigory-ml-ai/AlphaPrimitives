from pathlib import Path
from setuptools import setup, find_packages


def parse_requirements():
    reqs = []
    req_file = Path(__file__).parent / 'requirements.txt'
    if req_file.exists():
        with open(req_file, 'r', encoding='utf-8') as f:
            reqs = [line.strip() for line in f
                    if line.strip() and not line.startswith('#')]
    return reqs

setup(
    name='alphaprimitives',
    version='0.1.0',
    description='utility library',
    author='Ваше имя',
    author_email='',
    install_requires=['pandas', 'numba', 'numpy', 'bottleneck', 'scipy'],
    packages=find_packages(exclude=['tests', 'tests.*', '*.tests']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)