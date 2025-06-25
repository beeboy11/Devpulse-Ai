from setuptools import setup, find_packages

setup(
    name="devpulse",
    version="0.1.0",
    description="AI-powered, brutally honest, terminal error and command explanations for developers.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abiodun",
    author_email="beeboyabiodun111@gmail.com",
    url="https://github.com/beeboy11/devpulse",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-google-genai",
        "python-dotenv",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "devpulse=devpulse.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
