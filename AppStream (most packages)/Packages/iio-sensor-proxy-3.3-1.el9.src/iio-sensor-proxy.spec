Name:           iio-sensor-proxy
Version:        3.3
Release:        1%{?dist}
Summary:        IIO accelerometer sensor to input device proxy

License:        GPLv3+
URL:            https://github.com/hadess/iio-sensor-proxy
Source0:        https://gitlab.freedesktop.org/hadess/iio-sensor-proxy/uploads/83c63a8dd585ef6d1568791369dc8877/iio-sensor-proxy-3.3.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  systemd
%{?systemd_requires}

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%autosetup

%build
%meson -Dgtk_doc=true -Dgtk-tests=false
%meson_build

%install
%meson_install

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/monitor-sensor
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_udevrulesdir}/*-%{name}.rules
%{_sysconfdir}/dbus-1/system.d/net.hadess.SensorProxy.conf

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Wed Aug 18 2021 Bastien Nocera <bnocera@redhat.com> - 3.3-1
+ iio-sensor-proxy-3.3-1
- Update to 3.3
- Resolves: rhbz#1993769

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.1-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jun 14 2021 Bastien Nocera <bnocera@redhat.com> - 3.1-1
+ iio-sensor-proxy-3.1-1
- Update to 3.1
- Resolves: rhbz#1971625

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.0-4
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Bastien Nocera <bnocera@redhat.com> - 3.0-1
+ iio-sensor-proxy-3.0-1
- Update to 3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Bastien Nocera <bnocera@redhat.com> - 2.8-1
+ iio-sensor-proxy-2.8-1
- Update to 2.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Bastien Nocera <bnocera@redhat.com> - 2.7-1
+ iio-sensor-proxy-2.7-1
- Update to 2.7 (#1709812)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Bastien Nocera <bnocera@redhat.com> - 2.5-1
+ iio-sensor-proxy-2.5-1
- Update to 2.5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-3
- Add BuildRequires: make/gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Bastien Nocera <bnocera@redhat.com> - 2.4-1
+ iio-sensor-proxy-2.4-1
- Update to 2.4

* Wed Sep 20 2017 Bastien Nocera <bnocera@redhat.com> - 2.3-1
+ iio-sensor-proxy-2.3-1
- Update to 2.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2-1
- Update to 2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.1-1
- Update to 2.1

* Mon Dec 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.0-1
- Update to 2.0

* Fri Nov 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3-2
- Don't use hwdb update macro
- Trivial fixes

* Sat Sep 17 2016 Bastien Nocera <bnocera@redhat.com> - 1.3-1
- Update to 1.3

* Tue Sep 06 2016 Bastien Nocera <bnocera@redhat.com> - 1.2-1
- Update to 1.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 1.1-1
- Update to 1.1
- Add -docs subpackage

* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-6
- Fix udev rule (RHBZ #1234744)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-4
- use real license (GPLv3+)

* Sun May 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-3
- Fix license tag
- Disable silent building

* Sat May 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-2
- Use _udevrules dir instead of custom detecting rules dir

* Sat May 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0-1
- Initial package
