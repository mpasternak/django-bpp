#!/bin/bash -e

pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`
popd > /dev/null
cd $SCRIPTPATH/..

export DISTDIR=$SCRIPTPATH/../dist
echo "Buduje wheels w $DISTDIR"

mkdir -p $DISTDIR
pip3 wheel -q --wheel-dir=$DISTDIR --find-links=$DISTDIR -r requirements.txt 

export DISTDIR_DEV=${DISTDIR}_dev
mkdir -p $DISTDIR_DEV
pip3 wheel -q --wheel-dir=$DISTDIR_DEV --find-links=$DISTDIR --find-links=$DISTDIR_DEV -r requirements_dev.txt 
