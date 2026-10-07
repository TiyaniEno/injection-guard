from setuptools import setup, find_packages

setup(
    name="injection-guard-waf",
    version="1.0.0",
    description="Lightweight WAF middleware to guard against OS command injection - first line of defense",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TiyaniEno",
    author_email="tiyani@example.com",
    url="https://github.com/TiyaniEno/injection-guard",
    py_modules=["middleware", "__init__"],
    license="MIT",
    classifiers=[
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
