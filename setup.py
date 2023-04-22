import setuptools


setuptools.setup(
    name="pythondata-cpu-coreblocks",
    version="0.0.1", # todo commit hash
    author="",
    author_email="",
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
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'': ['sources/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks/issues",
        "Source Code": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks",
    },
)
