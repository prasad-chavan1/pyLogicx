from setuptools import setup, find_packages

setup(
    name='pyLogix',
    version='0.1',
    packages=find_packages(),
    install_requires=['colorama'],  # Add any dependencies your package needs
    description='Utility functions and logging system.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/prasad-chavan1/pyLogix/',  # Your repository URL
    author='Prasad Chavan',
    author_email='prasadchavan1203@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
