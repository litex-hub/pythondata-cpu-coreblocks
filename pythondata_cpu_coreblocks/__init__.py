import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/kuznia-rdzeni/coreblocks"

# Set to true, do disable pipx execution in LiteX.
# Installation of [native] dependencies is required.
RUN_NATIVE = False
PYTHON3_VERSION = 11
