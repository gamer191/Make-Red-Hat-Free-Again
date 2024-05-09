%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# RHEL: Tests disabled due to missing deps
%bcond_with tests

%global srcname cryptography

Name:           python%{python3_pkgversion}-%{srcname}
Version:        37.0.2
Release:        6%{?dist}
Summary:        PyCA's cryptography library

# We bundle various crates with cryptography which is dual licensed
# under the ASL 2.0 and BSD-3-Clause, as well as the Python license
# for the OS random engine derived by CPython.

# Inflector: BSD
# aliasable: MIT
# asn1: BSD
# asn1_derive: BSD
# autocfg: MIT or ASL 2.0
# base64: MIT or ASL 2.0
# cfg-if: MIT or ASL 2.0
# chrono: MIT or ASL 2.0
# indoc: MIT or ASL 2.0
# indoc-impl: MIT or ASL 2.0
# instant: BSD
# lazy_static: MIT or ASL 2.0
# libc: MIT or ASL 2.0
# lock_api: MIT or ASL 2.0
# num-integer: MIT or ASL 2.0
# num-traits: MIT or ASL 2.0
# once_cell: MIT or ASL 2.0
# ouroboros: MIT or ASL 2.0
# ouroboros_macro: MIT or ASL 2.0
# parking_lot: MIT or ASL 2.0
# parking_lot_core: MIT or ASL 2.0
# paste: MIT or ASL 2.0
# paste-impl: MIT or ASL 2.0
# pem: MIT
# proc-macro-error: MIT or ASL 2.0
# proc-macro-error-attr: MIT or ASL 2.0
# proc-macro-hack: MIT or ASL 2.0
# proc-macro2: MIT or ASL 2.0
# pyo3: ASL 2.0
# pyo3-build-config: ASL 2.0
# pyo3-macros: ASL 2.0
# pyo3-macros-backend: ASL 2.0
# quote: MIT or ASL 2.0
# scopeguard: MIT or ASL 2.0
# smallvec: MIT or ASL 2.0
# stable_deref_trait: MIT or ASL 2.0
# syn: MIT or ASL 2.0
# unicode-xid: MIT or ASL 2.0
# unindent: MIT or ASL 2.0
# version_check: MIT or ASL 2.0

License:        (ASL 2.0 or BSD) and Python and BSD and MIT and (MIT or ASL 2.0) and ASL 2.0
URL:            https://cryptography.io/en/latest/
Source0:        https://github.com/pyca/cryptography/archive/%{version}/%{srcname}-%{version}.tar.gz
                # created by ./vendor_rust.py helper script
Source1:        cryptography-%{version}-vendor.tar.bz2
Source2:        conftest-skipper.py

# Security fix for CVE-2023-23931: memory corruption via immutable objects
# Bugzilla tracker: https://bugzilla.redhat.com/show_bug.cgi?id=2171817
# Resolved upstream: https://github.com/pyca/cryptography/commit/94a50a9731f35405f0357fa5f3b177d46a726ab3
Patch0:         CVE-2023-23931.patch

# Security fix for CVE-2023-49083: NULL-dereference when loading PKCS7 certificates
# Bugzilla tracker: https://bugzilla.redhat.com/show_bug.cgi?id=2255331
# Resolved upstream:
# https://github.com/pyca/cryptography/commit/1e7b4d074e14c4e694d3ce69ad6754a6039fd6ff
# https://github.com/pyca/cryptography/commit/3165db8efc82d8e379c4931453f6c776ab8db013
Patch1:         CVE-2023-49083.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
%if 0%{?fedora}
BuildRequires:  rust-packaging
%else
BuildRequires:  rust-toolset
%endif

BuildRequires:  python%{python3_pkgversion}-cffi >= 1.7
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-rust >= 0.11.3
# Cargo.toml requires asn1 0.6, but package FTBFS with 0.6.1
#BuildRequires:  rust-asn1-devel >= 0.6.4

%if %{with tests}
%if 0%{?fedora}
BuildRequires:  python%{python3_pkgversion}-hypothesis >= 1.11.4
BuildRequires:  python%{python3_pkgversion}-iso8601
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
%endif
BuildRequires:  python%{python3_pkgversion}-pytest >= 6.0
BuildRequires:  python%{python3_pkgversion}-pytest-benchmark
BuildRequires:  python%{python3_pkgversion}-pytest-subtests >= 0.3.2
BuildRequires:  python%{python3_pkgversion}-pytz
%endif

Requires:       openssl-libs
Requires:       python%{python3_pkgversion}-cffi >= 1.7

# Provides for the bundled crates

