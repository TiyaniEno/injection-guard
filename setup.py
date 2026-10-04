from setuptools import setup
setup(
    name="injection-guard",
    version="1.0.0",
    py_modules=["middleware", "__init__"],
    description="Industrial WAF middleware that blocks OS command injection in 2 lines",
    author="TiyaniEno",
    author_email="tiyani@example.com",
    license="MIT",
    install_requires=["werkzeug"],
    python_requires=">=3.7",
)
