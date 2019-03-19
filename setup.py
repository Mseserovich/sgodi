from setuptools import setup, find_packages

setup(
    name='sort_lib_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<Mseserovich>/<sort_lib_package>',
    author='<Mseserovich>',
    author_email='<tshepo.tshabalala@moov.life>'
)
