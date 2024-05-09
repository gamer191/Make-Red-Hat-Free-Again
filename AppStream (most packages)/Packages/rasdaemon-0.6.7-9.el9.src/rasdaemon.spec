Name:			rasdaemon
Version:		0.6.7
Release:		9%{?dist}
Summary:		Utility to receive RAS error tracings
License:		GPLv2
URL:			http://git.infradead.org/users/mchehab/rasdaemon.git
Source0:		http://www.infradead.org/~mchehab/rasdaemon/%{name}-%{version}.tar.bz2
Patch0: labels.patch
Patch1: fcdffdcb28ece67ed78e3575a3dce45d9dd4f015.patch
Patch2: f7cdd720297cd17e405a7170c04df89d1d9536f8.patch
Patch3: 2b37a26dcec389723f75d69d3da9c2f15f6c317d.patch
Patch4: dda7d95bcbbb95e0db557a7a9325ee9815ab4e9b.patch
Patch5: 738bafafdcb2e8b0ced32fff31b13754d571090b.patch
Patch6: 1ff5f3d2a0fcd48add9462567c30fe0e14585fb4.patch
Patch7: 9acef39f13833f7d53ef96abc5a72e79384260f4.patch
Patch8: 28ea956acc2dab7c18b4701f9657afb9ab3ddc79.patch
Patch9: aecf33aa70331670c06db6b652712b476e24051c.patch
Patch10: 7937f0d6c2aaaed096f3a3d306416743c0dcb7a4.patch
Patch11: ec443ec0add059fa897f844349e1a2345d81713c.patch
Patch12: 9a5baed97b21af31064d9995ffcfaac0e9d7983e.patch
Patch13: b4402d36e1b42fb7b0d8ddccc83463a6e622dbc4.patch
Patch14: 50565005b10fe909c66f1c90f2feb95712427c7d.patch
Patch15: fc1dd37d422fc907416afd028514fff59b63ae12.patch
Patch16: 6bc43db1b6b3d73805179c21d1dd5521e8dc0f74.patch
Patch17: 2b6a54b0d31e02e657171fd27f4e31d996756bc6.patch
Patch18: 7ccf12f5ae26a055926d175d908c7930293438c4.patch
Patch19: 9415b7449c70f5ea4a0209ddb89c2f5f392d3b4b.patch
Patch20: d0e0bb3d73c4bc5060da20270a089857bba2a64c.patch
Patch21: 30158ef8d7aebc3e5201bf39b73ce7644f8e419e.patch
Patch22: aa36c96cd52d775570dae989dd95a060f1149077.patch
Patch23: 932118b04a04104dfac6b8536419803f236e6118.patch
Patch24: 1f74a59ee33b7448b00d7ba13d5ecd4918b9853c.patch
Patch25: 2d15882a0cbfce0b905039bebc811ac8311cd739.patch
Patch26: c785d309dcbdeb7ecd219975244f3944a8d047e9.patch
Patch27: b6a64416ab31b66ce92cabcc7fa1f3c5e9db2e87.patch

ExcludeArch:		s390 s390x
BuildRequires:		make
BuildRequires:		gcc
BuildRequires:		gettext-devel
BuildRequires:		perl-generators
BuildRequires:		sqlite-devel
BuildRequires:		systemd
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
Provides:		bundled(kernel-event-lib)
Requires:		hwdata
Requires:		perl-DBD-SQLite
%ifarch %{ix86} x86_64
Requires:		dmidecode
%endif

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
%{name} is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC is drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like arm also exists.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
an utility for reporting current error counts from the EDAC sysfs files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1

# The tarball is locked in time the first time aclocal was ran and will keep
# requiring an older version of automake
autoreconf -vfi

