%define svnrev 179

Name:    dvbcut
Version: 0.7.4
Release: 9%{?dist}
Summary: Clip and convert DVB transport streams to MPEG2 program streams

Group:   Applications/Multimedia
License: GPLv2+ and LGPLv2
# current upstream release location:
URL:     https://github.com/bernhardu/dvbcut-deb
#     use sh dvbcut-snapshot.sh to create the archive
Source0: https://github.com/bernhardu/dvbcut-deb/archive/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dvbcut-use_pkgconfig.patch aloisio@gmx.com -- use pkgconfig for ffmpeg libraries
Patch0:         dvbcut-use_pkgconfig.patch
# PATCH-FIX-OPENSUSE dvbcut-appicon-patch aloisio@gmx.com -- install icon in the proper path
Patch1:         dvbcut-appicon.patch
# PATCH-FIX-OPENSUSE dvbcut-locale.patch aloisio@gmx.com -- also install .qm locale files
Patch2:         dvbcut-locale.patch

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: a52dec-devel
BuildRequires: hicolor-icon-theme
BuildRequires: qt5-linguist
BuildRequires: pkgconfig
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(ao)
BuildRequires: libmad-devel
# No support for FFmpeg7 yet
%if 0%{?fedora} > 40 || 0%{?rhel} > 9
BuildRequires: compat-ffmpeg4-devel
%else
BuildRequires: ffmpeg-devel
%endif
BuildRequires: desktop-file-utils

Requires:      hicolor-icon-theme
# mplayer not actually required, but much better with it.
Recommends:    mplayer


%description
DVBcut is a Qt application that allows you to select certain parts of an MPEG
transport stream (as received via Digital Video Broadcasting, DVB) and save
these parts into a single MPEG output file. It follows a "keyhole surgery"
approach where the input video and audio data is mostly kept unchanged, and
only very few frames at the beginning and/or end of the selected range are
re-encoded in order to obtain a valid MPEG file. For MPEG video playback
dvbcut can use Mplayer if available.


%prep
%autosetup -p1 -n %{name}-deb-%{version}
rm config.guess config.sub install-sh
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

