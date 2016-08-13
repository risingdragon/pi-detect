#!/bin/sh

kill `ps aux | grep "./motion -c motion.conf" | grep -v grep | awk '{print $2}'`
