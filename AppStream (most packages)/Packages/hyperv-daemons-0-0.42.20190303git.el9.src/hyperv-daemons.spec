# Hyper-V KVP daemon binary name
%global hv_kvp_daemon hypervkvpd
# Hyper-V VSS daemon binary name
%global hv_vss_daemon hypervvssd
# Hyper-V FCOPY daemon binary name
%global hv_fcopy_daemon hypervfcopyd
# snapshot version
%global snapver .20190303git
# use hardened build
%global _hardened_build 1
# udev rules prefix
%global udev_prefix 70

Name:     hyperv-daemons
Version:  0
Release:  0.42%{?snapver}%{?dist}
Summary:  Hyper-V daemons suite

License:  GPLv2
URL:      http://www.kernel.org

# Source files obtained from kernel upstream 4.17-rc1 (60cc43fc888428bb2f18f08997432d426a243338)
# git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
Source0:  COPYING

# HYPERV KVP DAEMON
Source1:  hv_kvp_daemon.c
Source2:  hv_get_dhcp_info.sh
Source3:  hv_get_dns_info.sh
Source4:  hv_set_ifconfig.sh
Source5:  hypervkvpd.service
Source6:  hypervkvp.rules

# HYPERV VSS DAEMON
Source100:  hv_vss_daemon.c
Source101:  hypervvssd.service
Source102:  hypervvss.rules

# HYPERV FCOPY DAEMON
Source200:  hv_fcopy_daemon.c
Source201:  hypervfcopyd.service
Source202:  hypervfcopy.rules

# HYPERV TOOLS
Source301:  lsvmbus

Patch0002: 0002-Do-not-set-NM_CONTROLLED-no.patch
Patch0004: 0004-Update-C-files-and-scripts-to-kernel-version-5.7-rc1.patch
Patch0005: 0005-Add-vmbus_testing-tool-build-files.patch
Patch0006: 0006-tools-hv-change-http-to-https-in-hv_kvp_daemon.c.patch
# For bz#2026371 - [RHEL9][Hyper-V]The /usr/libexec/hypervkvpd/hv_set_ifconfig need update for RHEL9 since the ifdown/ifup was not supported on RHEL9
Patch7: hpvd-hv_set_ifconfig.sh-Use-nmcli-commands.patch
# For bz#2026371 - [RHEL9][Hyper-V]The /usr/libexec/hypervkvpd/hv_set_ifconfig need update for RHEL9 since the ifdown/ifup was not supported on RHEL9
Patch8: hpvd-Use-filename-for-connection-profile.patch
# For bz#2122115 - [Hyper-V][RHEL-9] Cannot set gateway properly when set static IPADDR0,NETMASK0,GATEWAY in ifcfg-eth0
Patch9: hpvd-redhat-hv_set_if_config-Workaround-for-gateway-numbe.patch
# For bz#2139457 - [Hyper-V][RHEL9.2] Update Hyper-V-Daemons
Patch10: hpvd-tools-hv-Remove-an-extraneous-the.patch
# For bz#2139457 - [Hyper-V][RHEL9.2] Update Hyper-V-Daemons
Patch11: hpvd-tools-hv-kvp-remove-unnecessary-void-conversions.patch
# For bz#2218931 - [Hyper-V] [RHEL-9] /usr/sbin/vmbus_testing python script prints: "SyntaxWarning: "is" with a literal."
Patch12: hpvd-vmbus_testing-fix-wrong-python-syntax-for-integer-va.patch

# Source-git patches

# Hyper-V is available only on x86 and aarch64 architectures
# The base empty (a.k.a. virtual) package can not be noarch
# due to http://www.rpm.org/ticket/78
ExclusiveArch:  i686 x86_64 aarch64

Requires:       hypervkvpd = %{version}-%{release}
Requires:       hypervvssd = %{version}-%{release}
Requires:       hypervfcopyd = %{version}-%{release}
BuildRequires:  gcc


%description
Suite of daemons that are needed when Linux guest
is running on Windows Host with Hyper-V.


%package -n hypervkvpd
Summary: Hyper-V key value pair (KVP) daemon
Requires: %{name}-license = %{version}-%{release}
BuildRequires: systemd, kernel-headers
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n hypervkvpd
Hypervkvpd is an implementation of Hyper-V key value pair (KVP)
functionality for Linux. The daemon first registers with the
kernel driver. After this is done it collects information
requested by Windows Host about the Linux Guest. It also supports
IP injection functionality on the Guest.


