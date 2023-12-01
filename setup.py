from setuptools import setup, find_packages

setup(
    name='victordaletopensourcetest',
    version='0.0.1',
    description='',
    license='PRIVATE',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
    ],
    entry_points="""
        [console_scripts]
        cellularStatus = Application:main
        """,

)
