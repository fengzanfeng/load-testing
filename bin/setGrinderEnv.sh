#!/bin/bash

GRINDERPATH=$HOME/local/grinder-3.10
GRINDERPROPERTIES=$GRINDERPATH/grinder.properties
CLASSPATH=$GRINDERPATH/lib/grinder.jar:$CLASSPATH

export CLASSPATH GRINDERPROPERTIES
