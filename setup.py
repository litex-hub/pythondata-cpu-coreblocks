import setuptools


setuptools.setup(
    name="pythondata-cpu-coreblocks",
    version="0.0.1.2024.10.27",
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
        "amaranth @ git+https://github.com/amaranth-lang/amaranth@9bd536bbf96b07720d6e4a8709b30492af8ddd13",
        "amaranth-stubs @ git+https://github.com/kuznia-rdzeni/amaranth-stubs@c0325b42e4553def483a82ffed14fdc6bf353bdb",
        "amaranth-yosys == 0.40.0.0.post100",
        "dataclasses-json >= 0.6.3"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks/issues",
        "Source Code": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks",
    },
)
