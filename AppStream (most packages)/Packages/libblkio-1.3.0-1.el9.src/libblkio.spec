Version:       1.3.0
Summary:       Block device I/O library
Name:          libblkio
Release:       1%{?dist}
URL:           https://gitlab.com/libblkio/libblkio
Source0:       %{url}/-/archive/v%{version}/libblkio-v%{version}.tar.bz2
Source1:       libblkio-vendor-v%{version}.tar.bz2
License:       (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSD-3-Clause) AND BSD-3-Clause

# Basic build requirements.
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: meson
BuildRequires: rustfmt
BuildRequires: cargo
BuildRequires: rust
BuildRequires: python3-docutils
BuildRequires: pkgconf


%description
libblkio is a library for high-performance block device I/O with
support for multi-queue devices. A C API is provided so that
applications can use the library from most programming languages.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}


%description devel
This package contains development tools for %{name}.


%prep
%autosetup -n libblkio-v%{version} -p1 -b 1
sed -e 's/--locked/--offline/' -i src/cargo-build.sh


%build
%{meson}
%{meson_build}


%install
%{meson_install}


%files
%license LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%doc README.rst
%{_libdir}/libblkio.so.1{,.*}


%files devel
%license LICENSE-APACHE LICENSE-MIT LICENSE.crosvm
%doc README.rst
%{_includedir}/blkio.h
%{_libdir}/libblkio.so
%{_libdir}/pkgconfig/blkio.pc
%{_mandir}/man3/blkio.3*


%changelog
* Thu May 11 2023 Stefan Hajnoczi <stefanha@redhat.com> - 1.3.0-1
- Update to 1.3.0, which simplifies the license expression due to crate
  dependency changes.

* Wed Apr 26 2023 Stefan Hajnoczi <stefanha@redhat.com> - 1.2.2-2
- Remove %autosetup -Sgit as it's not used and the build could break because BuildRequires: git-core was missing

* Tue Apr 11 2023 Stefan Hajnoczi <stefanha@redhat.com> - 1.2.2-1
- Import Fedora rpm 1.2.2-4 spec file with license updates (https://src.fedoraproject.org/rpms/libblkio/pull-request/1)
