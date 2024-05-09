#!/bin/bash

# config
COMMIT="64524fa8a041"
REMOTE="https://github.com/erocarrera/pefile-tests"

# clone repo and run tests
TESTDIR="$(mktemp --directory ${TMPDIR-/var/tmp}/test-XXXXXXXX)"
trap 'cd /; rm -rf "$TESTDIR"' EXIT
cd "$TESTDIR"
set -ex
git clone $REMOTE repo
cd repo
git checkout "$COMMIT"
pytest tests/pefile_test.py
