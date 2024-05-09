Name:		pgaudit
Version:	1.5.0
Release:	6%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

Source0:	https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	postgresql-server-devel >= 13, postgresql-server-devel < 14
BuildRequires:	openssl-devel

%{?postgresql_module_requires}

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.


%prep
%setup -q -n %{name}-%{version}


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{name}.so
%{_datadir}/pgsql/extension/%{name}--1.5.sql
%{_datadir}/pgsql/extension/%{name}.control


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.5.0-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 22 2021 Mohan Boddu <mboddu@redhat.com> - 1.5.0-5
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Thu Apr 22 2021 Honza Horak <hhorak@redhat.com> - 1.5.0-4
- Remove llvmjit parts
  Resolves: #1951268

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com>
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.5.0-2
- rebuild for libpq ABI fix rhbz#1908268

* Fri Feb  5 2021 Honza Horak <hhorak@redhat.com> - 1.5.0-1
- Update to 1.5.0 for PostgreSQL 13 support

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 13 2020 Devrim Gündüz <devrim@gunduz.org> - 1.4.0-1
- Update to 1.4.0 for PostgreSQL 12 support

* Sun Mar 08 2020 Patrik Novotný <panovotn@redhat.com> - 1.3.0-5
- Rebuild for PostgreSQL 12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Petr Kubat <pkubat@redhat.com> - 1.3.0-1
- rebase to latest upstream release

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 1.2.0-4
- rebuild against postgresql-server-devel (rhbz#1618698)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 - Filip Čáp <ficap@redhat.com> 1.2.0-1
- Initial RPM packaging for Fedora
- Based on Devrim Gündüz's packaging for PostgreSQL RPM Repo

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository
