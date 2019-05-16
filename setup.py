from setuptools import setup

setup(
    name='pyopenexrates',
    description='An openexchangerates.org service API wrapper for Python',
    version='0.3',
    url='https://github.com/intelligems/pyopenexrates',
    author='K. Livieratos',
    author_email='kostas@intelligems.eu',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    packages=['pyopenexrates'],
    install_requires=[
        'requests>=2.19.1'
    ]
)
