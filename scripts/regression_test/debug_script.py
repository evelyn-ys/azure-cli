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


def rerun_setup(cli_repo_path, extension_repo_path):
    try:
        if extension_repo_path:
            cmd = ['azdev', 'setup', '-c', cli_repo_path, '-r', extension_repo_path, '--debug']
        else:
            cmd = ['azdev', 'setup', '-c', cli_repo_path, '--debug']
        error_flag = run_command(cmd, check_return_code=True)
    except Exception:
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
    print(f"working directory: {os.getenv('BUILD_SOURCESDIRECTORY')}")
    print(f"cli repo path: {os.getenv('REPO', None)}")
    print(f"extension repo path: {os.getenv('EXTENSIONREPO', None)}")
    # modules = ["functionapp", "alertsmanagement"]
    # for module in modules:
    #     error_flag = install_extension(module)
    #     logger.info(f"Finish installing extension {module}, error_flag:{error_flag}")
    #     if not error_flag:
    #         cmd = ['azdev', 'test', module, '--discover', '--no-exitfirst', '--verbose', '--pytest-args', '"--durations=10"']
    #         error_flag = run_command(cmd)
    #         logger.info(f"Finish testing extension {module}, error_flag:{error_flag}")
    #     remove_extension(module)
    #     logger.info(f"Finish removing extension {module}, error_flag:{error_flag}")
    #     if error_flag:
    #         rerun_setup(cli_repo_path=os.getenv('BUILD_SOURCESDIRECTORY'), extension_repo_path=f"{os.getenv('BUILD_SOURCESDIRECTORY')}/azure-cli-extensions")


if __name__ == '__main__':
    main()
