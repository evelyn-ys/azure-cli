#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import logging
import os
import sys
import subprocess

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

instance_cnt = int(sys.argv[1])
instance_idx = int(sys.argv[2])
working_directory = "~/.azdev/env_config/mnt/vss/_work/1/s/env"


def run_command(cmd, check_return_code=False):
    error_flag = False
    logger.info(cmd)
    try:
        out = subprocess.run(cmd, check=True)
        if check_return_code and out.returncode:
            raise RuntimeError(f"{cmd} failed")
    except subprocess.CalledProcessError:
        error_flag = True
    return error_flag


def install_extension(extension_module):
    try:
        cmd = ['azdev', 'extension', 'add', extension_module]
        error_flag = run_command(cmd, check_return_code=True)
    except Exception:
        error_flag = True

    return error_flag


def remove_extension(extension_module):
    try:
        cmd = ['azdev', 'extension', 'remove', extension_module]
        error_flag = run_command(cmd, check_return_code=True)
    except Exception:
        error_flag = True

    return error_flag


def main():
    module = "functionapp"
    error_flag = install_extension(module)
    logger.info(f"Finish installing extension, error_flag:{error_flag}")
    if not error_flag:
        cmd = ['azdev', 'test', module, '--discover', '--no-exitfirst', '--verbose', '--pytest-args', '"--durations=10"']
        error_flag = run_command(cmd)
        logger.info(f"Finish testing extension, error_flag:{error_flag}")
    remove_extension(module)


if __name__ == '__main__':
    main()
