#!/bin/sh

set -e

cd tools/build/v2 || exit 1
#LOCATE_TARGET=${BOOST_BJAM_LOCATE_TARGET} ./bootstrap.sh
./bootstrap.sh

## EOF ##
