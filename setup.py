from setuptools import setup, find_packages

# Read requirements.txt
with open("requirements.txt", "r") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="finance-agent-system",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    author="Vedant Barbhaya",
    author_email="vedant.barbhaya@example.com",
    description="A multiagent finance system for data collection, analysis, and trading insights",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vedantbarbhaya/Finance-Agent-System",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial :: Investment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="finance, trading, multiagent, AI, data collection, financial analysis",
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "finance-agent=src.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/vedantbarbhaya/Finance-Agent-System/issues",
        "Source": "https://github.com/vedantbarbhaya/Finance-Agent-System",
        "Documentation": "https://github.com/vedantbarbhaya/Finance-Agent-System/wiki",
    },
) 