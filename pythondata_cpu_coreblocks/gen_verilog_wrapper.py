# Copyright (c) 2025 Aria Wegrzyn (Coreforge Foundation) <git@ariac.at>
# SPDX-License-Identifier: BSD-3-Clause

import sys
import subprocess

COREBLOCKS_DEPENDENCY = 'git+https://github.com/awariac/coreblocks.git@9069b6faaa1158d8052fabcc95229a8b61dd4783'

if __name__ == "__main__":
    ret = subprocess.run(['pipx', 'run', '--spec', COREBLOCKS_DEPENDENCY, 'coreblocks'] + sys.argv[1:])
    sys.exit(ret.returncode)
