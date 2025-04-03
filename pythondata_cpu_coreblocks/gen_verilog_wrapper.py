# Copyright (c) 2025 Piotr Wegrzyn (Coreforge Foundation) <piotro@piotro.eu>
# SPDX-License-Identifier: BSD-3-Clause

# /// script
# requires-python = ">=3.11"
# dependencies = [ 
#    "amaranth == 0.5.3",
#    "amaranth-stubs @ git+https://github.com/kuznia-rdzeni/amaranth-stubs.git@481b28c70812936d067e93e4e4cf2eb34bcc50d3",
#    "amaranth-yosys == 0.40.0.0.post100",
#    "dataclasses-json == 0.6.3",
#    "transactron @ git+https://github.com/kuznia-rdzeni/transactron@61215b518fc8049b6408cb416ec84b51c9c14a1c",
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