%package -n hypervvssd
Summary: Hyper-V VSS daemon
Requires: %{name}-license = %{version}-%{release}
BuildRequires: systemd, kernel-headers
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n hypervvssd
Hypervvssd is an implementation of Hyper-V VSS functionality
for Linux. The daemon is used for host initiated guest snapshot
on Hyper-V hypervisor. The daemon first registers with the
kernel driver. After this is done it waits for instructions
from Windows Host if to "freeze" or "thaw" the filesystem
on the Linux Guest.


%package -n hypervfcopyd
Summary: Hyper-V FCOPY daemon
Requires: %{name}-license = %{version}-%{release}
BuildRequires: systemd, kernel-headers
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n hypervfcopyd
Hypervfcopyd is an implementation of file copy service functionality
for Linux Guest running on Hyper-V. The daemon enables host to copy
a file (over VMBUS) into the Linux Guest. The daemon first registers
with the kernel driver. After this is done it waits for instructions
from Windows Host.


%package license
Summary:    License of the Hyper-V daemons suite
BuildArch:  noarch

%description license
Contains license of the Hyper-V daemons suite.

%package -n hyperv-tools
Summary:    Tools for Hyper-V guests
BuildArch:  noarch

%description -n hyperv-tools
Contains tools and scripts useful for Hyper-V guests.

%prep
%setup -Tc
cp -pvL %{SOURCE0} COPYING

cp -pvL %{SOURCE1} hv_kvp_daemon.c
cp -pvL %{SOURCE2} hv_get_dhcp_info.sh
cp -pvL %{SOURCE3} hv_get_dns_info.sh
cp -pvL %{SOURCE4} hv_set_ifconfig.sh
cp -pvL %{SOURCE5} hypervkvpd.service
cp -pvL %{SOURCE6} hypervkvp.rules
cp -pvL %{SOURCE100} hv_vss_daemon.c
cp -pvL %{SOURCE101} hypervvssd.service
cp -pvL %{SOURCE102} hypervvss.rules
cp -pvL %{SOURCE200} hv_fcopy_daemon.c
cp -pvL %{SOURCE201} hypervfcopyd.service
cp -pvL %{SOURCE202} hypervfcopy.rules

cp -pvL %{SOURCE301} lsvmbus

%patch0002 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
# HYPERV KVP DAEMON
%{__cc} $RPM_OPT_FLAGS -c hv_kvp_daemon.c
%{__cc} $RPM_LD_FLAGS  hv_kvp_daemon.o -o %{hv_kvp_daemon}

# HYPERV VSS DAEMON
%{__cc} $RPM_OPT_FLAGS -c hv_vss_daemon.c
%{__cc} $RPM_LD_FLAGS hv_vss_daemon.o -o %{hv_vss_daemon}

# HYPERV FCOPY DAEMON
%{__cc} $RPM_OPT_FLAGS -c hv_fcopy_daemon.c
%{__cc} $RPM_LD_FLAGS hv_fcopy_daemon.o -o %{hv_fcopy_daemon}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sbindir}
install -p -m 0755 %{hv_kvp_daemon} %{buildroot}%{_sbindir}
install -p -m 0755 %{hv_vss_daemon} %{buildroot}%{_sbindir}
install -p -m 0755 %{hv_fcopy_daemon} %{buildroot}%{_sbindir}
# Systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 hypervkvpd.service %{buildroot}%{_unitdir}
install -p -m 0644 hypervvssd.service %{buildroot}%{_unitdir}
install -p -m 0644 hypervfcopyd.service %{buildroot}%{_unitdir}
# Udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 0644 hypervkvp.rules %{buildroot}%{_udevrulesdir}/%{udev_prefix}-hypervkvp.rules
install -p -m 0644 hypervvss.rules %{buildroot}%{_udevrulesdir}/%{udev_prefix}-hypervvss.rules
install -p -m 0644 hypervfcopy.rules %{buildroot}%{_udevrulesdir}/%{udev_prefix}-hypervfcopy.rules
# Shell scripts for the KVP daemon
mkdir -p %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}
install -p -m 0755 hv_get_dhcp_info.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_get_dhcp_info
install -p -m 0755 hv_get_dns_info.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_get_dns_info
install -p -m 0755 hv_set_ifconfig.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_set_ifconfig
# Directory for pool files
mkdir -p %{buildroot}%{_sharedstatedir}/hyperv

