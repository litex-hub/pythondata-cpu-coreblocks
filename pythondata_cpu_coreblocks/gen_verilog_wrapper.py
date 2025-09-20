# Copyright (c) 2025 Piotr Wegrzyn (Coreforge Foundation) <piotro@piotro.eu>
# SPDX-License-Identifier: BSD-3-Clause

# /// script
# requires-python = ">=3.11"
# dependencies = [ 
#    "amaranth == 0.5.4",
#    "amaranth-stubs == 0.1.1",
#    "amaranth-yosys == 0.40.0.0.post100",
#    "dataclasses-json == 0.6.3",
#    "transactron @ git+https://github.com/kuznia-rdzeni/transactron.git@343500bb1971de64b0864198478420c4b68e5e8e"
# ]
# ///

import sys
import os

if __name__ == "__main__":
    parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent)

from pythondata_cpu_coreblocks import RUN_NATIVE, PYTHON3_VERSION, data_location

sys.path += [data_location]

import scripts.gen_verilog

if __name__ == "__main__":
    if RUN_NATIVE:
        assert sys.version_info >= (3, PYTHON3_VERSION), f"Coreblocks requires >=python3.{PYTHON3_VERSION} for elaboration (in RUN_NATIVE mode)."

    scripts.gen_verilog.main()
