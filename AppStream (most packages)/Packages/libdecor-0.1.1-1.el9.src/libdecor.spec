Name:           libdecor
Version:        0.1.1
Release:        1%{?dist}
Summary:        Wayland client side decoration library

License:        MIT
URL:            https://gitlab.gnome.org/jadahl/libdecor
Source:         %{url}/uploads/ee5ef0f2c3a4743e8501a855d61cb397/libdecor-0.1.1.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)

%description
Libdecor provides a small helper library for providing client side decoration
to Wayland clients.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Ddemo=false
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libdecor-0.so.0*
%dir %{_libdir}/libdecor/
%dir %{_libdir}/libdecor/plugins-1
%{_libdir}/libdecor/plugins-1/libdecor-cairo.so

%files devel
%{_includedir}/libdecor-0/
%{_libdir}/libdecor-0.so
%{_libdir}/pkgconfig/libdecor-0.pc


%changelog
* Sun Nov 06 2022 Neal Gompa <ngompa@centosproject.org> - 0.1.1-1
- Update to 0.1.1
  Resolves: rhbz#2140414

* Tue Dec 07 2021 Wim Taymans <wtaymans@redhat.com> - 0.1.0-3
- Version bump for rebuild

* Tue Dec 07 2021 Wim Taymans <wtaymans@redhat.com> - 0.1.0-2
- Version bump for resync

* Fri Jul 23 2021 Jonas Ådahl <jadahl@redhat.com> - 0.1.0-1
- Initial Fedora packaging
