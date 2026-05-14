# Copyright (c) 2025 Aria Wegrzyn (Coreforge Foundation) <git@ariac.at>
# SPDX-License-Identifier: BSD-3-Clause

import sys
import subprocess

COREBLOCKS_DEPENDENCY = 'git+https://github.com/kuznia-rdzeni/coreblocks.git@65e99687fc41b4a23acc735bd5a8b1b6d4fddb24'

PYTHON3_MIN_VERSION = 13

if __name__ == "__main__":
    # pipx fails to detect other versions if shims are used and fails, always fetch required python if current interpreter is too old
    python_args = ['--python', f'3.{PYTHON3_MIN_VERSION}', '--fetch-python', 'always'] if sys.version_info[1] < PYTHON3_MIN_VERSION else []
    
    ret = subprocess.run(['pipx', 'run'] + python_args + ['--spec', COREBLOCKS_DEPENDENCY, 'coreblocks'] + sys.argv[1:])
    sys.exit(ret.returncode)
