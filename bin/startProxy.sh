#!/bin/bash

source setGrinderEnv.sh
java -classpath $CLASSPATH net.grinder.TCPProxy -console -http >grinder.py
