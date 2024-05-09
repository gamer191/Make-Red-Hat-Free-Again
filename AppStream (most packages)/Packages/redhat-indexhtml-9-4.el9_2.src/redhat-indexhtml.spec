Summary: Browser default start page for Red Hat Enterprise Linux
Name: redhat-indexhtml
Version: 9
Release: 4%{?dist}
# There is no upstream for this project.
Source: %{name}-%{version}-3.tar.gz
License: CC-BY-SA
URL: https://access.redhat.com/products/red-hat-enterprise-linux/
Group: Documentation
BuildArchitectures: noarch

%description
The redhat-indexhtml package provides a welcome page shown by a web browser
after successful installation of Red Hat Enterprise Linux.

This web page advises users on how to register their Red Hat software and how
to get any support they might need.

%prep
%setup -q -n HTML

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

%files
%{_defaultdocdir}/HTML/*

%changelog
* Wed Mar 29 2023 Petr Kovar <pkovar@redhat.com> - 9-4
- Resolves: rhbz 2145165

* Thu Sep 01 2022 Petr Kovar <pkovar@redhat.com> - 9-3
- Fix translations
- Resolves: rhbz 2074078

* Tue Feb 01 2022 Petr Kovar <pkovar@redhat.com> - 9-2
- Update translations
- Resolves: rhbz 1999613
- Resolves: rhbz 2040651

* Mon Aug 30 2021 Petr Kovar <pkovar@redhat.com> - 9-1
- Fix License to conform to the Red Hat product documentation license
- Resolves: rhbz 1931544

* Mon Aug 30 2021 Petr Kovar <pkovar@redhat.com> - 9-0
- New content tarball for RHEL 9
- Resolves: rhbz 1931544

* Mon Jan 14 2019 Petr Kovar <pkovar@redhat.com> - 8-7
- New content tarball for RHEL 8.0 GA
- Update translations
- Resolves: rhbz 1661332

* Tue Dec 18 2018 Petr Kovar <pkovar@redhat.com> - 8-6
- New content tarball for RHEL 8 Beta
- Fix additional translations
- Resolves: rhbz 1644637

* Mon Dec 17 2018 Petr Kovar <pkovar@redhat.com> - 8-5
- New content tarball for RHEL 8 Beta
- Add additional translations
- Resolves: rhbz 1644637

* Fri Oct 12 2018 Petr Kovar <pkovar@redhat.com> - 8-4
- New content tarball for RHEL 8 Beta to fix fr-FR
- Resolves: rhbz1562063

* Fri Sep 07 2018 Petr Kovar <pkovar@redhat.com> - 8-3
- New content tarball for RHEL 8 Beta
- Remove outdated translations
- Update fr-FR, ja-JP, ko-KR and zh-CN translations
- Remove unneeded files
- Change file permissions to 644
- Update description
- Resolves: rhbz1562063

* Thu Aug 16 2018 Petr Kovar <pkovar@redhat.com> - 8-2
- New content tarball for RHEL 8 Beta.
- Resolves: rhbz1562063

* Tue Oct 24 2017 Merlin Mathesius <mmathesi@redhat.com> - 8-1
- Initial conversion of package for RHEL8 alpha.

* Wed May 21 2014 Paul W. Frields <pfrields@redhat.com> - 7-11
- Bump release for rebuild

* Wed May 21 2014 Paul W. Frields <pfrields@redhat.com> - 7-10
- Fix for unsupported locale

* Thu May 15 2014 Paul W. Frields <pfrields@redhat.com> - 7-9
- New content tarball to fix errant translation files (Resolves: rhbz1055849)
- Remove obsolete feedback.html and unsupported locale

* Fri Mar 28 2014 Paul W. Frields <pfrields@redhat.com> - 7-8
- Strip obsolete HTML files (BZ#1059300)

* Wed Mar 05 2014 Paul W. Frields <pfrields@redhat.com> - 7-7
- New content tarball

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 7-5
- Mass rebuild 2013-12-27

* Tue Nov 19 2013 Ruediger Landmann <rlandmann@redhat.com> - 7-4
- update URLs for 7-Beta (BZ#1031104)

* Tue Aug 27 2013 Jens Petersen <petersen@redhat.com> - 7-3
- move common/ subdirs into HTML/

* Fri Feb 22 2013 Ruediger Landmann <rlandmann@redhat.com> - 7-2
- rm stray tarball (BZ#799063)

* Tue Jun 26 2012 Ruediger Landmann <rlandmann@redhat.com> - 7-1
- Rebuild for RHEL7 (BZ#799063)

* Fri Aug 27 2010 Parag Nemade <pnemade AT redhat.com> - 6-1
- Respin the tarball to include translated pages (#626997)

* Thu Aug 26 2010 Parag Nemade <pnemade AT redhat.com> - 6-0.7
- final English content (#626997)

* Thu Jul 29 2010 Parag Nemade <pnemade AT redhat.com> - 6-0.6
- Resolves:-rh#578072-index.html page is not localized. showing en-US/index.html page 

* Wed May 12 2010 Michael Hideo <mhideo@redhat.com> - 6-0.5
- BZ#578072
- New content payload from pm group

* Thu Apr 15 2010 Jens Petersen <petersen@redhat.com>
- dont install the tarball
- update localized index.html files to show "6 Beta"

* Mon Feb 15 2010 Michael Hideo <mhideo@redhat.com> - 6-0.2
- enabling i18n

* Thu Feb  4 2010 Jens Petersen <petersen@redhat.com> - 6-0.1
- rename from indexhtml to redhat-indexhtml
- redirect to beta page

* Tue Aug 08 2006 Phil Knirsch <pknirsch@redhat.com> 5-1
- Minor cleanup to specfile
- Bumped version and release properly for RHEL5

* Fri Jul 29 2005 Bill Nottingham <notting@redhat.com> 4.1-1
- Russian (#160605)

* Tue Nov 30 2004 Bill Nottingham <notting@redhat.com> 4-2
- initial translations

* Mon Nov 22 2004 Bill Nottingham <notting@redhat.com> 4-0.1
- initial build for RHEL 4
