#!/bin/sh

build_dir=$1; shift
install_dir=$1; shift
HWAF_VARIANT=$1; shift

echo "build_dir:    [$build_dir]"
echo "install_dir:  [$install_dir]"
echo "HWAF_VARIANT: [$HWAF_VARIANT]"

set -x
set -e

/bin/mkdir -p ${install_dir}
pushd ${install_dir}

/bin/cp -ar ${build_dir}/* ${install_dir}/.
pushd ${install_dir}/mgr
./INSTALL
. ./setup.sh
make
popd

/bin/mv $CMTBIN tmp.${CMTBIN}
mkdir -p ${HWAF_VARIANT}
/bin/mv tmp.${CMTBIN}/{cmt,cmt.exe} ${HWAF_VARIANT}/.
/bin/rm -rf tmp.${CMTBIN}
/bin/ln -s $HWAF_VARIANT $CMTBIN

popd