# Tools
install -p -m 0755 lsvmbus %{buildroot}%{_sbindir}/
sed -i 's,#!/usr/bin/env python,#!%{__python3},' %{buildroot}%{_sbindir}/lsvmbus
install -p -m 0755 vmbus_testing %{buildroot}%{_sbindir}/

%post -n hypervkvpd
if [ $1 -gt 1 ] ; then
	# Upgrade
	systemctl --no-reload disable hypervkvpd.service >/dev/null 2>&1 || :
fi

%preun -n hypervkvpd
%systemd_preun hypervkvpd.service

%postun -n hypervkvpd
# hypervkvpd daemon does NOT support restarting (driver, neither)
%systemd_postun hypervkvpd.service
# If removing the package, delete %%{_sharedstatedir}/hyperv directory
if [ "$1" -eq "0" ] ; then
    rm -rf %{_sharedstatedir}/hyperv || :
fi


%post -n hypervvssd
if [ $1 -gt 1 ] ; then
	# Upgrade
	systemctl --no-reload disable hypervvssd.service >/dev/null 2>&1 || :
fi

%postun -n hypervvssd
%systemd_postun hypervvssd.service

%preun -n hypervvssd
%systemd_preun hypervvssd.service


%post -n hypervfcopyd
if [ $1 -gt 1 ] ; then
	# Upgrade
	systemctl --no-reload disable hypervfcopyd.service >/dev/null 2>&1 || :
fi

%postun -n hypervfcopyd
%systemd_postun hypervfcopyd.service

%preun -n hypervfcopyd
%systemd_preun hypervfcopyd.service


%files
# the base package does not contain any files.

