#!/bin/bash
cd ~
# Attempt to save the world data if the server is on :
(screen -p 0 -S "mc-${@}" -X eval 'stuff "save-all"\\015' && sleep 5) || true
source ~/.bashrc
python3 ~/backup.py "${@}"
