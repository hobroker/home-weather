#!/bin/bash

set -e

SSH="pi@192.168.29.54"
REMOTE_PATH="/home/pi/apps/home-weather"

scp -r ./src/* "$SSH:$REMOTE_PATH"
