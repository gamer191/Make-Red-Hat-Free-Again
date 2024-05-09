Name:           nispor
Version:        1.2.14
Release:        1%{?dist}
Summary:        API for network status querying
License:        ASL 2.0
URL:            https://github.com/nispor/nispor
Source:         https://github.com/nispor/nispor/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/nispor/nispor/releases/download/v%{version}/nispor-vendor-%{version}.tar.xz
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  rust-toolset
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-devel

Provides: bundled(crate(aho-corasick)) = 0.7.20
Provides: bundled(crate(anyhow)) = 1.0.68
Provides: bundled(crate(atty)) = 0.2.14
Provides: bundled(crate(autocfg)) = 1.1.0
Provides: bundled(crate(bitflags)) = 1.3.2
Provides: bundled(crate(byteorder)) = 1.4.3
Provides: bundled(crate(bytes)) = 1.3.0
Provides: bundled(crate(cfg-if)) = 1.0.0
Provides: bundled(crate(clap)) = 3.2.23
Provides: bundled(crate(clap_lex)) = 0.2.4
Provides: bundled(crate(diff)) = 0.1.13
Provides: bundled(crate(env_logger)) = 0.9.3
Provides: bundled(crate(ethtool)) = 0.2.4
Provides: bundled(crate(futures)) = 0.3.26
Provides: bundled(crate(futures-channel)) = 0.3.26
Provides: bundled(crate(futures-core)) = 0.3.26
Provides: bundled(crate(futures-executor)) = 0.3.26
Provides: bundled(crate(futures-io)) = 0.3.26
Provides: bundled(crate(futures-macro)) = 0.3.26
Provides: bundled(crate(futures-sink)) = 0.3.26
Provides: bundled(crate(futures-task)) = 0.3.26
Provides: bundled(crate(futures-util)) = 0.3.26
Provides: bundled(crate(genetlink)) = 0.2.4
Provides: bundled(crate(hashbrown)) = 0.12.3
Provides: bundled(crate(humantime)) = 2.1.0
Provides: bundled(crate(indexmap)) = 1.9.2
Provides: bundled(crate(itoa)) = 1.0.5
Provides: bundled(crate(libc)) = 0.2.139
Provides: bundled(crate(log)) = 0.4.17
Provides: bundled(crate(memchr)) = 2.5.0
Provides: bundled(crate(mio)) = 0.8.5
Provides: bundled(crate(mptcp-pm)) = 0.1.2
Provides: bundled(crate(netlink-packet-core)) = 0.5.0
Provides: bundled(crate(netlink-packet-generic)) = 0.3.2
Provides: bundled(crate(netlink-packet-route)) = 0.15.0
Provides: bundled(crate(netlink-packet-utils)) = 0.5.2
Provides: bundled(crate(netlink-proto)) = 0.11.1
Provides: bundled(crate(netlink-sys)) = 0.8.4
Provides: bundled(crate(nix)) = 0.26.2
Provides: bundled(crate(once_cell)) = 1.17.0
Provides: bundled(crate(os_str_bytes)) = 6.4.1
Provides: bundled(crate(paste)) = 1.0.11
Provides: bundled(crate(pin-project-lite)) = 0.2.9
Provides: bundled(crate(pin-utils)) = 0.1.0
Provides: bundled(crate(pretty_assertions)) = 1.3.0
Provides: bundled(crate(proc-macro2)) = 1.0.50
Provides: bundled(crate(quote)) = 1.0.23
Provides: bundled(crate(regex)) = 1.7.1
Provides: bundled(crate(regex-syntax)) = 0.6.28
Provides: bundled(crate(rtnetlink)) = 0.12.0
Provides: bundled(crate(ryu)) = 1.0.12
Provides: bundled(crate(serde)) = 1.0.152
Provides: bundled(crate(serde_derive)) = 1.0.152
Provides: bundled(crate(serde_json)) = 1.0.91
Provides: bundled(crate(serde_yaml)) = 0.9.17
Provides: bundled(crate(slab)) = 0.4.7
Provides: bundled(crate(socket2)) = 0.4.7
Provides: bundled(crate(static_assertions)) = 1.1.0
Provides: bundled(crate(strsim)) = 0.10.0
Provides: bundled(crate(syn)) = 1.0.107
Provides: bundled(crate(termcolor)) = 1.2.0
Provides: bundled(crate(textwrap)) = 0.16.0
Provides: bundled(crate(thiserror)) = 1.0.38
Provides: bundled(crate(thiserror-impl)) = 1.0.38
Provides: bundled(crate(tokio)) = 1.25.0
Provides: bundled(crate(tokio-macros)) = 1.8.2
Provides: bundled(crate(unicode-ident)) = 1.0.6
Provides: bundled(crate(unsafe-libyaml)) = 0.2.5
Provides: bundled(crate(yansi)) = 0.5.1

%description
Unified interface for Linux network state querying.

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       nispor = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch:      noarch

%description -n python3-%{name}

This package contains python3 binding of %{name}.

%package        devel
Summary:        %{summary}
Requires:       nispor%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel

This package contains C binding of %{name}.

%prep
%autosetup -p1

# Source1 is vendored dependencies
%cargo_prep -V 1

# The cargo_prep will create `.cargo/config` which take precedence over
# `.cargo/config.toml` shipped by upstream which fix the SONAME of cdylib.
# To workaround that, merge upstream rustflags into cargo_prep created one.
_FLAGS=`sed -ne 's/rustflags = "\(.\+\)"/\1/p' .cargo/config.toml`
sed -i -e "s/rustflags = \[\(.\+\), \]$/rustflags = [\1, \"$_FLAGS\"]/" \
    .cargo/config
