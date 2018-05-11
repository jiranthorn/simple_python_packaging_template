from setuptools import setup, find_packages
setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='packaging_template',
    # url='https://github.com/jladan/package_demo',
    author='author_name',
    # author_email='jladan@uwaterloo.ca',
    # Needed to actually package something

    packages=find_packages('src'),  # include all packages under src
    package_dir={'': 'src'},   # tell distutils packages are under src
    package_data={
        # If any package contains *.txt files, include them:
        '': ['*.xlsx', '*.xls', 'README'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        # 'mypkg': ['data/*.dat'],
    },


    # Needed for dependencies
    install_requires=['numpy', 'progressbar2'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Python Packaging template for python 2.7',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
