#!/bin/bash

GRINDERPATH=$HOME/grinder-3.10
GRINDERPROPERTIES=$GRINDERPATH/grinder.properties
CLASSPATH=$GRINDERPATH/lib/grinder.jar:$CLASSPATH

export CLASSPATH GRINDERPROPERTIES
