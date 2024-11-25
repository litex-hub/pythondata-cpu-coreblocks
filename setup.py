import setuptools


setuptools.setup(
    name="pythondata-cpu-coreblocks",
    version="0.0.1.2024.11.25",
    author="kuznia-rdzeni",
    author_email="coreblocks@cs.uni.wroc.pl",
    description="""\
Python module containing sources files for Coreblocks cpu.""",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'': ['sources/**'],
    },
    include_package_data=True,
    install_requires=[
        "amaranth == 0.5.3",
# FIXME: There is a false-positive conflict with amarhanth-stubs versioning; but correct version is taken from transactron deps
#        "amaranth-stubs @ git+https://github.com/kuznia-rdzeni/amaranth-stubs@edb302b001433edf4c8568190adc9bd0c0039f45",
        "amaranth-yosys == 0.40.0.0.post100",
        "dataclasses-json == 0.6.3",
        "transactron @ git+https://github.com/kuznia-rdzeni/transactron@972047b7bfac3d2e193a428de35c976f9b17c51a",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks/issues",
        "Source Code": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks",
    },
)