desktop-file-install                                  \
  --delete-original                                   \
  --dir %{buildroot}/%{_datadir}/applications/        \
  %{buildroot}/%{_datadir}/applications/*.desktop

%files
%doc ChangeLog CREDITS README README.icons
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/mime/packages/dvbcut.xml


%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-8
- Switch to compat-ffmpeg4-devel

* Tue Oct 22 2024 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-7
- rebuilt

* Thu Aug 01 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Leigh Scott <leigh123linux@gmail.com> - 0.7.4-3
- Rebuild for new ffmpeg

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Jul 14 2022 Leigh Scott <leigh123linux@gmail.com> - 0.7.4-1
- Update to 0.7.4

* Sun Feb 27 2022 Sérgio Basto <sergio@serjux.com> - 0.7.3-2
- Switch to compat-ffmpeg4

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 19 2021 Sérgio Basto <sergio@serjux.com> - 0.7.3-1
- Update to 0.7.3

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 0.6.1-37.svn179
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-36.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-35.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 0.6.1-34.svn179
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-33.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.6.1-32.svn179
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-31.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.6.1-30.svn179
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-29.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-28.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.6.1-27.svn179
- Rebuilt for new ffmpeg snapshot

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.6.1-26.svn179
- Rebuilt for new ffmpeg snapshot

* Wed Feb 28 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.6.1-25.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-24.svn179
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.1-23.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-22.svn179
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.1-21.svn179
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Mar 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-20.svn179
- fix missing icon (rfbz#3638)
- fix scriplets
- remove useless define
- clean up spec file

* Sat Nov  5 2016 David Timms <iinet.net.au at dtimms> - 0.6.1-19.svn179
- rebuild for ffmpeg-3.0.3
- add combined patch covering:
- ffmpeg-3.0.3 for removed deprecated definitions and functions.
- signed-unsigned comparison warnings.
- whitespace alignment warnings.
- replace tabs with spaces to match existing source files.
- c++ compiler c11 fixes (not compatble with <=F23).
- unused variables.

* Mon Oct 20 2014 David Timms <iinet.net.au at dtimms> - 0.6.1-18.svn179
- add patch for ffmpeg-2.4.3 for dropped av_new_stream().

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-17.svn179
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.6.1-16.svn179
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 0.6.1-15.svn179
- Rebuilt for ffmpeg-2.2

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-14.svn179
- Rebuilt

* Wed Sep 04 2013 David Timms <iinet.net.au at dtimms>- 0.6.1-13.svn179
- add patch to use new ffmpeg-2.0 rather than deprecated functions

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-12.svn179
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-11.svn179
- Rebuilt for x264/FFmpeg

* Sun May 19 2013 David Timms <iinet.net.au at dtimms> - 0.6.1-10.svn179
- fix changelog dates to match day as detected by mock-1.1.32-1.fc18.noarch
- fix bonus / in ffmpeg include path triggering build failure extracting debug
      info debugedit: canonicalization unexpectedly shrank by one character
    
* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-9.svn179
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-8.svn179
- Rebuilt for FFmpeg 1.0

* Wed Aug 29 2012 David Timms <iinet.net.au at dtimms> - 0.6.1-7.svn179
- drop upstreamed gcc47 patch
- add ffmpeg-0.10.4 patch dvbcut-179-vs-ubuntu-12.04.diff from Olaf Dietsche
- drop ffmpeg-0.8.2 patch superseded by ffmpeg-0.10.4 patch
- add ffmpeg-0.11.1 patch
- modify kde service install from desktop-file-install to copy.

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-6.svn178
- Rebuilt for FFmpeg

* Wed May 23 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-5.svn178
- Fix FTBFS with gcc47

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-4.svn178
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-3.svn178
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep  5 2011 David Timms <iinet.net.au at dtimms> - 0.6.1-2.svn178
- update to 0.6.1 release post svn178
- add patch for ffmpeg-0.8.2

* Mon Apr 25 2011 David Timms <iinet.net.au at dtimms> - 0.6.1-1.svn176
- update to 0.6.1 release post svn176
- includes upstream enhancement to work with certain transport streams
- delete upstreamed patches
- update makefile patches
- delete desktop file, patch included desktop file instead.

* Fri Apr 22 2011 David Timms <iinet.net.au at dtimms> - 0.6.0-13.svn170
- add patch to fix code to allow build with gcc-4.6
- add export dialog close button to suit gnome 3

* Thu Mar 17 2011 David Timms <iinet.net.au at dtimms> - 0.6.0-12.svn170
- fix Makefile.in to place files into standard locations
- fix src/Makefile to place online help in standard location
- del old icons
- package new icon and mime info files
- adjust configure/make/install to suit fixed Makefile.in

* Fri Feb 11 2011 David Timms <iinet.net.au at dtimms> - 0.6.0-11.svn170
- update to svn170 to pull in gcc-4.5 patches

* Mon Oct 26 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-10.svn166
- update to svn166
- drop upstreamed gcc44 patch
- add mpg mimetype to gnome desktop to provide mpeg open with in nautilus
- add kde service menu for mpg files for dolphin
- add help menu to package
- fix help file being placed in /usr/share/help

* Fri Oct 23 2009 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 0.6.0-9.svn157
- Update desktop file according to F-12 FedoraStudio feature

* Wed Oct 21 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.6.0-8.svn157
- rebuilt

* Mon Apr  6 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-7.svn157
- mod QTDIR configure.in patch to match newer configure.in revision

* Sat Apr  4 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-6.svn157
- use distro conditional to determine name of BR qt3-devel

* Fri Apr  3 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-5.svn157
- use another BR qt3 variant to work on both fedora and epel

* Thu Apr  2 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-4.svn157
- adjust BR for qt3 to work on both fedora and epel

* Sun Mar 29 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-3.svn157
- add gcc4 patch for rawhide

* Sun Mar 29 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-2.svn157
- update to latest post release svn checkout for minor fixes
- improve dvbcut-snapshot script to not use the checkout date
- del the debian packaging files from the snapshot archive
- mod spec to use svnver rather svndate, to make it easier to confirm sources
- del lines from DISTFILES that reference removed files

* Sat Feb  7 2009 David Timms <iinet.net.au at dtimms> - 0.6.0-1.20090207svn156
- update to 0.6.0 release, still using post release svn checkout

* Thu Jan  1 2009 David Timms <iinet.net.au at dtimms> - 0.5.4-6.20090101svn138
- add required alphatag to post release package name
- mod License to be GPLv2+ and LGPLv2
- mod -snapshot script to nuke internal ffmpeg source
- mod files to use the defined name macro
- include .tar.bz2 created with modified snapshot script. Still svn138

* Wed Dec 31 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-5.20081218
- cosmetic change, and rebuild Andrea's changes for review

* Mon Dec 29 2008 Andrea Musuruane <musuruan@gmail.com> - 0.5.4-4.20081218
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

* Sat Mar 15 2008 David Timms <iinet.net.au at dtimms> - 0.5.4-0.4.20080314svn118.fc9
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
