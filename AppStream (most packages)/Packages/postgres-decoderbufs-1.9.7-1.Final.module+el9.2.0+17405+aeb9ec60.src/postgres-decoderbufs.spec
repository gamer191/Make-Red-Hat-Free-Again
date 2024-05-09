%global pre Final

Name:		postgres-decoderbufs
Version:	1.9.7
Release:	1%{?pre:.%pre}%{?dist}
Summary:	PostgreSQL Protocol Buffers logical decoder plugin

License:	MIT
URL:		https://github.com/debezium/postgres-decoderbufs

%global full_version %{version}.%{?pre:%pre}%{?!pre:Final}

Source0:	https://github.com/debezium/%{name}/archive/v%{full_version}.tar.gz

BuildRequires: 	make
BuildRequires:	gcc
BuildRequires:	postgresql-server-devel >= 15
BuildRequires:	protobuf-c-devel

Requires:	protobuf-c
%{?postgresql_module_requires}

%description
A PostgreSQL logical decoder output plugin to deliver data as Protocol Buffers messages.


%if 0%{?postgresql_server_llvmjit}
%package llvmjit
Summary:	Just-in-time compilation support for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description llvmjit
Just-in-time compilation support for %{name}.
%endif


%prep
%setup -qn postgres-decoderbufs-%{full_version}


%build
%make_build


%install
%make_install


%files
%doc README.md
%license LICENSE
%{_libdir}/pgsql/decoderbufs.so
%{_datadir}/pgsql/extension/decoderbufs.control

%if 0%{?postgresql_server_llvmjit}
%files llvmjit
%{_libdir}/pgsql/bitcode/decoderbufs.index.bc
%{_libdir}/pgsql/bitcode/decoderbufs/
%endif


%changelog
* Wed Oct 26 2022 Filip Janus <fjanus@redhat.com> - 1.9.7-1.Final
- Iitial import for postgresql 15 stream
- Related: #2128410

