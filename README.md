# pythondata-cpu-coreblocks

[Coreblocks](https://github.com/kuznia-rdzeni/coreblocks) CPU packaged for use with [LiteX](https://github.com/enjoy-digital/litex.git).

`pipx` is the recommended way of running Verilog generation for Coreblocks.
This package is python version independent and it only provides wrapper that runs 'pipx' on a pinned Coreblocks version.

If you want to hack on Coreblocks source and use it with LiteX, install editable (or other) `coreblocks` package (not `pythondata-cpu-coreblocks`) in a LiteX virtual environment (note python version requirements) and use "LITEX_COREBLOCKS_RUN_NATIVE=1" environment variable on LiteX generation to use the local `coreblocks` package directly.

You can also provide any custom core configuration using this wrapper and only environment variables.
Set `LITEX_COREBLOCKS_CORECONFIG_FILE=<coreconfig file path, see --help>`, `LITEX_COREBLOCKS_CORECONFIG=<selected configuration name>`, `LITEX_COREBLOCKS_RUN_NATIVE=0` for LiteX generation.

## Installing manually

```bash
git clone https://github.com/kuznia-rdzeni/pythondata-cpu-coreblocks.git
pip install .
```

## Elaborating core to Verilog

```bash
python pythondata-cpu-coreblocks/gen_verilog_wrapper.py --help
```

or without this package

```bash
pipx run --spec <coreblocks package source or skip --spec for pypi default> coreblocks --help
```

## Issues

Report CPU issuses in the [Coreblocks](https://github.com/kuznia-rdzeni/coreblocks) repository.
