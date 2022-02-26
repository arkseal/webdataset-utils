from setuptools import find_packages, setup

scripts = []

setup(
    name='webdataset_utils',
    packages=find_packages(),
    include_package_data=True,
    version='0.0.1',
    description='Util Functions and Classes for WebDataset.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/ARKseal/webdataset-utils',
    author='Aarush Katta',
    author_email='ARKsealplays@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords=[
        'object store',
        'client',
        'deep learning'
    ],
    python_requires='>=3.6',
    scripts=scripts,
    install_requires=['webdataset']
)
