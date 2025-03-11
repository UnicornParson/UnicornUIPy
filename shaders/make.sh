#!/bin/bash
set -e
MAKER_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
QSB_PATH=/usr/lib/qt6/bin/qsb
# Check if qsb exists
if [[ ! -f "$QSB_PATH" ]]; then
    echo "Error: qsb tool not found at $QSB_PATH" >&2
    exit 1
fi

# Continue script execution if file exists
echo "qsb found at $QSB_PATH"

$QSB_PATH --glsl "440" --hlsl 50 --msl 12 --output $MAKER_HOME/blur.qsb $MAKER_HOME/blur.frag 