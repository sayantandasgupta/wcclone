from setuptools import setup, find_packages

setup(
    name='wcclone',
    version='0.1.0',
    author='Sayantan Dasgupta',
    author_email='sayantan.dasgupta21@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        wcclone=wcclone.wcclone:main
'''
)