%global __python3 /usr/bin/python3.12
%global python3_pkgversion 3.12

# RHEL: Tests disabled due to missing deps
%bcond_with tests

%global srcname cryptography

Name:           python%{python3_pkgversion}-%{srcname}
Version:        41.0.7
Release:        1%{?dist}
Summary:        PyCA's cryptography library

# We bundle various crates with cryptography which is dual licensed
# under the ASL 2.0 or BSD, as well as the Python license
# for the OS random engine derived by CPython.

# in the vendor dir from SOURCE1:
#     import pathlib, tomllib
#     bundled = {}
#     for d in pathlib.Path('.').iterdir():
#         cargo_toml = d / 'Cargo.toml'
#         cargo = tomllib.loads(cargo_toml.read_text())
#         bundled[cargo['package']['name']] = cargo['package']
#     for pkg in sorted(bundled):
#         print(f"# {pkg}: {bundled[pkg]['license']}")
# the output was then manually de-SPDX'ed
# windows-only crates manually removed from this list

# Inflector: BSD
# aliasable: MIT
# asn1: BSD
# asn1_derive: BSD
# autocfg: MIT or ASL 2.0
# base64: MIT or ASL 2.0
# bitflags: MIT or ASL 2.0
# cc: MIT or ASL 2.0
# cfg-if: MIT or ASL 2.0
# foreign-types: MIT or ASL 2.0
# foreign-types-shared: MIT or ASL 2.0
# indoc: MIT or ASL 2.0
# libc: MIT or ASL 2.0
# lock_api: MIT or ASL 2.0
# memoffset: MIT
# once_cell: MIT or ASL 2.0
# openssl: ASL 2.0
# openssl-macros: MIT or ASL 2.0
# openssl-sys: MIT
# ouroboros: MIT or ASL 2.0
# ouroboros_macro: MIT or ASL 2.0
# parking_lot: MIT or ASL 2.0
# parking_lot_core: MIT or ASL 2.0
# pem: MIT
# pkg-config: MIT or ASL 2.0
# proc-macro-error: MIT or ASL 2.0
# proc-macro-error-attr: MIT or ASL 2.0
# proc-macro2: MIT or ASL 2.0
# pyo3: ASL 2.0
# pyo3-build-config: ASL 2.0
# pyo3-ffi: ASL 2.0
# pyo3-macros: ASL 2.0
# pyo3-macros-backend: ASL 2.0
# quote: MIT or ASL 2.0
# redox_syscall: MIT
# scopeguard: MIT or ASL 2.0
# smallvec: MIT or ASL 2.0
# syn: MIT or ASL 2.0
# target-lexicon: ASL 2.0 (with LLVM-exception)
# unicode-ident: (MIT or ASL 2.0) and Unicode
# unindent: MIT or ASL 2.0
# vcpkg: MIT or ASL 2.0
# version_check: MIT or ASL 2.0
License:        (ASL 2.0 or BSD) and Python and BSD and MIT and ASL 2.0 and (MIT or ASL 2.0) and Unicode

URL:            https://cryptography.io/en/latest/
Source0:        https://github.com/pyca/cryptography/archive/%{version}/%{srcname}-%{version}.tar.gz
                # created by ./vendor_rust.py helper script
Source1:        cryptography-%{version}-vendor.tar.bz2
Source2:        conftest-skipper.py

# Improvement for the fix for CVE-2023-49083
# Backported from upstream:
# https://github.com/pyca/cryptography/commit/3165db8efc82d8e379c4931453f6c776ab8db013
Patch1:         raise-an-exception-for-CVE-2023-49083.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
%if 0%{?fedora}
BuildRequires:  rust-packaging
# test_load_with_other_sections in 40.0 fails with pem 1.1.0
BuildRequires:  rust-pem-devel >= 1.1.1
%else
BuildRequires:  rust-toolset
%endif

BuildRequires:  python%{python3_pkgversion}-cffi >= 1.12
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-rust >= 0.11.4

%if %{with tests}
%if 0%{?fedora}
BuildRequires:  python%{python3_pkgversion}-hypothesis >= 1.11.4
BuildRequires:  python%{python3_pkgversion}-iso8601
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
BuildRequires:  python%{python3_pkgversion}-pytz
%endif
BuildRequires:  python%{python3_pkgversion}-pytest >= 6.2.0
BuildRequires:  python%{python3_pkgversion}-pytest-benchmark
BuildRequires:  python%{python3_pkgversion}-pytest-subtests >= 0.5.0
%endif

Requires:       openssl-libs
Requires:       python%{python3_pkgversion}-cffi >= 1.12

