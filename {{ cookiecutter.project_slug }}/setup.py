from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.project_version }}",
    description="{{ cookiecutter.project_description }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    packages=find_packages(),
    install_requires=[],
    python_requires="{{ cookiecutter.python_version }}",
)

