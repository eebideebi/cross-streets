#!/bin/bash

# Exit immediately if a command fails
set -e

# Step 1: Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info

# Step 2: Build the package (source + wheel)
echo "Building package..."
python setup.py sdist bdist_wheel

# Step 3: Uninstall any previous version of the package
echo "Uninstalling previous version of cross-streets (if installed)..."
pip uninstall -y cross-streets || true  # ignore error if not installed

# Step 4: Install the newly built wheel
echo "Installing the new wheel..."
# Find the .whl file in dist/
WHL_FILE=$(ls dist/*.whl | sort | tail -n 1)
pip install "$WHL_FILE"

# Step 5: Run pytest
echo "Running tests..."
pytest


# TO RUN:
# chmod +x build_and_test.sh
# ./build_and_test.sh