rm .cargo/config.toml

%build
make
pushd src/python
%py3_build
popd

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%install
env SKIP_PYTHON_INSTALL=1 PREFIX=%{_prefix} LIBDIR=%{_libdir} %make_install

pushd src/python
%py3_install
popd

%files
%doc AUTHORS CHANGELOG DEVEL.md README.md
%license LICENSE
%{_bindir}/npc
%{_libdir}/libnispor.so.*

%files -n       python3-%{name}
%license LICENSE
%{python3_sitelib}/nispor*

%files devel
%license LICENSE
%{_libdir}/libnispor.so
%{_includedir}/nispor.h
%{_libdir}/pkgconfig/nispor.pc

%changelog
* Wed Sep 20 2023 Matej Focko <mfocko@redhat.com> - 1.2.14-1
- New release 1.2.14 (Gris Ge)
- bond: support changing bond mode (Gris Ge)
- Reorganize the code structure (Gris Ge)
- CI: Enable VRF and ethool pause test (Gris Ge)
- CI: Upgrade the version of github action tasks (Gris Ge)
- test: Fix ethtool link mode test on Ubuntu (Gris Ge)
- Github CI: Install extra module of running kernel (Gris Ge)
- macsec: add base_iface property (Fernando Fernandez Mancera)
- macsec: add MACsec interface support (Fernando Fernandez Mancera)
- Bump netlink-packet-route to 0.17.1 (Fernando Fernandez Mancera)

* Thu Jul 20 2023 Gris Ge <fge@redhat.com> - 1.2.12-1
- New release 1.2.12 (Gris Ge)
- Use latest rust-netlink crates (Gris Ge)

* Thu Feb 16 2023 Gris Ge <fge@redhat.com> - 1.2.10-1
- Upgrade to 1.2.10. RHBZ#2153165

* Thu Dec 15 2022 Gris Ge <fge@redhat.com> - 1.2.9-1
- Upgrade to 1.2.9. RHBZ#2153165

* Thu Jun 30 2022 Gris Ge <fge@redhat.com> - 1.2.7-1
- Upgrade to 1.2.7.

* Tue Mar 15 2022 Gris Ge <fge@redhat.com> - 1.2.4-1
- Upgarde to 1.2.4. RHBZ#2064299

* Thu Jan 13 2022 Gris Ge <fge@redhat.com> - 1.2.3-1
- Upgrade to 1.2.3. Resolves: RHBZ#1996623

* Fri Dec 03 2021 Gris Ge <fge@redhat.com> - 1.2.2-1
- Upgrade to 1.2.2. Resolves: RHBZ#1996623

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.1.1-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Sat Jun 19 2021 Gris Ge <fge@redhat.com> - 1.1.1-1
- Upgrade to 1.1.1. Resolves: RHBZ#1962382

* Wed Jun 16 2021 Wen Liang <wenliang@redhat.com> - 1.1.0-2
- Upload the new vendor tarball compressed by 'xz' tool. Resolves: RHBZ#1962382

* Tue Jun 01 2021 Wen Liang <wenliang@redhat.com> - 1.1.0-1
- Upgrade to 1.1.0. RHBZ#1962382

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0.1-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Nov 13 2020 Gris Ge <fge@redhat.com> - 1.0.1-2
- Upload new cargo vendor tarbal without crates used for windows platform.

* Tue Nov 10 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 1.0.1-1
- Upgrade to 1.0.1

* Mon Nov 09 2020 Gris Ge <fge@redhat.com> - 1.0.0-1
- Upgrade to 1.0.0

* Mon Oct 19 2020 Gris Ge <fge@redhat.com> - 0.6.1-2
- Rebuild to load the compose settings.

* Tue Oct 13 2020 Gris Ge <fge@redhat.com> - 0.6.1-1
- Upgrade to 0.6.1

* Fri Oct 09 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.6.0-2
- VXLAN Python fix incorrect destination port

* Fri Oct 09 2020 Fernando Fernandez Mancera <ferferna@redhat.com> - 0.6.0-1
- Upgrade to 0.6.0

* Sun Sep 20 2020 Gris Ge <fge@redhat.com> - 0.5.1-1
- Upgrade to 0.5.1

* Thu Sep 17 2020 Gris Ge <fge@redhat.com> - 0.5.0-3
- Trigger rebuild for CI gating

* Tue Sep 08 2020 Gris Ge <fge@redhat.com> - 0.5.0-2
- Fix the python3-nispor requirement

* Fri Sep 04 2020 Gris Ge <fge@redhat.com> - 0.5.0-1
- Upgrade to 0.5.0

* Sat Aug 29 2020 Gris Ge <fge@redhat.com> - 0.4.0-3
- Fix the ldconfig

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-2
- Add ldconfig to post and postun scripts

* Wed Aug 26 2020 Gris Ge <fge@redhat.com> - 0.4.0-1
- Upgrade to 0.4.0

* Mon Aug 17 2020 Gris Ge <fge@redhat.com> - 0.3.0-2
- Fix python linux bridge vlan filtering

* Sun Aug 16 2020 Gris Ge <fge@redhat.com> - 0.3.0-1
- Upgrade to 0.3.0

* Tue Aug 11 2020 Gris Ge <fge@redhat.com> - 0.2.0-1
- Upgrade to 0.2.0

* Thu Jul 09 2020 Gris Ge <fge@redhat.com> - 0.1.1-2
- Include license and documents

* Wed Jul 08 2020 Gris Ge <fge@redhat.com> - 0.1.1-1
- Initial build.
