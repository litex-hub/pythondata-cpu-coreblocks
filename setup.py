import setuptools


setuptools.setup(
    name="pythondata-cpu-coreblocks",
    version = "0.0.2026.05.14",
    author="kuznia-rdzeni",
    author_email="org@kuznia-rdzeni.org",
    description="""\
Python module providing Coreblocks CPU to LiteX""",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/kuznia-rdzeni/coreblocks/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    zip_safe=False,
    packages=["pythondata_cpu_coreblocks"],
    include_package_data=True,
    install_requires=[
        "pipx >= 1.8.0"
    ],
    project_urls={
        "Bug Tracker": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks/issues",
        "Source Code": "https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks",
    },
)