%files -n hypervkvpd
%{_sbindir}/%{hv_kvp_daemon}
%{_unitdir}/hypervkvpd.service
%{_udevrulesdir}/%{udev_prefix}-hypervkvp.rules
%dir %{_libexecdir}/%{hv_kvp_daemon}
%{_libexecdir}/%{hv_kvp_daemon}/*
%dir %{_sharedstatedir}/hyperv

%files -n hypervvssd
%{_sbindir}/%{hv_vss_daemon}
%{_unitdir}/hypervvssd.service
%{_udevrulesdir}/%{udev_prefix}-hypervvss.rules

%files -n hypervfcopyd
%{_sbindir}/%{hv_fcopy_daemon}
%{_unitdir}/hypervfcopyd.service
%{_udevrulesdir}/%{udev_prefix}-hypervfcopy.rules

%files license
%doc COPYING

%files -n hyperv-tools
%{_sbindir}/lsvmbus
%{_sbindir}/vmbus_testing

%changelog
* Mon Jul 10 2023 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.42.20190303git
- hpvd-vmbus_testing-fix-wrong-python-syntax-for-integer-va.patch [bz#2218931]
- Resolves: bz#2218931
  ([Hyper-V] [RHEL-9] /usr/sbin/vmbus_testing python script prints: "SyntaxWarning: "is" with a literal.")

* Mon Nov 21 2022 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.41.20190303git
- hpvd-redhat-hv_set_if_config-Workaround-for-gateway-numbe.patch [bz#2122115]
- hpvd-tools-hv-Remove-an-extraneous-the.patch [bz#2139457]
- hpvd-tools-hv-kvp-remove-unnecessary-void-conversions.patch [bz#2139457]
- Resolves: bz#2122115
  ([Hyper-V][RHEL-9] Cannot set gateway properly when set static IPADDR0,NETMASK0,GATEWAY in ifcfg-eth0)
- Resolves: bz#2139457
  ([Hyper-V][RHEL9.2] Update Hyper-V-Daemons)

* Fri Jul 29 2022 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.40.20190303git
- hpvd-hypervkvpd.service-ordering-fixes.patch [bz#2103188]
- Resolves: bz#2103188
  ([Hyper-V][RHEL-9] hypervkvpd.service service ordering)

* Wed Dec 15 2021 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.39.20190303git
- hpvd-hv_set_ifconfig.sh-Use-nmcli-commands.patch [bz#2026371]
- hpvd-Use-filename-for-connection-profile.patch [bz#2026371]
- Resolves: bz#2026371
  ([RHEL9][Hyper-V]The /usr/libexec/hypervkvpd/hv_set_ifconfig need update for RHEL9 since the ifdown/ifup was not supported on RHEL9)

* Mon Nov 08 2021 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.38.20190303git
- hpvd-Enable-build-on-aarch64.patch [bz#2020148]
- Resolves: bz#2020148
  ([Hyper-V][RHEL9.0][ARM] No hyperv-daemons package built for aarch64 platform)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0-0.37.20190303git
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon May 10 2021 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.36.20190303git
- Synchronize RHEL 8 changes [rhbz#1957651]
- Resolves: rhbz#1957651
  ([Hyper-V][RHEL-9] Update build to rhel format and syncup RHEL 8 content for hyperv-daemons.)

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0-0.35.20190303git
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.34.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Tom Stellard <tstellar@redhat.com> - 0-0.31.20190303git
- Use __cc macro instead of hard-coding gcc

* Fri Nov 08 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.30.20190303git
- Rebase to 5.4-rc6
- Add IgnoreOnIsolate to systemd units

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.28.20190303git
- Rebase to 5.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20180415git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20180415git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.25.20180415git
- Switch lsvmbus to Python3

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 0-0.24.20180415git
- Added gcc as an explicit BuildRequires

* Thu Apr 19 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.23.20180415git
- Rebase to 4.17-rc1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.21.20170105git
- Rebase to 4.15-rc2, drop fedora patches as changes are upstream
- Start kvpd after network.target

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.17.20160728git
- Use '-gt' instead of '>' to do the right comparison (#1412033)

* Thu Jan 05 2017 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.16.20160728git
- Rebase to 4.9
- hyperv-tools subpackage added

* Thu Jul 28 2016 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.15.20160728git
- Rebase to 4.8-rc0 (20160728 git snapshot)
- Disable services and remove ConditionVirtualization, multi-user.target
  dependencies switching to udev-only activation (#1331577)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20150702git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.13.20150702git
- Add udev rules to properly restart services (#1195029)
- Spec cleanup

* Thu Jul 02 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.12.20150702git
- Rebase to 4.2-rc0 (20150702 git snapshot)
- Switch to new chardev-based communication layer (#1195029)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20150108git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.10.20150108git
- Rebase to 3.19-rc3 (20150108 git snapshot)
- Drop 'nodaemon' patches, use newly introduced '-n' option

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20140714git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Tomas Hozza <thozza@redhat.com> - 0-0.8.20140714git
- Update the File copy daemon to the latest git snapshot
- Fix hyperfcopyd.service to check for /dev/vmbus/hv_fcopy

* Wed Jun 11 2014 Tomas Hozza <thozza@redhat.com> - 0-0.7.20140611git
- Fix FTBFS (#1106781)
- Use kernel-headers instead of kernel-devel for building
- package new Hyper-V fcopy daemon as hypervfcopyd sub-package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20140219git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Tomas Hozza <thozza@redhat.com> - 0-0.5.20140219git
- rebase to the latest git snapshot next-20140219
  - KVP, VSS: removed inclusion of linux/types.h
  - VSS: Ignore VFAT mounts during freeze operation

* Fri Jan 10 2014 Tomas Hozza <thozza@redhat.com> - 0-0.4.20131022git
- provide 'hyperv-daemons' package for convenient installation of all daemons

* Tue Oct 22 2013 Tomas Hozza <thozza@redhat.com> - 0-0.3.20131022git
- rebase to the latest git snapshot next-20130927 (obtained 2013-10-22)
  - KVP, VSS: daemon use single buffer for send/recv
  - KVP: FQDN is obtained on start and cached

* Fri Sep 20 2013 Tomas Hozza <thozza@redhat.com> - 0-0.2.20130826git
- Use 'hypervkvpd' directory in libexec for KVP daemon scripts (#1010268)
- daemons are now WantedBy multi-user.target instead of basic.target (#1010260)

* Mon Aug 26 2013 Tomas Hozza <thozza@redhat.com> - 0-0.1.20130826git
- Initial package
