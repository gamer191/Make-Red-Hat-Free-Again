%define nft_rpmversion 1.0.9
%define nft_specrelease 1

Name:           nftables
Version:        %{nft_rpmversion}
Release:        %{nft_specrelease}%{?dist}%{?buildid}
# Upstream released a 0.100 version, then 0.4. Need Epoch to get back on track.
Epoch:          1
Summary:        Netfilter Tables userspace utillites

License:        GPLv2
URL:            https://netfilter.org/projects/nftables/
Source0:        %{url}/files/%{name}-%{version}.tar.xz
Source1:        nftables.service
Source2:        nftables.conf
Source3:        main.nft
Source4:        router.nft
Source5:        nat.nft
Source6:        nft-test.stderr.expect
Source7:        run-tests.stderr.expect


BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex
BuildRequires: bison
BuildRequires: pkgconfig(libmnl) >= 1.0.4
BuildRequires: gmp-devel
BuildRequires: readline-devel
BuildRequires: pkgconfig(libnftnl) >= 1.2.6
BuildRequires: systemd
BuildRequires: asciidoc
BuildRequires: pkgconfig(xtables) >= 1.6.1
BuildRequires: jansson-devel
BuildRequires: python3-devel

%generate_buildrequires
cd py/
%pyproject_buildrequires

%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
Development tools and static libraries and header files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-nftables}

%description -n python3-nftables
The nftables python module provides an interface to libnftables via ctypes.

%prep
%autosetup -p1
cp -a %{SOURCE6} ./tests/py/
cp -a %{SOURCE7} ./tests/shell/

%build
autoreconf -fi
rm -Rf autom4te*.cache config.h.in~
%configure --disable-silent-rules --with-xtables --with-json --with-cli=readline
%make_build
cd py/
%pyproject_wheel

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Don't ship static lib (for now at least)
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnftables.a

chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man8/nft*

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
cp -a %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/

