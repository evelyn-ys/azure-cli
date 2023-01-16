#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import logging
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

instance_cnt = int(sys.argv[1])
instance_idx = int(sys.argv[2])
working_directory = "~/.azdev/env_config/mnt/vss/_work/1/s/env"


def main():
    build_id = os.getenv('BUILD_BUILDID')
    print(f"The build id is {build_id}")

    test_result_fp = os.path.join(working_directory, f'test_results_{instance_idx}.txt')
    with open(test_result_fp, 'a') as f:
        f.write(f"results {instance_idx}/{instance_cnt}:\n")
        f.write("success 100%")


if __name__ == '__main__':
    main()
