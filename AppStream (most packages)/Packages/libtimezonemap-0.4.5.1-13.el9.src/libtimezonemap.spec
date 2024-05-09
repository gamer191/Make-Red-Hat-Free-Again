Name:           libtimezonemap
Version:        0.4.5.1
Release:        13%{?dist}
Summary:        Time zone map widget for Gtk+

License:        GPLv3
URL:            https://launchpad.net/timezonemap
Source0:        https://github.com/dashea/timezonemap/archive/%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=2097831
Patch0:         0001-Remove-regions-from-the-map-2097831.patch

BuildRequires:  glib2-devel >= 2.26
BuildRequires:  gtk3-devel >= 3.1.4
BuildRequires:  json-glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gnome-common
BuildRequires:  libsoup-devel >= 2.42.0
BuildRequires:  librsvg2-devel
BuildRequires: make

%description
libtimezonemap is a time zone map widget for Gtk+. The widget displays a world
map with a highlighted region representing the selected time zone, and the
location can be changed by clicking on the map.

This library is a fork of the of the code from gnome-control-center's datetime
panel, which was itself a fork of Ubiquity's timezone map.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
libtimezonemap is a time zone map widget for Gtk+. This package contains header
files used for building applications that use %{name}.

%prep
%autosetup -n timezonemap-%{version} -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc README TODO
%{_libdir}/libtimezonemap.so.*
%{_libdir}/girepository-1.0/TimezoneMap-1.0.typelib
%{_datadir}/%{name}

%files devel
%{_libdir}/libtimezonemap.so
%{_libdir}/pkgconfig/timezonemap.pc
%{_includedir}/timezonemap
%{_datadir}/gir-1.0/TimezoneMap-1.0.gir
%{_datadir}/glade/catalogs/TimezoneMap.xml

%changelog
* Mon Jan 15 2024 Jiri Konecny <jkonecny@redhat.com> - 0.4.5.1-13
- Add libtimezonemap-devel to CRB
  Resolves: RHEL-13916

* Wed Jun 22 2022 Jiri Konecny <jkonecny@redhat.com> - 0.4.5.1-12
- Remove regions from the map
  Resolves: rhbz#2097831

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.5.1-11
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.5.1-10
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5.1-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 20 2017 David Shea <dshea@redhat.com> - 0.4.5.1-1
- Fix SVG visibility (jkonecny) (#1502915)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 David Shea <dshea@redaht.com> - 0.4.5-6
- Removed tests

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 David Shea <dshea@redhat.com> - 0.4.5-4
- Bring back the setting of $TZ (#1367647)

* Wed Jun 29 2016 David Shea <dshea@redhat.com> - 0.4.5-3
- Render the map directly from SVG (#1335158)
- Fix memory leaks in tz.c
- Fix an invalid memory access
- Do not modify TZ in the process environment
- Move all data files to /usr/share/libtimezonemap from .../libtimezonemap/ui
- Add extra city data so all timezone offsets are clickable
- Move Venezuela from -04:30 to -04:00
- Fix the conversion of points just west of 180 longitude
- Remove the out-of-date Olson map data
- Update the "backward" file
- Improve the location selected when setting the timezone by name (#1322648)
- Remove an extra line in the +10:00 layer
- Move Chile back an hour

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 David Shea <dshea@redhat.com> - 0.4.5-1
- Update the map images

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May  8 2015 David Shea <dshea@redhat.com> - 0.4.4-1
- Fixes for LP#1440157:
  Port to libsoup directly for geoname results
  Fix some memory leaks
  Do not reuse GCancellables
- Upstream merges of SVG update and constrained location cycles

* Fri May  1 2015 David Shea <dshea@redhat.com> - 0.4.2-6
- Updated the time zone map images
- Updated the city data from geonames.org
- Fix a memory leak and potential crash with the locations list
- Cycle through a smaller list of map locations on repeated clicks

* Wed Jan 28 2015 David Shea <dshea@redhat.com> - 0.4.2-5
- Use %%license for the license file

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.2-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  2 2014 David Shea <dshea@redhat.com> - 0.4.2-1
- New upstream release libtimezonemap-0.4.2

* Mon Dec  2 2013 David Shea <dshea@redhat.com> - 0.4.1-4
- Merge fixes from lp:timezonemap
- Add cc-timezone-location.h to timezonemapincludes_HEADERS so it gets installed (iain.lane)
- Set en_name correctly (iain.lane)
- Don't call g_type_init() on glib >= 2.35; it's deprecated (iain.lane)

* Wed Nov 27 2013 David Shea <dshea@redhat.com> - 0.4.1-3
- Added a glade catalog file (dshea)

* Tue Nov 26 2013 David Shea <dshea@redhat.com> - 0.4.1-2
- Make whitespace and indentation consistent (iain.lane@canonical.com)
- Switched to a git-formatted patch for the FSF address to make things easier
  for me to track (dshea)
- Create local copies of string properties. (dshea)
- Moved CcTimezoneLocation into its own file. (dshea)
- Don't close a NULL file pointer. (dshea)
- Turn on and fix g-ir-scanner warnings. (dshea)
- Added a .bzrignore file to ignore all the files generated by the build. (dshea)
- Ignore the INSTALL file (dshea)
- Added a function to clear the location set for a CcTimezoneMap (dshea)
- Allow the timezone highlight to be manually set separately from the location. (dshea)

* Thu Nov 14 2013 David Shea <dshea@redhat.com> - 0.4.1-1
- Initial version
