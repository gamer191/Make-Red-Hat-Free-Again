Name: eth-tools
Version: 11.5.0.0
Release: 173%{?dist}
Summary: Intel Ethernet Fabric Suite basic tools and libraries for fabric management

License: BSD
Url: https://github.com/intel/eth-fast-fabric
Source: %url/archive/refs/tags/v%{version_no_tilde}.tar.gz
ExclusiveArch: x86_64
# The Intel(R) Ethernet Fabric Suite product line is only available on x86_64 platforms at this time.

Epoch: 1

%description
This package contains the tools necessary to manage an Intel Ethernet fabric.

%package basic
Summary: Management level tools and scripts

Requires: rdma bc

Requires: expect%{?_isa}, tcl%{?_isa}, libibverbs-utils%{?_isa}, librdmacm-utils%{?_isa}, net-snmp%{?_isa}, net-snmp-utils%{?_isa}
BuildRequires: make
BuildRequires: expat-devel
BuildRequires: gcc-c++
BuildRequires: tcl-devel
BuildRequires: rdma-core-devel
BuildRequires: net-snmp-devel


%description basic
Contains basic tools for fabric management necessary on all compute nodes.

%package fastfabric
Summary: Management level tools and scripts
Requires: perl
Requires: eth-tools-basic%{?_isa} >= %{version}-%{release}

%description fastfabric
Contains tools for managing fabric on a management node.

%prep
%autosetup -n eth-fast-fabric-%{version_no_tilde}

%build
cd OpenIb_Host
OPA_FEATURE_SET= CLOCAL='%build_cflags' CCLOCAL='%build_cxxflags' LDLOCAL='%build_ldflags' ./ff_build.sh %{_builddir}

%install
BUILDDIR=%{_builddir} DESTDIR=%{buildroot} LIBDIR=%{_prefix}/lib DSAP_LIBDIR=%{_libdir} ./OpenIb_Host/ff_install.sh

%files basic
%{_sbindir}/ethbw
%{_sbindir}/ethcapture
%{_sbindir}/ethshmcleanup
%{_prefix}/lib/eth-tools/setup_self_ssh
%{_prefix}/lib/eth-tools/usemem
%{_prefix}/lib/eth-tools/ethipcalc
%{_prefix}/lib/eth-tools/stream
%{_prefix}/lib/eth-tools/ethudstress
%{_mandir}/man1/ethbw.1*
%{_mandir}/man1/ethcapture.1*
%{_mandir}/man1/ethshmcleanup.1*
%{_datadir}/eth-tools/samples/mgt_config.xml-sample
%dir %{_sysconfdir}/eth-tools/
%config(noreplace) %{_sysconfdir}/eth-tools/mgt_config.xml

%files fastfabric
%{_sbindir}/*
%exclude %{_sbindir}/ethbw
%exclude %{_sbindir}/ethcapture
%exclude %{_sbindir}/ethshmcleanup
%{_prefix}/lib/eth-tools/*
%exclude %{_prefix}/lib/eth-tools/setup_self_ssh
%exclude %{_prefix}/lib/eth-tools/usemem
%exclude %{_prefix}/lib/eth-tools/ethipcalc
%exclude %{_prefix}/lib/eth-tools/stream
%exclude %{_prefix}/lib/eth-tools/ethudstress
%{_datadir}/eth-tools/*
%exclude %{_datadir}/eth-tools/samples/mgt_config.xml-sample
%{_mandir}/man8/eth*.8*
%{_usrsrc}/eth/*
%{_sysconfdir}/eth-tools/ethmon.si.conf
# Replace ethmon.si.conf, as it's a template config file.
%config(noreplace) %{_sysconfdir}/eth-tools/ethfastfabric.conf
%config(noreplace) %{_sysconfdir}/eth-tools/ethmon.conf
%config(noreplace) %{_sysconfdir}/eth-tools/allhosts
%config(noreplace) %{_sysconfdir}/eth-tools/hosts
%config(noreplace) %{_sysconfdir}/eth-tools/switches
%config(noreplace) /usr/lib/eth-tools/osid_wrapper


%changelog
* Fri Jun 02 2023 Kamal Heib <kheib@redhat.com> - 1:11.5.0.0-173
- Update to upstream release 11.5.0.0
- Resolves: rhbz#2144026

* Fri Feb 03 2023 Michal Schmidt <mschmidt@redhat.com> - 1:11.4.0.0-201
- Update to upstream release 11.4.0.0
- Resolves: rhbz#2097531

* Wed Aug 03 2022 Michal Schmidt <mschmidt@redhat.com> - 1:11.3.0.0-1
- Update to upstream release 11.3.0.0
- Resolves: rhbz#2037052

* Tue Nov 09 2021 Honggang Li <honli@redhat.com> - 1:11.1.0.1-5
- Update to upstream release 11.1.0.1
- Fix annocheck issues
- Resolves: rhbz#2019268

* Wed Oct 27 2021 Honggang Li <honli@redhat.com> - 1:11.1.0.0-180
- Update to upstream release 11.1.0.0
- Resolves: rhbz#1991463

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:11.0.0.0-164
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Thu Jul 01 2021 Honggang Li <honli@redhat.com> - 11.0.0.0-163
- Import Intel Ethernet Fast Fabric Suite for RHEL9
- Resolves: rhbz#1919019
