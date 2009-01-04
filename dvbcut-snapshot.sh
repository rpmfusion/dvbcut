#!/bin/bash
# based on:
# http://cvs.rpmfusion.org/viewvc/rpms/ffmpeg/F-10/ffmpeg-snapshot.sh?revision=1.2&root=free

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
svn=$(date +%Y%m%d)

cd "$tmp"
svn checkout -r {$svn} https://dvbcut.svn.sourceforge.net/svnroot/dvbcut/trunk dvbcut-$svn
cd dvbcut-$svn

# remove included ffmpeg sources
find . -type d -name "ffmpeg*" -print0 | xargs -0r rm -rf

# remove subversion control files
find . -type d -name .svn -print0 | xargs -0r rm -rf

cd ..
tar jcf "$pwd"/dvbcut-$svn.tar.bz2 dvbcut-$svn
cd - >/dev/null


