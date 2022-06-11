from setuptools import setup

setup(
    name='settle-up-adapter',
    version='1.0.0',
    packages=['app', 'app.api', 'app.core', 'app.utils', 'app.models', 'app.services'],
    url='https://github.com/joern1811/settle-up-adapter',
    license='MIT',
    author='Jörn Dombrowski',
    author_email='joern.dombrowski@gmail.com',
    description='A REST-API adapter for the Settle-Up-Application.',
    install_requires=[
        'fastapi',
        'starlette',
        'pydantic',
        'logging',
        'uvicorn',
        'requests',
        'pyrebase'
    ]
)
