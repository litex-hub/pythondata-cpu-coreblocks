# pythondata-cpu-coreblocks

Files needed for the Coreblocks cpu packaged into a Python module so they can be used with Python libraries and tools.

This is useful for usage with tools like
[LiteX](https://github.com/enjoy-digital/litex.git).

The data files can be found under the Python module `pythondata_cpu_coreblocks` The
`pythondata_cpu_coreblocks.data_location` value can be used to find the files on the file
system.


# Installing manually

```
git clone https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks.git
cd pythondata-cpu-coreblocks
git submodule update --init --recursive --remote
python setup.py install
```

