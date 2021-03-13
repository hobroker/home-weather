#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PID="$( ps | grep app.py | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//' )"

[[ ! -z "$PID" ]] && kill -9 $PID

nohup $DIR/app.py &> $DIR/output.log &
