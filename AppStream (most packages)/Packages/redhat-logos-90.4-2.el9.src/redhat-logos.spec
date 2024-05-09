%global codename sphericalcow
# Package is only arch specific due to missing deps on arm
# Debuginfo package is useless.
%global debug_package %{nil}

Name:       redhat-logos
Version:    90.4
Release:    2%{?dist}
Summary:    Red Hat-related icons and pictures

Group:      System Environment/Base
URL:        http://www.redhat.com
# No upstream, done in internal git
Source0:    redhat-logos-%{version}.tar.xz
License:    Licensed only for approved usage, see COPYING for details.

Obsoletes:  redhat-logos < 80.1-2
Provides:   system-logos = %{version}-%{release}

Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5

Requires(post): coreutils
BuildRequires: hardlink

%description
Licensed only for approved usage, see COPYING for details.

%package httpd
Summary: Red Hat-related icons and pictures used by httpd
Provides: system-logos-httpd = %{version}-%{release}
Provides: redhat-logos-httpd = %{version}-%{release}
BuildArch: noarch

%description httpd
Licensed only for approved usage, see COPYING for details.

%package ipa
Summary: Red Hat-related icons and pictures used by ipa
Provides: system-logos-ipa = %{version}-%{release}
Provides: redhat-logos-ipa = %{version}-%{release}
BuildArch: noarch

%description ipa
Licensed only for approved usage, see COPYING for details.

%package -n redhat-backgrounds
Summary: Red Hat-related desktop backgrounds
BuildArch: noarch

Obsoletes: redhat-logos < 80.1-2
Provides:  system-backgrounds = %{version}-%{release}
Requires:  redhat-logos = %{version}-%{release}

%description -n redhat-backgrounds
Licensed only for approved usage, see COPYING for details.


