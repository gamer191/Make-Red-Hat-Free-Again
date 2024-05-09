Name:		python-libevdev
Version:	0.9
Release:	4%{?dist}
Summary:	Python bindings to the libevdev evdev device wrapper library

License:	MIT
URL:		https://pypi.python.org/pypi/libevdev/
Source0:	https://gitlab.freedesktop.org/libevdev/python-libevdev/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%package -n	python3-libevdev
Summary:	Python bindings to the libevdev evdev device wrapper library

BuildRequires:	python3-devel python3-setuptools
Requires:	libevdev

%{?python_provide:%python_provide python3-libevdev}

%description -n	python3-libevdev
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%files -n	python3-libevdev
%license COPYING
%{python3_sitelib}/libevdev/
%{python3_sitelib}/libevdev-%{version}-py*.egg-info

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.9-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri May 14 2021 Peter Hutterer <peter.hutterer@redhat.com> 0.9-3
- Import from Fedora (#1957087)

