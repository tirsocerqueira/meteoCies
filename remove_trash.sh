#!/bin/bash

# Change to directory
cd /path/to/directory

# Removing .mp4 y .jpg
find . -name "*.mp4" -type f -delete
find . -name "*.jpg" -type f -delete


# To cron the job:
# chmod +x remove_trash.sh
# 1) crontab -e
# 2) 0 23 * * * /path/to/remove_trash.sh