import setuptools


setuptools.setup(
    name="pythondata-cpu-coreblocks",
    version="0.0.1.2025.09.30",
    author="kuznia-rdzeni",
    author_email="org@kuznia-rdzeni.org",
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
    python_requires='>=3.8',
    zip_safe=False,
    packages=["pythondata_cpu_coreblocks"],
    package_data={
    	'': ['sources/**'],
    },
    include_package_data=True,
    install_requires=[
        "pipx"
    ],
    extras_require={
        "native": [
            "amaranth == 0.5.4",
            "amaranth-stubs == 0.1.1",
            "amaranth-yosys == 0.40.0.0.post100",
            "dataclasses-json == 0.6.3",
            "transactron == 0.3.1",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks/issues",
        "Source Code": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks",
    },
)
