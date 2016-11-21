#!/bin/bash
# based on:
# http://cvs.rpmfusion.org/viewvc/rpms/ffmpeg/F-10/ffmpeg-snapshot.sh?revision=1.2&root=free
# 2009-03-29 DT add request a specific revision, and use the revision number.
echo "  dvbcut-snapshot. A specific svn revision can be passed."

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)

if [ -n "$1" ]
then
  svnrev=$1
else
# determine current head/trunk svn revision number
  echo "      determining the head revision number..."
  svnrev=$(svn info https://dvbcut.svn.sourceforge.net/svnroot/dvbcut/trunk |grep Revision|cut -c11-)
fi 
echo "  retrieving revision $svnrev ..."

cd "$tmp"
svn checkout -r $svnrev https://dvbcut.svn.sourceforge.net/svnroot/dvbcut/trunk dvbcut-svn$svnrev
cd dvbcut-svn$svnrev

echo "  stripping ffmpeg and creating bzip2 archive ..."
# remove included ffmpeg sources
find . -type d -name "ffmpeg*" -print0 | xargs -0r rm -rf

# remove subversion control files
find . -type d -name .svn -print0 | xargs -0r rm -rf

# remove debian packaging files
find . -type d -name "debian*" -print0 | xargs -0r rm -rf

cd ..
tar jcf "$pwd"/dvbcut-svn$svnrev.tar.bz2 dvbcut-svn$svnrev
cd - >/dev/null

