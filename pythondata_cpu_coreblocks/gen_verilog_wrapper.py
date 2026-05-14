# Copyright (c) 2025 Aria Wegrzyn (Coreforge Foundation) <git@ariac.at>
# SPDX-License-Identifier: BSD-3-Clause

import sys
import subprocess

COREBLOCKS_DEPENDENCY = 'git+https://github.com/kuznia-rdzeni/coreblocks.git@65e99687fc41b4a23acc735bd5a8b1b6d4fddb24'

if __name__ == "__main__":
    ret = subprocess.run(['pipx', 'run', '--spec', COREBLOCKS_DEPENDENCY, 'coreblocks'] + sys.argv[1:])
    sys.exit(ret.returncode)
