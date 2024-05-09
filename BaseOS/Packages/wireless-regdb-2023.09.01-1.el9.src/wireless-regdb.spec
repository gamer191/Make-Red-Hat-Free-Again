%global         _firmwarepath    /usr/lib/firmware

Name:           wireless-regdb
Version:        2023.09.01
Release:        1%{?dist}
Summary:        Regulatory database for 802.11 wireless networking

License:        ISC
URL:            https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
BuildArch:      noarch

Requires:       udev, iw
Requires:       systemd >= 190

BuildRequires: make
BuildRequires:  systemd-devel

Provides:       crda = 3.19-1
Obsoletes:      crda < 3.19-1

Source0:        http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-%{version}.tar.xz
Source1:        setregdomain
Source2:        setregdomain.1
Source3:        85-regulatory.rules


%description
The wireless-regdb package provides the regulatory rules database
used by the kernels 802.11 networking stack in order to comply 
with radio frequency regulatory rules around the world.


%prep
%setup -q


%build
: # Package installs a firmware-like, prebuilt binary from upstream...


%install
make install DESTDIR=%{buildroot} MANDIR=%{_mandir} \
	FIRMWARE_PATH=%{_firmwarepath}

install -D -pm 0755 %SOURCE1 %{buildroot}%{_sbindir}/setregdomain
install -D -pm 0644 %SOURCE2 %{buildroot}%{_mandir}/man1/setregdomain.1
install -D -pm 0644 %SOURCE3 %{buildroot}%{_udevrulesdir}/85-regulatory.rules

rm -rf %{buildroot}/usr/lib/crda


%files
%{_sbindir}/setregdomain
%{_udevrulesdir}/85-regulatory.rules
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s
%{_mandir}/man1/setregdomain.1*
%{_mandir}/man5/regulatory.db.5*
%{_mandir}/man5/regulatory.bin.5*
%license LICENSE
%doc README


%changelog
* Wed Sep 06 2023 Jose Ignacio Tornos Martinez <jtornosm@redhat.com> - 2023.09.01-1
- Update to version 2023.09.01 from upstream
- Resolves: RHEL-2362

* Mon Nov 22 2021 Michal Schmidt <mschmidt@redhat.com> - 2020.11.20-6
- To let the Obsoletes fix land, enable gating, bump release.
- Resolves: rhbz#1997398

* Thu Nov 18 2021 Michal Schmidt <mschmidt@redhat.com> - 2020.11.20-5
- Update crda Provides/Obsoletes to cover the version in RHEL 8.
- Resolves: rhbz#1997398

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2020.11.20-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2020.11.20-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.11.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 09 2020 John W. Linville <linville@redhat.com> - 2020.11.20-1
- Update to version 2020.11.20 from upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 John W. Linville <linville@redhat.com> - 2020.04.29-1
- Update to version 2020.04.29 from upstream

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.06.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 John W. Linville <linville@redhat.com> - 2019.06.03-5
- Remove patch preventing install of regulatory.bin.5 man page
- Include regulatory.bin.5 man page in distributed files

* Mon Aug 26 2019 John W. Linville <linville@redhat.com> - 2019.06.03-4
- Bump crda Provides and Obsoletes to ensure proper upgrades

* Mon Aug 05 2019 John W. Linville <linville@redhat.com> - 2019.06.03-3
- remove Requires for kernel

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.06.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 John W. Linville <linville@redhat.com> - 2019.06.03-1
- Update to version 2019.06.03 from upstream

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.05.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 John W. Linville <linville@redhat.com> - 2018.05.31-4
- Enable Provides for crda so as to promote automated upgrades

* Wed Jul 18 2018 John W. Linville <linville@redhat.com> - 2018.05.31-3
- Fix-up changelog typos and bump Release

* Wed Jul 18 2018 John W. Linville <linville@redhat.com> - 2018.05.31-2
- Add BuildRequires for systemd-devel to provide _udevrulesdir definition

* Fri Jul 06 2018 John W. Linville <linville@redhat.com> - 2018.05.31-1
- Initial build
