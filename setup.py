import setuptools


setuptools.setup(
    name="pythondata-cpu-coreblocks",
    version="0.0.1.2024.02.08",
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
        "amaranth @ git+https://github.com/amaranth-lang/amaranth@94c504afc7d81738ecdc9523a2615ef43ecbf51a",
        "amaranth-yosys >= 0.35",
        "typing-extensions >= 4.9"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks/issues",
        "Source Code": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks",
    },
)
