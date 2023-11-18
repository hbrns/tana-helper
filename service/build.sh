#!/bin/sh

# activate correct python virtual env
poetry env use 3.11
source .venv/bin/activate
poetry install --no-root

# build ther swift script first
# Compile for macOS
test -f "service/bin" && rm -r "service/bin"
mkdir -p service/bin

echo "Building for macOS arm64..."
ARCH=arm64
swiftc service/scripts/getcalendar.swift -o service/bin/getcalendar.${ARCH} -target arm64-apple-macosx10.15

echo "Building for macOS amd64..."
ARCH=amd64
swiftc service/scripts/getcalendar.swift -o service/bin/getcalendar.${ARCH} -target x86_64-apple-macosx10.15

echo "Packaging universal binary..."
lipo -create -output service/bin/getcalendar service/bin/getcalendar.arm64 service/bin/getcalendar.amd64

echo "Removing arch builds..."
rm service/bin/*.arm64 service/bin/*.amd64


# build the python bundle for menubar app and start wrapper
# build the .app bundle 

test -f "dist" && rm -r "dist"
pyinstaller tanahelper.spec --noconfirm