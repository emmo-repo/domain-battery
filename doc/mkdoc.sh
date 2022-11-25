#!/bin/sh
# Bash script for generating documentation
set -ex

# Directories
rootdir=$(git rev-parse --show-toplevel)
ontodocdir=${rootdir}/doc
tmpdir=${ontodocdir}/tmp

cd ${ontodocdir}

mkdir -p ${tmpdir}/figs
cp -u ${rootdir}/doc/img/bigmap.png ${tmpdir}/figs/.

ontograph -m ${rootdir}/battery.ttl ${tmpdir}/battery-structure.png
ontoconvert -si -- ${rootdir}/battery.ttl ${tmpdir}/battery-inferred.ttl
ontoconvert -si -- ${rootdir}/batteryquantities.ttl ${tmpdir}/batteryquantities-inferred.ttl

ontodoc --template=battery.md --format=html ${tmpdir}/battery-inferred.ttl \
        ${tmpdir}/battery.html

ontodoc --template=battery.md ${tmpdir}/battery-inferred.ttl \
        ${tmpdir}/battery.pdf
