from setuptools import setup, find_packages


DESCRIPTION = """\
AwesomeAiogram is a framework for quickly creating and maintaining projects based on the Aiogram library.
"""


LONG_DESCRIPTION = """\
**AwesomeAiogram** is a framework for quickly creating and maintaining projects based on the Aiogram library.

Inspired by Django, we aimed to simplify common boilerplate code with automatic generation triggered by a single or
multiple commands. We focused on making it universal and scalable, like a modular builder where you use ready-made
building blocks to construct your project—while keeping it independent from requiring all blocks to function.
"""

setup(
    # Base:
    name="AwesomeAiogram",
    version="0.1",

    # Credentials:
    url="https://github.com/DriveWaveTech",
    author="DriveWaveTech",

    # Descriptions:
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    # Packages:
    python_requires=">=3.12",
    packages=find_packages(),
    install_requires=[
        # Base Modules:
        'python-dotenv==1.0.1',
        'loguru==0.7.2',

        # Parsing Modules:
        'PyYAML==6.0.2',
        'Jinja2==3.1.4',

        # Database Modules:
        'asyncpg==0.30.0',
        'SQLAlchemy==2.0.36',
        'alembic==1.13.3',

        # Telegram Modules:
        'aiogram==3.13.1',
    ],

    # Run:
    entry_points={
        'console_scripts': [
            'AwesomeAiogram=AwesomeAiogram:main',
        ],
    },

    # Other:
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
