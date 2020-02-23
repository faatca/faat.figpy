from pathlib import Path
import re
from setuptools import setup

here = Path(__file__).parent


def find_version(path):
    content = path.read_text(encoding="utf-8")
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="faat.figpy",
    version=find_version(here / "faat" / "figpy" / "__init__.py"),
    description="Simple configuration library using python syntax",
    long_description=(here / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/faatca/faat.figpy",
    author="Aaron Milner",
    author_email="aaron.milner@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["faat.figpy"],
    install_requires=[],
    python_requires=">=3.6",
)