rm $RPM_BUILD_ROOT/%{_datadir}/nftables/*.nft
cp %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	$RPM_BUILD_ROOT/%{_sysconfdir}/nftables/

find $RPM_BUILD_ROOT/%{_sysconfdir} \
	\( -type d -exec chmod 0700 {} \; \) , \
	\( -type f -exec chmod 0600 {} \; \)

cd py/
%pyproject_install
%pyproject_save_files nftables

%post
%systemd_post nftables.service
%ldconfig_post

%preun
%systemd_preun nftables.service

%postun
%systemd_postun_with_restart nftables.service
%ldconfig_postun

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/nftables/
%config(noreplace) %{_sysconfdir}/sysconfig/nftables.conf
%{_sbindir}/nft
%{_libdir}/libnftables.so.*
%{_mandir}/man5/libnftables-json.5*
%{_mandir}/man8/nft*
%{_unitdir}/nftables.service
%{_docdir}/nftables/examples/*.nft

%files devel
%{_libdir}/libnftables.so
%{_libdir}/pkgconfig/libnftables.pc
%{_includedir}/nftables/libnftables.h
%{_mandir}/man3/libnftables.3*

%files -n python3-nftables -f %{pyproject_files}

%changelog
* Fri Oct 27 2023 Phil Sutter <psutter@redhat.com> [1.0.9-1.el9]
- spec: Utilize pyproject-rpm-macros for the python sub-package (Phil Sutter) [RHEL-14191]
- Rebase onto version 1.0.9 (Phil Sutter) [RHEL-14191]

* Thu Sep 21 2023 Phil Sutter <psutter@redhat.com> [1.0.4-11.el9]
- rule: check address family in set collapse (Phil Sutter) [RHEL-5908]
- spec: Rename variables to avoid a clash (Phil Sutter) [INTERNAL]

* Tue Feb 21 2023 Phil Sutter <psutter@redhat.com> [1.0.4-10.el9]
- netlink_delinearize: Sanitize concat data element decoding (Phil Sutter) [2160049]
- optimize: Clarify chain_optimize() array allocations (Phil Sutter) [2160049]
- optimize: Do not return garbage from stack (Phil Sutter) [2160049]
- netlink: Fix for potential NULL-pointer deref (Phil Sutter) [2160049]
- meta: parse_iso_date() returns boolean (Phil Sutter) [2160049]
- mnl: dump_nf_hooks() leaks memory in error path (Phil Sutter) [2160049]
- owner: Fix potential array out of bounds access (Phil Sutter) [2160049]

* Fri Feb 17 2023 Phil Sutter <psutter@redhat.com> [1.0.4-9.el9]
- tests: add a test case for map update from packet path with concat (Phil Sutter) [2094894]
- netlink_linearize: fix timeout with map updates (Phil Sutter) [2094894]
- netlink_delinearize: fix decoding of concat data element (Phil Sutter) [2094894]

* Thu Feb 09 2023 Phil Sutter <psutter@redhat.com> [1.0.4-8.el9]
- monitor: Sanitize startup race condition (Phil Sutter) [2130721]
- evaluate: set eval ctx for add/update statements with integer constants (Phil Sutter) [2094894]
- src: allow anon set concatenation with ether and vlan (Phil Sutter) [2094887]
- evaluate: search stacked header list for matching payload dep (Phil Sutter) [2094887]
- netlink_delinearize: also postprocess OP_AND in set element context (Phil Sutter) [2094887]
- tests: add a test case for ether and vlan listing (Phil Sutter) [2094887]
- debug: dump the l2 protocol stack (Phil Sutter) [2094887]
- proto: track full stack of seen l2 protocols, not just cumulative offset (Phil Sutter) [2094887]
- netlink_delinearize: postprocess binary ands in concatenations (Phil Sutter) [2094887]
- netlink_delinearize: allow postprocessing on concatenated elements (Phil Sutter) [2094887]
- intervals: check for EXPR_F_REMOVE in case of element mismatch (Phil Sutter) [2115627]
- intervals: fix crash when trying to remove element in empty set (Phil Sutter) [2115627]
- scanner: don't pop active flex scanner scope (Phil Sutter) [2113874]
- parser: add missing synproxy scope closure (Phil Sutter) [2113874]
- tests/py: Add a test for failing ipsec after counter (Phil Sutter) [2113874]
- doc: Document limitations of ipsec expression with xfrm_interface (Phil Sutter) [1806431]

* Tue Jan 31 2023 Phil Sutter <psutter@redhat.com> [1.0.4-7.el9]
- One more attempt at fixing expected error records (Phil Sutter) [1973687]

* Tue Jan 31 2023 Phil Sutter <psutter@redhat.com> [1.0.4-6.el9]
- Realy fix expected error records (Phil Sutter) [1973687]

* Fri Jan 27 2023 Phil Sutter <psutter@redhat.com> [1.0.4-5.el9]
- Fix expected error records (Phil Sutter) [1973687]

* Fri Jan 20 2023 Phil Sutter <psutter@redhat.com> [1.0.4-4.el9]
- Add expected error records for testsuite runs (Phil Sutter) [1973687]

* Fri Nov 25 2022 Phil Sutter <psutter@redhat.com> [1.0.4-3.el9]
- Prevent port-shadow attacks in sample nat config (Phil Sutter) [2061940]

* Fri Jun 24 2022 Phil Sutter <psutter@redhat.com> [1.0.4-2.el9]
- intervals: Do not sort cached set elements over and over again (Phil Sutter) [1917398]
- intervals: do not empty cache for maps (Phil Sutter) [1917398]
- intervals: do not report exact overlaps for new elements (Phil Sutter) [1917398]
- rule: collapse set element commands (Phil Sutter) [1917398]
- tests: shell: runtime set element automerge (Phil Sutter) [1917398]

* Thu Jun 09 2022 Phil Sutter <psutter@redhat.com> - 1:1.0.4-1
- Review package dependencies
- new version 1.0.4

* Tue Mar 01 2022 Phil Sutter <psutter@redhat.com> - 1:0.9.8-13
- tests: extend dtype test case to cover expression with integer type
- evaluate: set evaluation context for set elements

* Fri Jan 14 2022 Phil Sutter <psutter@redhat.com> - 1:0.9.8-12
- evaluate: pick data element byte order, not dtype one

* Wed Dec 08 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-11
- tests: py: add dnat to port without defining destination address
- evaluate: fix inet nat with no layer 3 info
- include: missing sctp_chunk.h in Makefile.am
- exthdr: Implement SCTP Chunk matching
- scanner: sctp: Move to own scope
- scanner: introduce start condition stack
- json: Simplify non-tcpopt exthdr printing a bit

* Wed Dec 08 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-10
- tests: shell: better parameters for the interval stack overflow test
- tests: shell: $NFT needs to be invoked unquoted

* Thu Nov 11 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-9
- doc: nft.8: Extend monitor description by trace

* Fri Nov 05 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-8
- tests: cover baecd1cf2685 ("segtree: Fix segfault when restoring a huge interval set")
- segtree: Fix segfault when restoring a huge interval set

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.9.8-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jun 18 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-6
- json: init parser state for every new buffer/file

* Tue Jun 15 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-5
- src: add xzalloc_array() and use it to allocate the expression hashtable

* Mon Jun 14 2021 Phil Sutter <psutter@redhat.com> - 1:0.9.8-4
- Install an improved sample config
- Fix permissions of osf-related configs
- rule: Fix for potential off-by-one in cmd_add_loc()
- netlink_delinearize: Fix suspicious calloc() call
- netlink: Avoid memleak in error path of netlink_delinearize_obj()
- netlink: Avoid memleak in error path of netlink_delinearize_table()
- netlink: Avoid memleak in error path of netlink_delinearize_chain()
- netlink: Avoid memleak in error path of netlink_delinearize_set()
- json: Drop pointless assignment in exthdr_expr_json()
- evaluate: Mark fall through case in str2hooknum()
- parser_json: Fix for memleak in tcp option error path
- parser_bison: Fix for implicit declaration of isalnum
- main: fix nft --help output fallout from 719e4427
- tests: add icmp/6 test where dependency should be left alone
- payload: check icmp dependency before removing previous icmp expression

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.9.8-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Kevin Fenzi <kevin@scrye.com> - 0.9.8-1
- Update to 0.9.8. Fixes rhbz#1916940

* Sat Oct 31 2020 Kevin Fenzi <kevin@scrye.com> - 0.9.7-1
- Update to 0.9.7. Fixes bug #1891769

* Thu Oct 29 2020 Stephen Gallagher <sgallagh@redhat.com> - 1:0.9.6-2
- Drop upstreamed patch

* Sat Sep 05 2020 Neal Gompa <ngompa13@gmail.com> - 1:0.9.6-1
- Update to 0.9.6 (RH#1846663)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 1:0.9.3-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.9.3-4
- Rebuilt for Python 3.9

* Fri May 15 2020 Richard Shaw <hobbes1069@gmail.com> - 1:0.9.3-3
- Add patch for json performance with ipsets, fixes RHBZ#1834853.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.3-1
- Update to 0.9.3. Fixes bug #1778959

* Tue Oct 01 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.2-3
- Drop unneeded docbook2X build dependency
- Add python3-nftables sub-package

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.2-2
- Move libnftables section 3 man page to devel package.

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.2-1
- Update to 0.9.2. Fixes bug #1743223

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.1-2
- Add some filters to nftables.conf

* Tue Jun 25 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.1-1
- Update to 0.9.1. Fixes bug #1723515

* Mon Jun 17 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.0-7
- Rebuild for new libnftnl.

* Sat Mar 16 2019 Kevin Fenzi <kevin@scrye.com> - 1:0.9.0-6
- Fix permissions. Bug #1685242

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.9.0-5
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.0-3
- Fix config file to have correct include names. Fixes bug #1642103

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.0-1
- Update to 0.9.0. Fixes bug #1589404

* Fri May 11 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.5-1
- Update to 0.8.5. Fixes bug #1576802

* Sun May 06 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.4-2
- Fix devel package to require the Epoch too.
- Fix libraries split

* Fri May 04 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.4-1
- Update to 0.8.4. Fixes bug #1574096

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.3-1
- Update to 0.8.3. Fixes bug #1551207

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.2-1
- Update to 0.8.2. Fixes bug #1541582

* Tue Jan 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.1-1
- Update to 0.8.1. Fixes bug #1534982

* Sun Oct 22 2017 Kevin Fenzi <kevin@scrye.com> - 0.8-1
- Update to 0.8. 

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:0.7-2
- Rebuild for readline 7.x

* Thu Dec 22 2016 Kevin Fenzi <kevin@scrye.com> - 0.7-1
- Update to 0.7

* Fri Jul 15 2016 Kevin Fenzi <kevin@scrye.com> - 0.6-2
- Rebuild for new glibc symbols

* Thu Jun 02 2016 Kevin Fenzi <kevin@scrye.com> - 0.6-1
- Update to 0.6.

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-4
- Add example config files and move config to /etc/sysconfig. Fixes bug #1313936

* Fri Mar 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-3
- Add systemd unit file. Fixes bug #1313936

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Kevin Fenzi <kevin@scrye.com> 0.5-1
- Update to 0.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Kevin Fenzi <kevin@scrye.com> 0.4-2
- Add patch to fix nft -f dep gen.

* Fri Dec 26 2014 Kevin Fenzi <kevin@scrye.com> 0.4-1
- Update to 0.4
- Add Epoch to fix versioning. 

* Wed Sep 03 2014 Kevin Fenzi <kevin@scrye.com> 0.100-4.20140903git
- Update to 20140903 snapshot

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-4.20140704git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Kevin Fenzi <kevin@scrye.com> 0.100-3.20140704git
- Update to new snapshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-2.20140426git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140426git
- Update t0 20140426

* Sun Mar 30 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140330git
- Update to 20140330 snapshot
- Sync versions to be post 0.100 release.

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 0-0.7.20140326git
- Update to 20140326 snapshot
- Fix permissions on man pages. 

* Mon Mar 24 2014 Kevin Fenzi <kevin@scrye.com> 0-0.6.20140324git
- Update to 20140324 snapshot

* Fri Mar 07 2014 Kevin Fenzi <kevin@scrye.com> 0-0.5.20140307git
- Update to 20140307

* Sat Jan 25 2014 Kevin Fenzi <kevin@scrye.com> 0-0.4.20140125git
- Update to 20140125 snapshot

* Sat Jan 18 2014 Kevin Fenzi <kevin@scrye.com> 0-0.3.20140118git
- Update to 20140118 snapshot
- Fixed License tag to be correct
- Fixed changelog
- nft scripts now use full path for nft
- Fixed man page building
- Dropped unneeded rm in install
- Patched build to not be silent. 

* Tue Dec 03 2013 Kevin Fenzi <kevin@scrye.com> 0-0.2.20131202git
- Use upstream snapshots for source.
- Use 0 for version. 

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 0-0.1
- initial version for Fedora review
