# pythondata-cpu-coreblocks

[Coreblocks](https://github.com/kuznia-rdzeni/coreblocks) cpu packaged for use with [LiteX](https://github.com/enjoy-digital/litex.git).

`gen_verilog` is wrapped with PEP723 compatible script `gen_verilog_wrapper.py`, to be run with `pipx` with correct python version and environment.

This package is python version independent.
If you want to install dependencies to your environment and elaborate with your python, set `RUN_NATIVE` in `pythondata_cpu_coreblocks/__init__.py` (read by LiteX),
and install `[native]` optional requirements.

## Installing manually

```bash
git clone https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks.git
cd pythondata-cpu-coreblocks
git submodule update --init
pip install .
```

Manually install coreblocks dependencies:

```bash
pip install -r .[native]
# or, if you changed submodule:
pip install -r pythondata_cpu_coreblocks/sources/requirements.txt
```

## Elaborate core to Verilog

```bash
pipx run --python 3.11 --fetch-missing-python pythondata_cpu_coreblocks/gen_verilog_wrapper.py <args>
```
