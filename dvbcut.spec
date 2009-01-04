# svn revision 138
%define svndate 20090101

Name:    dvbcut
Version: 0.5.4
Release: 7.%{svndate}svn138%{?dist}
Summary: Clip and convert DVB transport streams to MPEG2 program streams

Group:   Applications/Multimedia
License: GPLv2+ and LGPLv2
URL:     http://dvbcut.sourceforge.net/
# No release has been made since 2007-mid, so using svn checkout for latest fixes:
#Source0: http://downloads.sourceforge.net/dvbcut/dvbcut_%{version}.tar.bz2
#     use sh dvbcut-snapshot.sh to create the archive
Source0: %{name}-%{svndate}.tar.bz2
# Since no icons have been developed by the project, created icons using the
#     weblogo on the home page. Scaled and text pixel edited using gimp.
Source1: %{name}.logo.16x16.png
Source2: %{name}.logo.24x24.png
Source3: %{name}.logo.48x48.png
# This desktop file was created by hand.
Source4: %{name}.desktop
Source5: %{name}-snapshot.sh

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: autoconf
BuildRequires: qt-devel
BuildRequires: libao-devel 
BuildRequires: a52dec-devel 
BuildRequires: libmad-devel
BuildRequires: ffmpeg-devel
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme
# mplayer not actually required, but much better with it.
Requires: mplayer

%description
dvbcut is a Qt application that allows you to select certain parts of an MPEG
transport stream (as received via Digital Video Broadcasting, DVB) and save
these parts into a single MPEG output file. It follows a "keyhole surgery"
approach where the input video and audio data is mostly kept unchanged, and
only very few frames at the beginning and/or end of the selected range are 
re-encoded in order to obtain a valid MPEG file. For mpeg video playback
dvbcut can use mplayer if available.


%prep
%setup -q -n %{name}-%{svndate}

# Fix QTDIR libs in configure
sed -i 's,-L$QTDIR/$mr_libdirname,-L$QTDIR/lib,' configure.in

# Avoid stripping binaries
sed -i 's,$(STRIP) $(topdir)/bin/dvbcut$(EXEEXT),,' src/Makefile.in


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
autoconf
%configure --with-ffmpeg=%{_prefix} \
    --with-ffmpeg-include=%{_includedir}/ffmpeg/
# It does not compile with smp_mflags
make


%install
rm -rf %{buildroot}
make install \
    bindir=%{buildroot}%{_bindir} \
    mandir=%{buildroot}%{_mandir}

# manual install of icons
for iconsize in 16x16 24x24 48x48; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$iconsize/apps/
done
install -p -m 644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
install -p -m 644 %{SOURCE3} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
    --dir %{buildroot}%{_datadir}/applications %{SOURCE4}


%clean
rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING CREDITS README README.icons
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Mon Jan  5 2009 David Timms <iinet.net.au at dtimms> - 0.5.4-7.20090101svn138
- mod BR qt3 to qt for EL-5 branch

* Thu Jan  1 2009 David Timms <iinet.net.au at dtimms> - 0.5.4-6.20090101svn138
- add required alphatag to post release package name
- mod License to be GPLv2+ and LGPLv2
- mod -snapshot script to nuke internal ffmpeg source
- mod files to use the defined name macro
- include .tar.bz2 created with modified snapshot script. Still svn138

* Wed Dec 31 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-5.20081218
- cosmetic change, and rebuild Andrea's changes for review

* Mon Dec 28 2008 Andrea Musuruane <musuruan@gmail.com> - 0.5.4-4.20081218
- removed ugly configure hack in %%install
- removed %%{?_smp_mflags} from make invocation
- patched configure to fix qt lib dir
- cosmetic changes

* Wed Dec 24 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-3.20081218
- fix x86_64 configure by supplying qt lib dir

* Tue Dec 23 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-2.20081218
- add BR: autoconf to solve mock build issue
- del repeated parameters from build due to change to configure macro

* Mon Dec 22 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-1.20081218
- use correct post release versioning scheme
- remove --vendor from desktop-file-install
- remove .desktop en-au identical translation
- use configure macro instead of ./configure in build and install
 
* Sun Dec 21 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.13.20081218
- remove execute permission from dvbcut-snapshot.sh
- add re-configure in %%install to move installdir reference from %%build

* Sun Dec 21 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.12.20081218
- fix generation of debuginfo
- test rebuild against ffmpeg-libs-0.4.9-0.57.20081217.fc11

* Sat Dec 20 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.11.20081218
- change to autotools build system
- fix icon source file install
- drop ffmpeg path patches; autotools solves this ;)

* Sat Dec 20 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.10.20081218
- mod icon install to work in a loop
- del some old comments

* Thu Dec 18 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.9.20081218
- update to current svn revision 138
- add Requires: hicolor-icon-theme to provide correct icon dir ownership
- del DesktopFileVersion: field from .desktop file
- del .desktop icon filename size indicator, so that system can choose
- mod icon install to use a common png filename below icons/size/apps/
- add shell script to archive a dated svn revision
- add patches for ffmpeg's change in include folder layout

* Wed Jun 25 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.8.20080621svn131
- add conditional build requires to ensure it builds against correct qt[3]-devel

* Sat Jun 21 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.7.20080621svn131
- previous build crashes if the export via ffmpeg functions are used
- update to current svn revision

* Sun Jun 15 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.6.20080621svn129
- update to current svn revision
- upstream added make/autoconf via configure/make to the source, but we are are 
      able to fallback to SCons build - which succeeded.

* Sat Jun 07 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.5.20080607svn125.fc9
- update to current svn revision, unsuccessful compile. SCons issues.

* Sat Mar 14 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.4.20080314svn118.fc9
- add BuildRequires desktop-file-utils so that it builds properly in mock.
- update to new upstream svn version.
- drop patch0-4 since similar have been committed upstream.

* Sat Mar  1 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.3.20080217svn116.fc9
- patch SContruct to generate decent debuginfo.
- fix install to use make install. Fixes docs install problem.
- add man to files.
- del BuildRequires gettext desktop-file-utils since they aren't required.
- del Requires qt ffmpeg since rpm should take care of that.

* Fri Feb 29 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.2.20080217svn116.fc9
- mod spec to suit svn release. include patches, icons, desktop file.

* Thu Nov 08 2007 David Timms <iinet.net.au at dtimms> - 0.5.4-0.1
- initial package for fedora (based on Herbert Graeber packman effort)

