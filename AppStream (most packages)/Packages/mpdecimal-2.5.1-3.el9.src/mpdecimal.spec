# versioned documentation for old releases
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           mpdecimal
Version:        2.5.1
Release:        3%{?dist}
Summary:        Library for general decimal arithmetic
License:        BSD

URL:            http://www.bytereef.org/mpdecimal/index.html
Source0:        http://www.bytereef.org/software/mpdecimal/releases/mpdecimal-%{version}.tar.gz
Source1:        http://speleotrove.com/decimal/dectest.zip

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
The package contains a library libmpdec implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package -n %{name}++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Library for general decimal arithmetic (C++)

%description -n %{name}++
The package contains a library libmpdec++ implementing General Decimal
Arithmetic Specification. The specification, written by Mike Cowlishaw from
IBM, defines a general purpose arbitrary precision data type together with
rigorously specified functions and rounding behavior.

%package        devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}++%{?_isa} = %{version}-%{release}
Summary:        Development headers for mpdecimal library

%description devel
The package contains development headers for the mpdecimal library.

%package        doc
Summary:        Documentation for mpdecimal library
# docs is FBSDDL
# bundles underscore.js: MIT
# bundles jquery: MIT
# jquery bundles sizzle.js: MIT
License:        FBSDDL and MIT
BuildArch:      noarch
Provides:       bundled(js-jquery) = 3.4.1
Provides:       bundled(js-underscore) = 1.3.1

%description doc
The package contains documentation for the mpdecimal library.

%prep
%autosetup
unzip -d tests/testdata %{SOURCE1}

%build
# Force -ffat-lto-objects so that configure tests are assembled which
# is required for ASM configure tests.  -ffat-lto-objects is the default
# for F33, but will not be the default in F34
#define _lto_cflags -flto=auto -ffat-lto-objects

%configure
make %{?_smp_mflags}

%check
make check

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.a

# license will go into dedicated directory
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE.txt

# relocate documentation if versioned documentation is used
if [ "%{_pkgdocdir}" != "%{_docdir}/%{name}" ]; then
  install -d -m 0755 %{buildroot}%{_pkgdocdir}
  mv -v %{buildroot}%{_docdir}/%{name}/* %{buildroot}%{_pkgdocdir}/
fi

%files
%license LICENSE.txt
%{_libdir}/libmpdec.so.%{version}
%{_libdir}/libmpdec.so.3

%files -n %{name}++
%{_libdir}/libmpdec++.so.%{version}
%{_libdir}/libmpdec++.so.3

%files devel
%{_libdir}/libmpdec.so
%{_libdir}/libmpdec++.so
%{_includedir}/mpdecimal.h
%{_includedir}/decimal.hh

%files doc
%license doc/LICENSE.txt
%doc %{_pkgdocdir}

%ldconfig_scriptlets

%changelog
* Thu Jan 19 2023 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-3
- Split libmpdec++ into a mpdecimal++ subpackage
- This prevents packages only using the libmpdec library from transitively depending on libstdc++

* Wed Jan 18 2023 Charalampos Stratakis <cstratak@redhat.com> - 2.5.1-2
- Fix license information

* Tue Jan 17 2023 Charalampos Stratakis <cstratak@redhat.com> - 2.5.1-1
- Import into RHEL
- Fedora contributions by:
      Charalampos Stratakis <cstratak@redhat.com>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Jan Vcelak <jvcelak@fedoraproject.org>
      Jaroslav Škarvada <jskarvad@redhat.com>
      Jeff Law <law@redhat.com>
      Lukas Zachar <lzachar@redhat.com>
      Miro Hrončok <miro@hroncok.cz>
      Tom Stellard <tstellar@redhat.com>
