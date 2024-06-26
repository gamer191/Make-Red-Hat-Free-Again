Name:           perl-Module-CoreList
# Epoch to compete with perl.spec
Epoch:          1
Version:        5.20210320
Release:        3%{?dist}
Summary:        What modules are shipped with versions of perl
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Module-CoreList
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-CoreList-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Copy not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# feature not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(List::Util)
# Pod::Usage not used at tests
BuildRequires:  perl(version) >= 0.88
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(List::Util)
Requires:       perl(version) >= 0.88

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$

%description
Module::CoreList provides information on which core and dual-life modules
are shipped with each version of perl.

%package tools
Summary:        Tool for listing modules shipped with perl
Requires:       perl(feature)
Requires:       perl(version) >= 0.88
Requires:       perl-Module-CoreList = %{epoch}:%{version}-%{release}
# The files were distributed with perl.spec's subpackage
# perl-Module-CoreList <= 1:5.020001-309
Conflicts:      perl-Module-CoreList < 1:5.20140914

%description tools
This package provides a corelist(1) tool which can be used to query what
modules were shipped with given perl version.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-tools = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Module-CoreList-%{version}

# Help file to recognise the Perl scripts and normalize shebangs
for F in t/*.t; do
    if head -1 "$F" | grep -q -e '^#!.*perl' ; then
        perl -MConfig -pi -e 's|^#!.*perl\b|$Config{startperl}|' "$F"
    else
        perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    fi
    chmod +x "$F"
done

# Remove release tests
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod\.t}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

# Install tests
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset PERL_CORE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tools
%doc README
%{_bindir}/corelist
%{_mandir}/man1/corelist.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:5.20210320-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:5.20210320-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Sun Mar 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20210320-1
- 5.20210320 bump

* Mon Feb 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20210220-1
- 5.20210220 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20210123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20210123-1
- 5.20210123 bump

* Thu Jan 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20210120-1
- 5.20210120 bump

* Mon Dec 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20201220-1
- 5.20201220 bump

* Fri Nov 20 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20201120-1
- 5.20201120 bump

* Wed Oct 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20201020-1
- 5.20201020 bump

* Mon Sep 21 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20200920-1
- 5.20200920 bump

* Fri Aug 21 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200820-1
- 5.20200820 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20200717-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200717-1
- 5.20200717 bump

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20200620-457
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20200620-456
- Increase release to favour standalone package

* Mon Jun 22 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200620-1
- 5.20200620 bump

* Tue Jun 09 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200603-1
- 5.20200603 bump

* Tue Jun 02 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200602-1
- 5.20200602 bump

* Wed Apr 29 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200428-1
- 5.20200428 bump

* Mon Mar 23 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200320-1
- 5.20200320 bump

* Mon Mar 16 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200314-1
- 5.20200314 bump

* Fri Feb 21 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200220-1
- 5.20200220 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20200120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20200120-1
- 5.20200120 bump

* Thu Jan 02 2020 Petr Pisar <ppisar@redhat.com> - 1:5.20191220-1
- 5.20191220 bump

* Thu Nov 21 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20191120-1
- 5.20191120 bump

* Mon Nov 11 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20191110-1
- 5.20191110 bump

* Mon Oct 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20191020-1
- 5.20191020 bump

* Mon Sep 23 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190920-1
- 5.20190920 bump

* Wed Aug 21 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190820-1
- 5.20190820 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20190720-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190720-1
- 5.20190720 bump

* Fri Jun 21 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190620-1
- 5.20190620 bump

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20190524-3
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20190524-2
- Perl 5.30 rebuild

* Mon May 27 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190524-1
- 5.20190524 bump

* Wed May 22 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190522-1
- 5.20190522 bump

* Tue Apr 23 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190420-1
- 5.20190420 bump

* Thu Mar 21 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190320-1
- 5.20190320 bump

* Thu Feb 21 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190220-1
- 5.20190220 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20190120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Petr Pisar <ppisar@redhat.com> - 1:5.20190120-1
- 5.20190120 bump

* Wed Dec 19 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20181218-1
- 5.20181218 bump

* Mon Dec 03 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20181130-1
- 5.20181130 bump

* Wed Nov 21 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20181120-1
- 5.20181120 bump

* Tue Oct 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20181020-1
- 5.20181020 bump

* Fri Sep 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20180920-1
- 5.20180920 bump

* Tue Aug 21 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180820-1
- 5.20180820 bump

* Mon Jul 23 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180720-1
- 5.20180720 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20180626-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20180626-2
- Perl 5.28 re-rebuild of bootstrapped packages

* Thu Jun 28 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180626-1
- 5.20180626 bump

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20180622-416
- Increase release to favour standalone package

* Mon Jun 25 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180622-1
- 5.20180622 bump

* Mon Apr 23 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180420-1
- 5.20180420 bump

* Fri Apr 20 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180415-1
- 5.20180415 bump

* Mon Apr 16 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180414-1
- 5.20180414 bump

* Fri Apr 13 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180414-0.1.RC1
- 5.20180414_26 bump

* Wed Mar 21 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180221-1
- 5.20180221 bump

* Wed Feb 21 2018 Petr Pisar <ppisar@redhat.com> - 1:5.20180220-1
- 5.20180220 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20180120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20180120-1
- 5.20180120 bump

* Fri Dec 22 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20171220-1
- 5.20171220 bump

* Tue Nov 21 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20171120-1
- 5.20171120 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20171020-1
- 5.20171020 bump

* Mon Sep 25 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170923-1
- 5.20170923 bump

* Thu Sep 21 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170920-1
- 5.20170920 bump

* Tue Aug 22 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170821-1
- 5.20170821 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20170720-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170720-1
- 5.20170720 bump

* Mon Jul 17 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170715-1
- 5.20170715 bump

* Tue Jun 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20170621-1
- 5.20170621 bump

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20170531-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20170531-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170531-1
- 5.20170531 bump

* Wed May 31 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170530-1
- 5.20170530 bump

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170520-0.1
- Upgrade to 5.20170520 as provided in perl's blead git branch

* Fri Apr 21 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170420-1
- 5.20170420 bump

* Tue Mar 21 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170320-1
- 5.20170320 bump

* Tue Feb 21 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170220-1
- 5.20170220 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20170120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170120-1
- 5.20170120 bump

* Mon Jan 16 2017 Petr Pisar <ppisar@redhat.com> - 1:5.20170115-1
- 5.20170115 bump

* Wed Dec 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20161220-1
- 5.20161220 bump

* Mon Nov 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20161120-1
- 5.20161120 bump

* Fri Oct 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20161020-1
- 5.20161020 bump

* Wed Sep 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160920-1
- 5.20160920 bump

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160820-1
- 5.20160820 bump

* Fri Aug 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20160720-2
- Avoid loading optional modules from default . (CVE-2016-1238)

* Thu Jul 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160720-1
- 5.20160720 bump

* Tue Jun 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160620-1
- 5.20160620 bump

* Mon May 23 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160520-1
- 5.20160520 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20160507-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20160507-2
- Perl 5.24 rebuild

* Tue May 10 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160507-1
- 5.20160507 bump

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160429-1
- 5.20160429 bump

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160320-1
- 5.20160320 bump

* Mon Feb 22 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160121-1
- 5.20160121 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20160120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160120-1
- 5.20160120 bump

* Tue Dec 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20151220-1
- 5.20151220 bump

* Mon Dec 14 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20151213-1
- 5.20151213 bump

* Mon Nov 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20151120-1
- 5.20151120 bump

* Thu Oct 22 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20151020-1
- 5.20151020 bump

* Mon Sep 21 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150920-1
- 5.20150920 bump

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150912-1
- 5.20150912 bump

* Tue Aug 25 2015 Tom Callaway <spot@fedoraproject.org> - 1:5.20150820-1
- 5.20150820 bump

* Tue Jul 21 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150720-1
- 5.20150720 bump

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150620-1
- 5.20150620 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.20150520-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20150520-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20150520-2
- Perl 5.22 rebuild

* Tue Jun 02 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150520-1
- 5.20150520 bump

* Tue Apr 21 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150420-1
- 5.20150420 bump

* Mon Mar 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150320-1
- 5.20150320 bump

* Mon Feb 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150220-1
- 5.20150220 bump

* Mon Feb 16 2015 Tom Callaway <spot@fedoraproject.org> - 1:5.20150214-1
- 5.20150214 bump

* Fri Jan 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150120-1
- 5.20150120 bump

* Fri Jan 02 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20141220-1
- 5.20141220 bump

* Tue Nov 25 2014 Petr Pisar <ppisar@redhat.com> - 1:5.20141120-1
- 5.20141120 bump

* Tue Oct 21 2014 Petr Pisar <ppisar@redhat.com> - 1:5.20141020-1
- 5.20141020 bump

* Wed Oct 08 2014 Petr Pisar <ppisar@redhat.com> - 1:5.20141002-1
- 5.20141002 bump

* Wed Sep 17 2014 Petr Pisar <ppisar@redhat.com> 1:5.20140914-1
- Specfile autogenerated by cpanspec 1.78.
