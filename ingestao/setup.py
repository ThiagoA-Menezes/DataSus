# setup.py

from setuptools import setup, find_packages

setup(
    name = 'dttools',
    version = '0.1',
    packages=find_packages(),
    description='Biblioteca criada pelo Teo Calvo para criação de um range',
    author='Thiago Menezes',
    author_email='assis.thiago@gmail.com',
    #url='https://github.com/seu-usuario/my_custom_lib',  # opcional, se estiver no GitHub
    install_requires=['datetime'],  # Dependências, se houver
)