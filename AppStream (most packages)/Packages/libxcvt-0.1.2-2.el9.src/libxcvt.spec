%if !0%{?rhel}
%global with_cvt   1
%endif

Name:      libxcvt
Version:   0.1.2
Release:   2%{?dist}
Summary:   VESA CVT standard timing modelines generator

URL:       https://gitlab.freedesktop.org/xorg/lib/libxcvt/
Source0:   https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz

License:   MIT

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: meson

%description
libxcvt is a library providing a standalone version of the X server
implementation of the VESA CVT standard timing modelines generator.

%package devel
Summary: Development package
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?with_cvt}
%package -n cvt
Summary: Command line tool to calculate VESA CVT mode lines
Conflicts: xorg-x11-server-Xorg < 1.21

%description -n cvt
A standalone version of the command line tool cvt copied from the Xorg
implementation and is meant to be a direct replacement to the version
provided by the Xorg server.
%endif

%prep
%autosetup -S git_am -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%if !0%{?with_cvt}
rm -vf %{buildroot}%{_bindir}/cvt
rm -vf %{buildroot}%{_mandir}/man1/cvt.1*
%endif

%files
%doc COPYING
%{_libdir}/libxcvt.so.*

%files devel
%{_libdir}/pkgconfig/libxcvt.pc
%dir %{_includedir}/libxcvt
%{_includedir}/libxcvt/*.h
%{_libdir}/libxcvt.so

%if 0%{?with_cvt}
%files -n cvt
%{_bindir}/cvt
%{_mandir}/man1/cvt.1*
%endif

%changelog
* Thu Dec 22 2022 Olivier Fourdan <ofourdan@redhat.com> - 0.1.2-2
- Add explicit package version requirement for the devel package
  for rpminspect.

* Tue Jul 19 2022 Olivier Fourdan <ofourdan@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Olivier Fourdan <ofourdan@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Thu Jul 8 2021 Olivier Fourdan <ofourdan@redhat.com> - 0.1.0-1
- Initial import (#1980342)
