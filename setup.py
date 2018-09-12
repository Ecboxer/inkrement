import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='inkrement',
    version='0.0.1',
    author='Eric Boxer',
    author_email='ecb2198@columbia.edu',
    description='Incremental data visualization in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Ecboxer/inkrement',
    packages=['inkrement'],
    install_requires=[
        'matplotlib.pyplot>=2.2.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)    
