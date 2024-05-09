Name:		pgaudit
Version:	1.7.0
Release:	1%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

Source0:	https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: postgresql-server-devel >= 15
BuildRequires: openssl-devel

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
%{_datadir}/pgsql/extension/%{name}--1*.sql
%{_datadir}/pgsql/extension/%{name}.control


%changelog
* Wed Oct 19 2022 Filip Janus <fjanus@redhat.com> - 1.7.0-1
- Initial import for postgresql 15 module
- Update to 1.7.0
- Support postgresql 15
- Related: #2128410
