import setuptools


setup_params = dict(
    name='pyswiss',
    version='0.0.1',
    description='A collection of python tools and language insights.',
    author="Mathias Bustamante",
    author_email="mathiasbc@gmail.com",
    url="https://github.com/mathiasbc/pyswiss",
    download_url="https://github.com/mathiasbc/pyswiss/tarball/0.0.1",
    packages=['pyswiss'],
    install_requires=[
        'pytest==2.8.3',
    ]
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
