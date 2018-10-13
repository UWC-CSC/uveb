from setuptools import setup

setup(
    name='uveb',
    packages=['uveb'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-httpauth',
        'passlib'
    ]
)
