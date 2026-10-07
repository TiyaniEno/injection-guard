from setuptools import setup

setup(
    name="injection-guard-waf",
    version="1.0.0",
    description="Lightweight WAF middleware to guard against OS command injection - first line of defense",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="TiyaniEno",
    url="https://github.com/TiyaniEno/injection-guard",
    py_modules=["middleware"],
    license="MIT",
    python_requires=">=3.7",
)
