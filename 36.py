#!/usr/bin/env python

import os

for pid in os.listdir('/proc'):
    if pid.isdigit():
        print pid