%build
%ifarch %{arm} aarch64
%configure --enable-sqlite3 --enable-aer --enable-mce --enable-extlog --enable-devlink --enable-diskerror --enable-abrt-report --enable-non-standard --enable-arm --enable-hisi-ns-decode
%else
%configure --enable-sqlite3 --enable-aer --enable-mce --enable-extlog --enable-devlink --enable-diskerror --enable-abrt-report
%endif
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -p -m 0644 misc/rasdaemon.service %{buildroot}/%{_unitdir}/rasdaemon.service
install -D -p -m 0644 misc/ras-mc-ctl.service %{buildroot}%{_unitdir}/ras-mc-ctl.service
rm INSTALL %{buildroot}/usr/include/*.h
mkdir -p %{buildroot}/%{_sharedstatedir}/rasdaemon
install -d -p -m 0755 %{buildroot}/%{_sharedstatedir}/rasdaemon
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
install -D -p -m 0644 misc/rasdaemon.env %{buildroot}/%{_sysconfdir}/sysconfig/rasdaemon
sed -i "s/^PAGE_CE_ACTION=.*/PAGE_CE_ACTION=account/" %{buildroot}/%{_sysconfdir}/sysconfig/rasdaemon

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_sbindir}/rasdaemon
%{_sbindir}/ras-mc-ctl
%{_mandir}/*/*
%{_unitdir}/*.service
%{_sharedstatedir}/rasdaemon
%{_sysconfdir}/ras/dimm_labels.d
%{_sysconfdir}/sysconfig/rasdaemon

%changelog
* Thu Oct 26 2023 Aristeu Rozanski <aris@redhat.com> 0.6.7-9
- Update SMCA support for AMD processors [RHEL-11092]

* Tue May 03 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-8
- Update ras-mc-ctl manpage to match current options [2079132]

* Mon May 02 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-7
- Fix issue printing memory module sizes [2080596]

* Thu Mar 31 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-6
- Merging 2065729 fixes into 9.1 branch [2067499]

* Thu Mar 24 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-5
- Trying to guess what's going on on the testing side [2065729]

* Thu Mar 24 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-4
- Adding simple test to stop being gated [2065729]

* Thu Mar 24 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-3
- Adding gating.yaml [2065729]

* Fri Mar 18 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-2
- Adding missing rasdaemon environment configuration to /etc/sysconfig/rasdaemon [2065729]

* Tue Feb 08 2022 Aristeu Rozanski <aris@redhat.com> 0.6.7-1
- Bumped to 0.6.7
- Backported patches that sit on top of 0.6.7 without being released
  Related: rhbz#2052190

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.6.4-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.6.4-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild


* Thu Oct 10 2019 Mauro Carvalho Chehab <mchehab+samsung@kernel.org>  0.6.4-1
- Bump to version 0.6.4 with some DB changes for hip08 and some fixes

* Fri Aug 23 2019 Mauro Carvalho Chehab <mchehab+samsung@kernel.org>  0.6.3-1
- Bump to version 0.6.3 with new ARM events, plus disk I/O and netlink support

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org>  0.6.2-1
- Bump to version 0.6.2 with improvements for PCIe AER parsing and at ras-mc-ctl tool

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org>  0.6.1-1
- Bump to version 0.6.1 adding support for Skylake Xeon MSCOD, a bug fix and some new DELL labels

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Mauro Carvalho Chehab <mchehab@osg.samsung.com>  0.6.0-1
- Bump to version 0.6.0 adding support for Arm and Hisilicon events and update Dell Skylate labels

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 Mauro Carvalho Chehab <mchehab@osg.samsung.com> 0.5.8-3
- Add a virtual provide, per BZ#104132

* Fri Apr 15 2016 Mauro Carvalho Chehab <mchehab@osg.samsung.com> 0.5.8-2
- Bump to version 0.5.8 with support for Broadwell EP/EX MSCOD/DE MSCOD

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 03 2015 Mauro Carvalho Chehab <mchehab@osg.samsung.com> 0.5.6-1
- Bump to version 0.5.6 with support for LMCE and some fixes

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Mauro Carvalho Chehab <mchehab@osg.samsung.com> 0.5.5-1
- Bump to version 0.5.5 with support for newer Intel platforms & some fixes

* Tue Sep 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.4-3
- aarch64/ppc64 have edac capabilities
- spec cleanups
- No need to run autoreconf

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Mauro Carvalho Chehab <m.chehab@samsung.com> 0.5.4-1
- Bump to version 0.5.4 with some fixes, mainly for amd64

* Sun Aug 10 2014 Mauro Carvalho Chehab <m.chehab@samsung.com> 0.5.3-1
- Bump to version 0.5.3 and enable ABRT and ExtLog

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Mauro Carvalho Chehab <m.chehab@samsung.com> 0.5.2-1
- fix and enable ABRT report support

* Fri Mar 28 2014 Mauro Carvalho Chehab <m.chehab@samsung.com> 0.5.1-1
- Do some fixes at the service files and add some documentation for --record

* Sun Feb 16 2014  Mauro Carvalho Chehab <m.chehab@samsung.com> 0.5.0-1
- Add experimental ABRT support

* Tue Sep 10 2013 Mauro Carvalho Chehab <m.chehab@samsung.com> 0.4.2-1
- Fix ras-mc-ctl layout filling

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.4.1-4
- Perl 5.18 rebuild

* Sun Jun  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.4.1-3
- ARM has EDMA drivers (currently supported in Calxeda highbank)

* Wed May 29 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.1-2
- Fix the name of perl-DBD-SQLite package

* Wed May 29 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.1-1
- Updated to version 0.4.1 with contains some bug fixes

* Tue May 28 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.4.0-1
- Updated to version 0.4.0 and added support for mce, aer and sqlite3 storage

* Mon May 20 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.3.0-1
- Package created

