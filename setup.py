from setuptools import setup

setup(
    name='uveb',
    packages=['uveb'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-httpauth',
        'mysql-connector',
        'passlib'
    ],
    version='0.0.1',
    description='The backend for the VR Experience of UWC CSC',
    author='Marko Vejnovic',
    author_email='marko.vejnovic@hotmail.com',
)