Provides: bundled(crate(Inflector)) = 0.11.4
Provides: bundled(crate(aliasable)) = 0.1.3
Provides: bundled(crate(asn1)) = 0.8.7
Provides: bundled(crate(asn1_derive)) = 0.8.7
Provides: bundled(crate(autocfg)) = 1.1.0
Provides: bundled(crate(base64)) = 0.13.0
Provides: bundled(crate(cfg-if)) = 1.0.0
Provides: bundled(crate(chrono)) = 0.4.19
Provides: bundled(crate(indoc)) = 0.3.6
Provides: bundled(crate(indoc-impl)) = 0.3.6
Provides: bundled(crate(instant)) = 0.1.12
Provides: bundled(crate(lazy_static)) = 1.4.0
Provides: bundled(crate(libc)) = 0.2.124
Provides: bundled(crate(lock_api)) = 0.4.7
Provides: bundled(crate(num-integer)) = 0.1.44
Provides: bundled(crate(num-traits)) = 0.2.14
Provides: bundled(crate(once_cell)) = 1.10.0
Provides: bundled(crate(ouroboros)) = 0.15.0
Provides: bundled(crate(ouroboros_macro)) = 0.15.0
Provides: bundled(crate(parking_lot)) = 0.11.2
Provides: bundled(crate(parking_lot_core)) = 0.8.5
Provides: bundled(crate(paste)) = 0.1.18
Provides: bundled(crate(paste-impl)) = 0.1.18
Provides: bundled(crate(pem)) = 1.0.2
Provides: bundled(crate(proc-macro-error)) = 1.0.4
Provides: bundled(crate(proc-macro-error-attr)) = 1.0.4
Provides: bundled(crate(proc-macro-hack)) = 0.5.19
Provides: bundled(crate(proc-macro2)) = 1.0.37
Provides: bundled(crate(pyo3)) = 0.15.2
Provides: bundled(crate(pyo3-build-config)) = 0.15.2
Provides: bundled(crate(pyo3-macros)) = 0.15.2
Provides: bundled(crate(pyo3-macros-backend)) = 0.15.2
Provides: bundled(crate(quote)) = 1.0.18
Provides: bundled(crate(scopeguard)) = 1.1.0
Provides: bundled(crate(smallvec)) = 1.8.0
Provides: bundled(crate(stable_deref_trait)) = 1.2.0
Provides: bundled(crate(syn)) = 1.0.91
Provides: bundled(crate(unicode-xid)) = 0.2.2
Provides: bundled(crate(unindent)) = 0.1.8
Provides: bundled(crate(version_check)) = 0.9.4

# Cryptography crate
Provides: crate(cryptography-rust) = 0.1.0

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep
%autosetup -p1 -n %{srcname}-%{version}


%if 0%{?fedora}
# Fedora: use cargo macros to make use of RPMified crates
%cargo_prep
cd src/rust
rm -f Cargo.lock
%cargo_generate_buildrequires
cd ../..
%else
# RHEL: use vendored Rust crates
%cargo_prep -V 1
%endif

%build
export RUSTFLAGS="%build_rustflags"
%py3_build

%install
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete
%py3_install

%check
%if %{with tests}
%if 0%{?rhel}
# skip hypothesis tests on RHEL
rm -rf tests/hypothesis
# append skipper to skip iso8601 and pretend tests
cat < %{SOURCE2} >> tests/conftest.py
%endif

%if 0%{?eln}
# enable SHA-1 signatures for RSA tests
# also see https://github.com/pyca/cryptography/pull/6931 and rhbz#2060343
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
%endif

# see https://github.com/pyca/cryptography/issues/4885 and
# see https://bugzilla.redhat.com/show_bug.cgi?id=1761194 for deselected tests
# see rhbz#2042413 for memleak. It's unstable under Python 3.11 and makes
# not much sense for downstream testing.
PYTHONPATH=${PWD}/vectors:%{buildroot}%{python3_sitearch} \
    %{__python3} -m pytest \
    -k "not (test_buffer_protocol_alternate_modes or test_dh_parameters_supported or test_load_ecdsa_no_named_curve or test_openssl_memleak)"
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst docs
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info

%changelog
* Fri Jan 26 2024 Charalampos Stratakis <cstratak@redhat.com> - 37.0.2-6
- Security fix for CVE-2023-49083
- Resolves: RHEL-19832

* Thu Feb 23 2023 Charalampos Stratakis <cstratak@redhat.com> - 37.0.2-5
- Bump release for rebuild

* Mon Feb 20 2023 Charalampos Stratakis <cstratak@redhat.com> - 37.0.2-4
- Security fix for CVE-2023-23931

* Tue Feb 14 2023 Charalampos Stratakis <cstratak@redhat.com> - 37.0.2-3
- Rebuild for gating

* Mon Feb 13 2023 Charalampos Stratakis <cstratak@redhat.com> - 37.0.2-2
- Add explicit dependency on python3.11-rpm-macros

* Thu Dec 01 2022 Charalampos Stratakis <cstratak@redhat.com> - 37.0.2-1
- Initial package
- Fedora contributions by:
      Alfredo Moralejo <amoralej@redhat.com>
      Charalampos Stratakis <cstratak@redhat.com>
      Christian Heimes <christian@python.org>
      Colin Walters <walters@verbum.org>
      Dennis Gilmore <dennis@ausil.us>
      Fabio Valentini <decathorpe@gmail.com>
      Felix Schwarz <felix.schwarz@oss.schwarz.eu>
      Haikel Guemar <hguemar@fedoraproject.org>
      Igor Gnatenko <ignatenkobrain@fedoraproject.org>
      Iryna Shcherbina <shcherbina.iryna@gmail.com>
      Lumir Balhar <lbalhar@redhat.com>
      Matěj Cepl <mcepl@cepl.eu>
      Miro Hrončok <miro@hroncok.cz>
      Nathaniel McCallum <npmccallum@redhat.com>
      Randy Barlow <randy@electronsweatshop.com>
      Robert Kuska <rkuska@redhat.com>
      Sahana Prasad <sahana@redhat.com>
      Stephen Gallagher <sgallagh@redhat.com>
      Troy Dawson <tdawson@redhat.com>
