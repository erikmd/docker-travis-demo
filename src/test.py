#!/usr/bin/env python3
import sys

print("test.py ... STDERR", flush=True, file=sys.stderr)
print("Hello world STDOUT", flush=True)
print("    exit(1) STDERR", flush=True, file=sys.stderr)

exit(1)