%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/
for i in backgrounds/*.jpg backgrounds/*.xml; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.background.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
install -p -m 644 backgrounds/10_org.gnome.desktop.screensaver.default.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/
install -p -m 644 backgrounds/desktop-backgrounds-default.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
for i in firstboot/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/themes/fedora-%{codename}/
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

# create hardlink for system-noindex-logo.png which is a part of separate
# package (system-logos-httpd)
ln $RPM_BUILD_ROOT%{_datadir}/pixmaps/fedora-gdm-logo.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/system-noindex-logo.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
for i in plymouth/charge/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/charge
done

for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  done
done


mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
pushd $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_datadir}/icons/hicolor/16x16/apps/fedora-logo-icon.png favicon.png
popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/xfce4_xicon1.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/fedora-logo-icon.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/start-here.svg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
ln -s ../apps/start-here.svg .
popd

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a fedora/*.svg $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.png $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images
cp -a ipa/*.jpg $RPM_BUILD_ROOT%{_datadir}/ipa/ui/images

mkdir -p $RPM_BUILD_ROOT%{_datadir}/testpage
install -p -m 644 testpage/index.html $RPM_BUILD_ROOT%{_datadir}/testpage

mkdir -p $RPM_BUILD_ROOT%{_datadir}/testpage/
cp -a testpage/index.html $RPM_BUILD_ROOT%{_datadir}/testpage/

# save some dup'd icons
# Except in /boot. Because some people think it is fun to use VFAT for /boot.
/usr/bin/hardlink -v %{buildroot}/usr

%ifnarch x86_64 i686
rm -f $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/splash.lss
%endif

%post
touch --no-create %{_datadir}/icons/hicolor || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/favicon.png
%{_datadir}/firstboot/themes/fedora-%{codename}/
%{_datadir}/plymouth/themes/charge/

%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%exclude %{_datadir}/pixmaps/system-noindex-logo.png
%{_datadir}/anaconda/pixmaps/*
%ifarch x86_64 i686
%{_datadir}/anaconda/boot/splash.lss
%endif
%{_datadir}/anaconda/boot/syslinux-splash.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/%{name}/

%{_datadir}/glib-2.0/schemas/*.override

# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/backgrounds
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/22x22/apps/
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/36x36/
%dir %{_datadir}/icons/hicolor/36x36/apps/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%dir %{_datadir}/icons/hicolor/96x96/
%dir %{_datadir}/icons/hicolor/96x96/apps/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%dir %{_datadir}/icons/hicolor/scalable/places/
%dir %{_datadir}/anaconda
%dir %{_datadir}/anaconda/boot/
%dir %{_datadir}/anaconda/pixmaps
%dir %{_datadir}/firstboot/
%dir %{_datadir}/firstboot/themes/
%dir %{_datadir}/plymouth/
%dir %{_datadir}/plymouth/themes/

%files httpd
%license COPYING
%{_datadir}/testpage
%{_datadir}/testpage/index.html
%{_datadir}/pixmaps/poweredby.png
%{_datadir}/pixmaps/system-noindex-logo.png

%files ipa
%license COPYING
%{_datadir}/ipa/ui/images/*
# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/ipa
%dir %{_datadir}/ipa/ui
%dir %{_datadir}/ipa/ui/images

%files -n redhat-backgrounds
%license COPYING
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/*


%changelog
* Mon May 15 2023 Ray Strode <rstrode@redhat.com> - 90.4-2
- Drop deps neeed by splashtolss.sh since we don't use it anymore
  Resolves: #2203822

* Thu Feb 17 2022 Ray Strode <rstrode@redhat.com> - 90.4-1
- Prune set a bit based on design feedback and
  change default.
  Resolves: #2047663

* Thu Feb 17 2022 Ray Strode <rstrode@redhat.com> - 90.3-1
- Add initial cut at RHEL 9 branding
  Related: #2047663

* Fri Aug 20 2021 Ray Strode <rstrode@redhat.com> - 90.2-1
- Strip RHEL 8 branding and use graytones until until RHEL 9 branding is available
  Resolves: #1975387

* Fri Aug 06 2021 Luboš Uhliarik <luhliari@redhat.com> - 90.1-1
- New web server test page
- Resolves: #1956386

* Mon Jun 14 2021 Ray Strode <rstrode@redhat.com> - 90.0-1
- Add trademark footer on web server test page
  Resolves: #1956741

* Tue Feb 16 2021 Vendula Poncova <vponcova@redhat.com> - 85.1-1
- Add a custom installer stylesheet for RHEL
  Resolves: #1928711

* Fri Jan 29 2021 Ray Strode <rstrode@redhat.com> - 84.1-1
- Add a few more rotated backgrounds
  Resolves: #1854287

* Thu Jan 28 2021 Ray Strode <rstrode@redhat.com> - 84.0-1
- Improve appearance of backgrounds on rotated tablets
  Resolves: #1854287

* Tue Nov 10 2020 Lubos Uhliarik <luhliari@redhat.com> - 82.2-1
- Add web server test page index.html to redhat-logos
  Resolves: #1896319

* Fri Aug 16 2019 Ray Strode <rstrode@redhat.com> - 81.1-1
- Add missing metadata in 8 abstract light wallpapers
  Related: #1720610

* Mon Aug 12 2019 Ray Strode <rstrode@redhat.com> - 81.0-1
- Add wallpapers for wider screen monitors
  Related: #1720610
- Move logo to corner in wallpapers that have it in center
  Resolves: #1706793

* Mon Jun 17 2019 Ray Strode <rstrode@redhat.com> - 80.8-1
- Fix black spot in one of the backgrounds
  Resolves: #1684106
- Add missing 2560x1600 8-abstract-light background
  Resolves: #1692309
- letter box instead of crop backgrounds when there's no
  good aspect ratio
  Related: #1720610

* Wed Jan 30 2019 Ray Strode <rstrode@redhat.com> - 80.7-1
- Put in place new logos and wallpapers
  Resolves: #1637686

* Mon Jan 14 2019 Ray Strode <rstrode@redhat.com> - 80.6-1
- Update anaconda sidebar and top bar
  Resolves: #1638383

* Mon Oct 15 2018 Ray Strode <rstrode@redhat.com> - 80.5-1
- Another wallpaper content update
  Related: #1636822

* Mon Oct 15 2018 Thomas Woerner <twoerner@redhat.com> - 80.4-1
- Moved ipa/idm logos and background to redhat-logos-ipa
  Related: #1626507

* Wed Oct 10 2018 Ray Strode <rstrode@redhat.com> - 80.3-1
- Make night time pattern lighter
  Resolves: #1628092
- Remove Alpha from logos
  Resolves: #1637446
- Remove Alpha from wallpapers
  Resolves: #1636822

* Tue Sep 18 2018 Kalev Lember <klember@redhat.com> - 80.2-1
- Install an override for GNOME lock screen background
- Resolves: #1630296

* Fri Sep 07 2018 Stephen Gallagher <sgallagh@redhat.com> - 80.1-2
- Separate desktop backgrounds into their own subpackage
- Correct the description to match the license terms
- Drop vestiges of fedora-logos

* Thu Aug 30 2018 Ray Strode <rstrode@redhat.com> - 80.1-1
- Add new plymouth branding
  Resolves: #1623525

* Mon Jul 16 2018 Ray Strode <rstrode@redhat.com> - 80.0-2
- Drop the BR on png optimizers we don't use
  Related: #1593166

* Thu Jun 28 2018 David Cantrell <dcantrell@redhat.com> - 80.0-1
- Drop the BR on libicns-utils and other cleanups
  Resolves: rhbz#1596389

* Thu May  3 2018 Jan Horak <jhorak@redhat.com> - 79.0.6-2
- Removed ImageMagick buildrequire as no longer needed

* Tue Apr 10 2018 Ray Strode <rstrode@redhat.com> - 79.0.6-1
- more background updates

* Wed Nov 29 2017 Ray Strode <rstrode@redhat.com> - 79.0.5-1
- deduplicate patterncity wallpapers

* Wed Nov 29 2017 Ray Strode <rstrode@redhat.com> - 79.0.4-1
- more background updates

* Wed Nov 29 2017 Ray Strode <rstrode@redhat.com> - 79.0.3-1
- Add control-center wallpaper metadata files
- Add latest update for backgrouns from jimmac

* Tue Nov 28 2017 Ray Strode <rstrode@redhat.com> - 79.0.2-1
- Add update for backgrounds from jimmac

* Tue Nov 21 2017 Ray Strode <rstrode@redhat.com> - 79.0.1-1
- Update artwork with first cut alpha content
- Drop obsolete bits of package like KDE artwork and references
  to Bluecurve

* Fri Nov  3 2017 Ray Strode <rstrode@redhat.com> - 79.0.0-1
- Merge in latest changes from fedora-logos and rhel7 redhat-logos

* Fri Sep 22 2017 Troy Dawson <tdawson@redhat.com> - 79.0.0-0.1
- Initial build for rhel-8
- Imported from generic-logos 18.0.0-4

* Mon Apr 11 2016 Ray Strode <rstrode@redhat.com> - 70.0.3-6
- fix Source line
  Related: #1325373

* Mon Apr 11 2016 Ray Strode <rstrode@redhat.com> - 70.0.3-5
- new developers³ banner
  Resolves: #1325373

* Mon Mar 03 2014 Than Ngo <than@redhat.com> - 70.0.3-4
- broken 24x24 icon fix

* Mon Feb 24 2014 Than Ngo <than@redhat.com> - 70.0.3-3
- add backgrounds to KDE wallpaper, bz#1068687

* Mon Feb 17 2014 Ray Strode <rstrode@redhat.com> 70.0.3-2
- Add default.xml back to the build
  Related: #1053025

* Mon Feb 17 2014 Ray Strode <rstrode@redhat.com> 70.0.3-1
- Shrink supplemental backgrounds by making them jpegs instead
  of pngs.
  Related: #1053025 1065938

* Tue Feb 11 2014 Ray Strode <rstrode@redhat.com> 70.0.2-1
- Add supplemental backgrounds
  Resolves: #1053025

* Tue Feb 11 2014 Ray Strode <rstrode@redhat.com> 70.0.1-1
- Add anaconda branding
  Related: #1045250 1063197

* Tue Feb 11 2014 Ray Strode <rstrode@redhat.com> 70.0.0-1
- Add firstboot stuff
  Resolves: #1058397

* Mon Feb 10 2014 Ray Strode <rstrode@redhat.com> 69.1.15-1
- Drop bootloader stuff
  Resolves: #1063246

* Wed Jan 22 2014 Ray Strode <rstrode@redhat.com> 69.1.14-1
- Improve /usr/share/pixmaps/fedora-logo.png for control-center
  Related: #1053000

* Wed Jan 22 2014 Ray Strode <rstrode@redhat.com> 69.1.13-1
- more branding updates
  Related: #1042818

* Tue Jan 21 2014 Ray Strode <rstrode@redhat.com> 69.1.12-1
- Add back a login screen logo
  Resolves: #1042818

* Tue Jan 21 2014 Ray Strode <rstrode@redhat.com> 69.1.11-1
- Make the (R) symbol bigger in the panel logo
  Resolves: #1052978

* Wed Jan  8 2014 David Shea <dshea@redhat.com> - 69.1.10-1
- Added release notes images for anaconda
  Resolves: #1049655

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 69.1.9-2
- Mass rebuild 2013-12-27

* Mon Nov 04 2013 Ray Strode <rstrode@redhat.com> 69.1.9-1
- Fix file conflict
  Resolves: #1025559

* Fri Oct 25 2013 Ray Strode <rstrode@redhat.com> 69.1.8-1
- Update plymouth theme
  Related: #1002219

* Mon Oct 21 2013 Ray Strode <rstrode@redhat.com> 69.1.6-1
- Update syslinux background to black
  Resolves: #1003873
- Prune unused images from anaconda/ after talking to #anaconda

* Wed Jul 31 2013 Ray Strode <rstrode@redhat.com> 69.1.5-1
- Update header image
  Resolves: #988066

* Tue Jul 30 2013 Than Ngo <than@redhat.com> - 69.1.4-1
- cleanup kde theme

* Wed Jul 17 2013 Matthias Clasen <mclasen@redhat.com> 69.1.3-3
- Drop unused old background (#918324)

* Thu Jul 11 2013 Ray Strode <rstrode@redhat.com> 69.1.3-2
- Drop fedora.icns (It brings in an undesirable dependency,
  and we don't support the platform it's designed for
  anyway)

* Wed Apr 24 2013 Than Ngo <than@redhat.com> - 69.1.3-1
- Resolves: #949670, rendering issue in kdm theme
- fix background in kdm theme

* Mon Jan 21 2013 Ray Strode <rstrode@redhat.com> 69.1.2-1
- background reversion fixes.
  Resolves: #884841

* Thu Jan 17 2013 Ray Strode <rstrode@redhat.com> 69.1.1-1
- Revert to earlier header image
  Resolves: #884841

* Wed Nov 14 2012 Ray Strode <rstrode@redhat.com> 69.1.0-1
- Update to latest backgrounds
  Resolves: #860311
- Drop Fedora icon theme
  Resolves: #800475

* Fri Nov  9 2012 Matthias Clasen <mclasen@redhat.com> 69.0.9-3
- Fix a typo in the default background override

* Wed Oct 31 2012 Tomas Bzatek <tbzatek@redhat.com> 69.0.9-2
- Provide the virtual system-backgrounds-gnome for gnome-desktop3

* Tue Oct 30 2012 Ray Strode <rstrode@redhat.com> 69.0.9-1
- Install default background override file here, now that
  desktop-backgrounds-gnome is gone

* Tue Oct 30 2012 Than Ngo <than@redhat.com> - 69.0.8-1
- bz#835922, missing kde wallpaper

* Mon Jun 18 2012 Ray Strode <rstrode@redhat.com> 69.0.7-1
- Update background to RHEL7 branding
  Related: #833137

* Thu May 10 2012 Than Ngo <than@redhat.com> - 69.0.6-1
- add missing kde desktoptheme

* Tue Mar 06 2012 Than Ngo <than@redhat.com> - 69.0.5-1
- bz#798621, add missing kde themes

* Tue Feb 07 2012 Ray Strode <rstrode@redhat.com> 69.0.4-1
- More syslinux splash updates
  Related: #786885

* Fri Feb 03 2012 Ray Strode <rstrode@redhat.com> 69.0.3-1
- Three's a charm?
  Resolves: #786885

* Thu Feb 02 2012 Ray Strode <rstrode@redhat.com> 69.0.2-1
- syslinux splash updates
  Resolves: #786885

* Thu Jan 26 2012 Ray Strode <rstrode@redhat.com> 69.0.1-1
- More updates (problems spotted by stickster)

* Tue Nov 15 2011 Ray Strode <rstrode@redhat.com> - 69.0.0-1
- Resync from fedora-logos-16.0.2-1

* Wed Aug 25 2010 Ray Strode <rstrode@redhat.com> 60.0.14-1
- Update description and COPYING file
  Resolves: #627374

* Fri Jul 30 2010 Ray Strode <rstrode@redhat.com> 60.0.13-1
- Add header image
  Related: #558608

* Fri Jul 16 2010 Ray Strode <rstrode@redhat.com> 60.0.12-1
- Drop glow theme
  Resolves: #615251

* Tue Jun 15 2010 Matthias Clasen <mclasen@redhat.com> 60.0.11-2
- Silence gtk-update-icon-cache in %%post and %%postun
Resolves: #589983

* Fri May 21 2010 Ray Strode <rstrode@redhat.com> 60.0.11-1
- Update anaconda artwork based on feedback
  Resolves: #594825

* Tue May 11 2010 Than Ngo <than@redhat.com> - 60.0.10-1
- update ksplash theme to match the latest splash

* Thu May 06 2010 Ray Strode <rstrode@redhat.com> 60.0.9-1
- Add back grub.splash
  Resolves: 589703
- Add extra frame to plymouth splash
  Related: #558608

* Wed May 05 2010 Ray Strode <rstrode@redhat.com> 60.0.8-1
- Add large logo for compiz easter egg
  Resolves: #582411
- Drop Bluecurve
  Related: #559765
- Install logo icons in System theme
  Related: #566370

* Tue May 04 2010 Ray Strode <rstrode@redhat.com> 60.0.7-1
- Rename firstboot theme to RHEL
  Resolves: #566173
- Add new plymouth artwork
  Related: #558608
- Update backgrounds
- Update anaconda
- Drop gnome-splash
- Drop empty screensaver dir
  Resolves: #576912
- Drop grub splash at request of artists

* Thu Apr 22 2010 Than Ngo <than@redhat.com> - 60.0.6-1
- fix many cosmetic issues in kdm/ksplash theme

* Mon Apr 12 2010 Ray Strode <rstrode@redhat.com> 60.0.5-3
Resolves: #576912
- Readd default.xml

* Fri Apr 09 2010 Ray Strode <rstrode@redhat.com> 60.0.5-2
- Make the upgrade path from alpha a little smoother
  Resolves: #580475

* Wed Apr 07 2010 Ray Strode <rstrode@redhat.com> 60.0.5-1
Resolves: #576912
- Update wallpapers

* Tue Feb 23 2010 Ray Strode <rstrode@redhat.com> 60.0.4-3
Resolves: #559695
- Drop xpm symlinking logic
- hide anaconda image dir behind macro

* Wed Feb 17 2010 Ray Strode <rstrode@redhat.com> 60.0.4-1
Resolves: #565886
- One more update to the KDE artwork
- Revert firstboot theme rename until later since compat link
  is causing problems.

* Wed Feb 17 2010 Ray Strode <rstrode@redhat.com> 60.0.3-1
Resolves: #565886
- Put backgrounds here since they're "trade dress"
- Rename firstboot theme from leonidas to RHEL (with compat link)

* Wed Feb 17 2010 Jaroslav Reznik <jreznik@redhat.com> 60.0.2-1
- KDE theme merged into redhat-logos package
- updated license (year in copyright)

* Fri Feb 05 2010 Ray Strode <rstrode@redhat.com> 60.0.1-3
Resolves: #559695
- spec file cleanups

* Mon Jan 25 2010 Than Ngo <than@redhat.com> - 60.0.1-2
- drop useless leonidas in KDE

* Fri Jan 22 2010 Ray Strode <rstrode@redhat.com> 60.0.1-1
Resolves: #556906
- Add updated artwork for Beta

* Thu Jan 21 2010 Matthias Clasen <mclasen@redhat.com> 60.0.0-2
- Remove a non-UTF-8 char from the spec
 
* Wed Jan 20 2010 Ray Strode <rstrode@redhat.com> 60.0.0-1
Resolves: #556906
- Add bits from glow plymouth theme

* Wed Jan 20 2010 Ray Strode <rstrode@redhat.com> - 11.90.4-1
Resolves: #556906
- Update artwork for Beta

* Tue Dec 08 2009 Dennis Gregorovic <dgregor@redhat.com> - 11.90.3-1.1
- Rebuilt for RHEL 6

* Mon Jun 01 2009 Ray Strode <rstrode@redhat.com> - 11.90.3-1
- remove some of the aliasing from the charge theme

* Fri May 29 2009 Ray Strode <rstrode@redhat.com> - 11.90.2-1
- Drop backgrounds again because they don't actually contain logos

* Fri May 29 2009 Ray Strode <rstrode@redhat.com> - 11.90.1-1
- Install new backgrounds

* Fri May 29 2009 Ray Strode <rstrode@redhat.com> - 11.90.0-2
- Rebuild using tarball dist from cvs

* Thu May 28 2009 Ray Strode <rstrode@redhat.com> - 11.90.0-1
- Update artwork for RHEL 6 alpha

* Thu Jan  4 2007 Jeremy Katz <katzj@redhat.com> - 4.9.16-1
- Fix syslinux splash conversion, Resolves: #209201

* Fri Dec  1 2006 Matthias Clasen <mclasen@redhat.com> - 4.9.15-1
- Readd rhgb/main-logo.png, Resolves: #214868

* Tue Nov 28 2006 David Zeuthen <davidz@redhat.com> - 4.9.14-1
- Don't include LILO splash. Resolves: #216748
- New syslinux-splash from Diana Fong. Resolves: #217493

* Tue Nov 21 2006 David Zeuthen <davidz@redhat.com> - 4.9.13-1
- Make firstboot/splash-small.png completely transparent
- Fix up date for last commit
- Resolves: #216501

* Mon Nov 20 2006 David Zeuthen <davidz@redhat.com> - 4.9.12-1
- New shadowman gdm logo from Diana Fong (#216370)

* Wed Nov 15 2006 David Zeuthen <davidz@redhat.com> - 4.9.10-1
- New shadowman logos from Diana Fong (#215614)

* Fri Nov 10 2006 Than Ngo <than@redhat.com> - 4.9.9-1
- add missing KDE splash (#212130)

* Wed Oct 25 2006 David Zeuthen <davidz@redhat.com> - 4.9.8-1
- Add new shadowman logos (#211837)

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 4.9.7-1 
- Include the xml file in the tarball

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 4.9.6-1
- Add names for the default background (#211556)

* Tue Oct 17 2006 Matthias Clasen <mclasen@redhat.com> - 4.9.5-1
- Update the url pointing to the trademark policy (#187124)

* Thu Oct  5 2006 Matthias Clasen <mclasen@redhat.com> - 4.9.4-1
- Fix some colormap issues in the syslinux-splash (#209201)

* Wed Sep 20 2006 Ray Strode <rstrode@redhat.com> - 4.9.2-1
- ship new artwork from Diana Fong for login screen

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.8-1
- Fix packager to dist the xml background file

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.7-1
- Add background xml file for the new backgrounds
- Add po directory for translating the background xml

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.6-1
- Add new RHEL graphics

* Fri Aug 25 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.5-1
- Modify the anaconda/splash.png file to say Beta instead of Alpha

* Tue Aug 01 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.4-1
- Add firstboot-left to the firstboot images

* Fri Jul 28 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.3-1
- Add attributions to the background graphics metadata
- Add a 4:3 asspect ratio version of the default background graphic

* Thu Jul 27 2006 John (J5) Palmieri <johnp@redhat.com> - 1.2.2-1
- Add default backgrounds

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 1.2.1-1
- Add system lock dialog

* Thu Jun 15 2006 Jeremy Katz <katzj@redhat.com> - 1.2.0-1
- alpha graphics

* Wed Aug  3 2005 David Zeuthen <davidz@redhat.com> - 1.1.26-1
- Add russian localisation for rnotes (#160738)

* Thu Dec  2 2004 Jeremy Katz <katzj@redhat.com> - 1.1.25-1
- add rnotes

* Fri Nov 19 2004 Alexander Larsson <alexl@redhat.com> - 1.1.24-1
- Add rhgb logo (#139788)

* Mon Nov  1 2004 Alexander Larsson <alexl@redhat.com> - 1.1.22-1
- Move rh logo from redhat-artwork here (#137593)

* Fri Oct 29 2004 Alexander Larsson <alexl@redhat.com> - 1.1.21-1
- Fix alignment of gnome splash screen (#137360)

* Fri Oct  1 2004 Alexander Larsson <alexl@redhat.com> - 1.1.20-1
- New gnome splash

* Tue Aug 24 2004 Jeremy Katz <katzj@redhat.com> - 1.1.19-1
- update firstboot splash

* Sat Jun  5 2004 Jeremy Katz <katzj@redhat.com> - 1.1.18-1
- provides: system-logos

* Thu Jun  3 2004 Jeremy Katz <katzj@redhat.com> - 1.1.17-1
- add anaconda bits

* Tue Mar 23 2004 Alexander Larsson <alexl@redhat.com> 1.1.16-1
- fix the logos in the gdm theme

* Fri Jul 18 2003 Havoc Pennington <hp@redhat.com> 1.1.15-1
- build new stuff from garrett

* Wed Feb 26 2003 Havoc Pennington <hp@redhat.com> 1.1.14-1
- build new stuff in cvs

* Mon Feb 24 2003 Jeremy Katz <katzj@redhat.com> 1.1.12-1
- updated again
- actually update the grub splash

* Fri Feb 21 2003 Jeremy Katz <katzj@redhat.com> 1.1.11-1
- updated splash screens from Garrett

* Tue Feb 18 2003 Havoc Pennington <hp@redhat.com> 1.1.10-1
- move in a logo from gdm theme #84543

* Mon Feb  3 2003 Havoc Pennington <hp@redhat.com> 1.1.9-1
- rebuild

* Wed Jan 15 2003 Brent Fox <bfox@redhat.com> 1.1.8-1
- rebuild for completeness

* Mon Dec 16 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Thu Sep  5 2002 Havoc Pennington <hp@redhat.com>
- add firstboot images to makefile/specfile
- add /usr/share/pixmaps stuff
- add splash screen images
- add COPYING

* Thu Sep  5 2002 Jeremy Katz <katzj@redhat.com>
- add boot loader images

* Thu Sep  5 2002 Havoc Pennington <hp@redhat.com>
- move package to CVS

* Tue Jun 25 2002 Owen Taylor <otaylor@redhat.com>
- Add a shadowman-only derived from redhat-transparent.png

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 31 2001 Owen Taylor <otaylor@redhat.com>
- Fix alpha channel in redhat-transparent.png

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com>
- Add %%defattr

* Mon Jun 19 2000 Owen Taylor <otaylor@redhat.com>
- Add version of logo for embossing on the desktop

* Tue May 16 2000 Preston Brown <pbrown@redhat.com>
- add black and white version of our logo (for screensaver).

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- rebuild for new description.

* Sat Sep 25 1999 Bill Nottingham <notting@redhat.com>
- different.

* Mon Sep 13 1999 Preston Brown <pbrown@redhat.com>
- added transparent mini and 32x32 round icons

* Sat Apr 10 1999 Michael Fulbright <drmike@redhat.com>
- added rhad logos

* Thu Apr 08 1999 Bill Nottingham <notting@redhat.com>
- added smaller redhat logo for use on web page

* Wed Apr 07 1999 Preston Brown <pbrown@redhat.com>
- added transparent large redhat logo

* Tue Apr 06 1999 Bill Nottingham <notting@redhat.com>
- added mini-* links to make AnotherLevel happy

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- added copyright

* Tue Mar 30 1999 Michael Fulbright <drmike@redhat.com>
- added 48 pixel rounded logo image for gmc use

* Mon Mar 29 1999 Preston Brown <pbrown@redhat.com>
- package created