# Provides for the bundled crates
# (continuation of the snippet above the License tag)
#     for pkg in sorted(bundled):
#         print(f"Provides: bundled(crate({pkg})) = {bundled[pkg]['version']}")
Provides: bundled(crate(Inflector)) = 0.11.4
Provides: bundled(crate(aliasable)) = 0.1.3
Provides: bundled(crate(asn1)) = 0.15.2
Provides: bundled(crate(asn1_derive)) = 0.15.2
Provides: bundled(crate(autocfg)) = 1.1.0
Provides: bundled(crate(base64)) = 0.13.1
Provides: bundled(crate(bitflags)) = 1.3.2
Provides: bundled(crate(cc)) = 1.0.79
Provides: bundled(crate(cfg-if)) = 1.0.0
Provides: bundled(crate(foreign-types)) = 0.3.2
Provides: bundled(crate(foreign-types-shared)) = 0.1.1
Provides: bundled(crate(indoc)) = 1.0.9
Provides: bundled(crate(libc)) = 0.2.144
Provides: bundled(crate(lock_api)) = 0.4.9
Provides: bundled(crate(memoffset)) = 0.8.0
Provides: bundled(crate(once_cell)) = 1.17.2
Provides: bundled(crate(openssl)) = 0.10.60
Provides: bundled(crate(openssl-macros)) = 0.1.1
Provides: bundled(crate(openssl-sys)) = 0.9.96
Provides: bundled(crate(ouroboros)) = 0.15.6
Provides: bundled(crate(ouroboros_macro)) = 0.15.6
Provides: bundled(crate(parking_lot)) = 0.12.1
Provides: bundled(crate(parking_lot_core)) = 0.9.7
Provides: bundled(crate(pem)) = 1.1.1
Provides: bundled(crate(pkg-config)) = 0.3.27
Provides: bundled(crate(proc-macro-error)) = 1.0.4
Provides: bundled(crate(proc-macro-error-attr)) = 1.0.4
Provides: bundled(crate(proc-macro2)) = 1.0.64
Provides: bundled(crate(pyo3)) = 0.18.3
Provides: bundled(crate(pyo3-build-config)) = 0.18.3
Provides: bundled(crate(pyo3-ffi)) = 0.18.3
Provides: bundled(crate(pyo3-macros)) = 0.18.3
Provides: bundled(crate(pyo3-macros-backend)) = 0.18.3
Provides: bundled(crate(quote)) = 1.0.28
Provides: bundled(crate(redox_syscall)) = 0.2.16
Provides: bundled(crate(scopeguard)) = 1.1.0
Provides: bundled(crate(smallvec)) = 1.10.0
Provides: bundled(crate(syn)) = 1.0.109
Provides: bundled(crate(target-lexicon)) = 0.12.7
Provides: bundled(crate(unicode-ident)) = 1.0.9
Provides: bundled(crate(unindent)) = 0.1.11
Provides: bundled(crate(vcpkg)) = 0.2.15
Provides: bundled(crate(version_check)) = 0.9.4

# Cryptography crates
Provides: bundled(crate(cryptography-cffi)) = 0.1.0
Provides: bundled(crate(cryptography-openssl)) = 0.1.0
Provides: bundled(crate(cryptography-rust)) = 0.1.0
Provides: bundled(crate(cryptography-x509)) = 0.1.0

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%prep
%autosetup -p1 -n %{srcname}-%{version}
%if 0%{?fedora}
%cargo_prep
rm src/rust/Cargo.lock
%else
# RHEL: use vendored Rust crates
%cargo_prep -V 1
%endif

%if 0%{?fedora}
%generate_buildrequires
# Fedora: use RPMified crates
cd src/rust
%cargo_generate_buildrequires
cd ../..
%endif

# Remove cosmetical pytest-subtests 0.10.0 option
sed -i 's,--no-subtests-shortletter,,' pyproject.toml

%build
export OPENSSL_NO_VENDOR=1
%py3_build

%install
# Actually other *.c and *.h are appropriate
# see https://github.com/pyca/cryptography/issues/1463
find . -name .keep -print -delete
%py3_install

%check
%if %{with tests}
%if 0%{?rhel}
# skip hypothesis and pytz tests on RHEL
rm -rf tests/hypothesis tests/x509
# append skipper to skip iso8601 and pretend tests
cat < %{SOURCE2} >> tests/conftest.py
%endif

# enable SHA-1 signatures for RSA tests
# also see https://github.com/pyca/cryptography/pull/6931 and rhbz#2060343
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes

# see https://github.com/pyca/cryptography/issues/4885 and
# see https://bugzilla.redhat.com/show_bug.cgi?id=1761194 for deselected tests
# see rhbz#2042413 for memleak. It's unstable under Python 3.11 and makes
# not much sense for downstream testing.
# see rhbz#2171661 for test_load_invalid_ec_key_from_pem: error:030000CD:digital envelope routines::keymgmt export failure
PYTHONPATH=${PWD}/vectors:%{buildroot}%{python3_sitearch} \
    %{__python3} -m pytest \
    --ignore vendor \
    -k "not (test_buffer_protocol_alternate_modes or test_dh_parameters_supported or test_load_ecdsa_no_named_curve or test_decrypt_invalid_decrypt or test_openssl_memleak or test_load_invalid_ec_key_from_pem)"
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst docs
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info

%changelog
* Tue Feb 06 2024 Miro Hrončok <mhroncok@redhat.com> - 41.0.7-1
- Update to 41.0.7, fixes CVE-2023-49083

* Tue Jan 23 2024 Miro Hrončok <mhroncok@redhat.com> - 41.0.5-2
- Rebuilt for timestamp .pyc invalidation mode

* Wed Nov 08 2023 Charalampos Stratakis <cstratak@redhat.com> - 41.0.5-1
- Initial package
- Fedora contributions by:
      Alfredo Moralejo <amoralej@redhat.com>
      Benjamin A. Beasley <code@musicinmybrain.net>
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
      Yaakov Selkowitz <yselkowi@redhat.com>
