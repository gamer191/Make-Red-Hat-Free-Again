%define rsyslog_statedir %{_sharedstatedir}/rsyslog
%define rsyslog_pkidir %{_sysconfdir}/pki/rsyslog
%define rsyslog_docdir %{_docdir}/rsyslog

Summary: Enhanced system logging and kernel message trapping daemon
Name: rsyslog
Version: 8.2310.0
Release: 4%{?dist}
License: (GPLv3+ and ASL 2.0)
URL: http://www.rsyslog.com/
Source0: http://www.rsyslog.com/files/download/rsyslog/%{name}-%{version}.tar.gz
Source1: http://www.rsyslog.com/files/download/rsyslog/%{name}-doc-%{version}.tar.gz
Source2: rsyslog.conf
Source3: rsyslog.sysconfig
Source4: rsyslog.log
Source5: rsyslog.service
# Add qpid-proton as another source, enable omamqp1 module in a
# separatae sub-package with it statically linked(see rhbz#1713427)
Source6: qpid-proton-0.39.0.tar.gz

Patch1: rsyslog-8.1911.0-rhbz1659898-imjournal-default-tag-v2.patch
Patch2: rsyslog-8.2102.0-rhbz1886400-reduce-default-timeout.patch
Patch3: rsyslog-8.2310.0-do-not-preserve-statefile-on-file-move.patch
Patch4: rsyslog-8.2310.0-do-not-preserve-statefile-on-file-move-doc.patch
Patch5: rsyslog-8.2310.0-remove-state-on-file-delete.patch
Patch6: rsyslog-8.2310.0-omprog-binary-path.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: dos2unix
BuildRequires: flex
BuildRequires: libgcrypt-devel
BuildRequires: libfastjson-devel >= 0.99.8
BuildRequires: libestr-devel >= 0.1.9
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: pkgconfig
BuildRequires: python3-docutils
# make sure systemd is in a version that isn't affected by rhbz#974132
BuildRequires: systemd-devel >= 204-8
BuildRequires: zlib-devel
BuildRequires: libcap-ng-devel

Conflicts: selinux-policy < 38.1.29-1

Recommends: %{name}-logrotate = %version-%release
Requires: bash >= 2.0
%{?systemd_ordering}

Provides: syslog
Obsoletes: sysklogd < 1.5-11

%package logrotate
Summary: Log rotation for rsyslog
Requires: %name = %version-%release
Requires: logrotate >= 3.5.2

%package crypto
Summary: Encryption support
Requires: %name = %version-%release

%package doc
Summary: HTML documentation for rsyslog
BuildArch: noarch

%package elasticsearch
Summary: ElasticSearch output module for rsyslog
Requires: %name = %version-%release
BuildRequires: libcurl-devel

%package mmfields
Summary: Fields extraction module
Requires: %name = %version-%release

%package mmjsonparse
Summary: JSON enhanced logging support
Requires: %name = %version-%release

%package mmnormalize
Summary: Log normalization support for rsyslog
Requires: %name = %version-%release
BuildRequires: libestr-devel liblognorm-devel >= 1.0.2

%package mmaudit
Summary: Message modification module supporting Linux audit format
Requires: %name = %version-%release

%package mmsnmptrapd
Summary: Message modification module for snmptrapd generated messages
Requires: %name = %version-%release

%package mysql
Summary: MySQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: mariadb-connector-c-devel

%package pgsql
Summary: PostgresSQL support for rsyslog
Requires: %name = %version-%release
BuildRequires: libpq-devel

%package gssapi
Summary: GSSAPI authentication and encryption support for rsyslog
Requires: %name = %version-%release
BuildRequires: krb5-devel

%package relp
Summary: RELP protocol support for rsyslog
Requires: %name = %version-%release
Requires: librelp >= 1.9.0
BuildRequires: librelp-devel >= 1.9.0

%package gnutls
Summary: TLS protocol support for rsyslog via GnuTLS library
Requires: %name = %version-%release
BuildRequires: gnutls-devel

%package openssl
Summary: TLS protocol support for rsyslog via OpenSSL library
Group: System Environment/Daemons
Requires: %name = %version-%release
BuildRequires: openssl-devel

%package snmp
Summary: SNMP protocol support for rsyslog
Requires: %name = %version-%release
BuildRequires: net-snmp-devel

%package udpspoof
Summary: Provides the omudpspoof module
Requires: %name = %version-%release
BuildRequires: libnet-devel

%package omamqp1
Summary: Provides the omamqp1 module
Requires: %name = %version-%release
Requires: cyrus-sasl-lib
Requires: openssl-libs
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cyrus-sasl-devel
BuildRequires: openssl-devel
BuildRequires: python3

%package kafka
Summary: Provides the omkafka module
Requires: %name = %version-%release
BuildRequires: librdkafka-devel

%package mmkubernetes
Summary: Provides the mmkubernetes module
Requires: %name = %version-%release
BuildRequires: libcurl-devel

%description
Rsyslog is an enhanced, multi-threaded syslog daemon. It supports MySQL,
syslog/TCP, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is compatible with stock sysklogd
and can be used as a drop-in replacement. Rsyslog is simple to set up, with
advanced features suitable for enterprise-class, encryption-protected syslog
relay chains.

%description logrotate
This subpackage contains the default logrotate configuration for rsyslog.

%description crypto
This package contains a module providing log file encryption and a
command line tool to process encrypted logs.

%description doc
This subpackage contains documentation for rsyslog.

%description elasticsearch
This module provides the capability for rsyslog to feed logs directly into
Elasticsearch.

%description mmjsonparse
This module provides the capability to recognize and parse JSON enhanced
syslog messages.

%description mmnormalize
This module provides the capability to normalize log messages via liblognorm.

%description mmaudit
This module provides message modification supporting Linux audit format
in various settings.

%description mmsnmptrapd
This message modification module takes messages generated from snmptrapd and
modifies them so that they look like they originated from the read originator.

%description mmfields
The mmfield module permits to extract fields. Using this module is of special
advantage if a field-based log format is to be processed, like for example CEF
and either a large number of fields is needed or a specific field is used multiple
times inside filters.

%description mysql
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.

%description pgsql
The rsyslog-pgsql package contains a dynamic shared object that will add
PostgreSQL database support to rsyslog.

%description gssapi
The rsyslog-gssapi package contains the rsyslog plugins which support GSSAPI
authentication and secure connections. GSSAPI is commonly used for Kerberos
authentication.

%description relp
The rsyslog-relp package contains the rsyslog plugins that provide
the ability to receive syslog messages via the reliable RELP
protocol.

%description gnutls
The rsyslog-gnutls package contains the rsyslog plugins that provide the
ability to send and receive syslog messages via upcoming syslog-transport-tls
IETF standard protocol.

%description openssl
The rsyslog-openssl package contains the rsyslog plugins that provide the
ability to send and receive syslog messages via TCP or RELP using TLS
encryption via OpenSSL library. For details refer to rsyslog doc on imtcp
and omfwd modules.

%description snmp
The rsyslog-snmp package contains the rsyslog plugin that provides the
ability to send syslog messages as SNMPv1 and SNMPv2c traps.

%description udpspoof
This module is similar to the regular UDP forwarder, but permits to
spoof the sender address. Also, it enables to circle through a number
of source ports.

%description omamqp1
The omamqp1 output module can be used to send log messages via an AMQP
1.0-compatible messaging bus.

%description kafka
The rsyslog-kafka package provides module for Apache Kafka output.

%description mmkubernetes
The rsyslog-mmkubernetes package provides module for adding kubernetes
container metadata.

%prep
# set up rsyslog-doc sources
%setup -q -a 1 -T -c

rm -r LICENSE README.md source build/objects.inv
mv build doc
# set up rsyslog sources
%setup -q -D
# Unpack qpid-proton for rhel
%setup -q -D -T -b 6

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

%build
# Add additional flags as per https://one.redhat.com/rhel-developer-guide/#_what_are_the_required_flags
%ifarch aarch64
export CFLAGS="$RPM_OPT_FLAGS -mbranch-protection=standard"
%else
export CFLAGS="$RPM_OPT_FLAGS -fcf-protection=full"
%endif

%ifarch sparc64
#sparc64 need big PIC
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpic"
%endif
# build the proton first
(
	cd %{_builddir}/qpid-proton-0.39.0
	mkdir bld
	cd bld

	# Need ENABLE_FUZZ_TESTING=NO to avoid a link failure
	# Find python include dir and python library from
	# https://stackoverflow.com/questions/24174394/cmake-is-not-able-to-find-python-libraries
	cmake .. \
		-DBUILD_BINDINGS="" \
		-DBUILD_STATIC_LIBS=YES \
		-DENABLE_FUZZ_TESTING=NO \
		-DPYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")  \
		-DPYTHON_LIBRARY=$(python3 -c "import distutils.sysconfig as sysconfig; print(sysconfig.get_config_var('LIBDIR'))") \
		-DCMAKE_AR="/usr/bin/gcc-ar" -DCMAKE_NM="/usr/bin/gcc-nm" -DCMAKE_RANLIB="/usr/bin/gcc-ranlib"
	make -j8
)

%ifarch sparc64
#sparc64 need big PIE
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
%else
export CFLAGS="$RPM_OPT_FLAGS -fpie"
%endif
export LDFLAGS="-pie -Wl,-z,relro -Wl,-z,now"

# the hiredis-devel package doesn't provide a pkg-config file
sed -i 's/%{version}/%{version}-%{release}/g' configure.ac
autoreconf -if
%configure \
	--prefix=/usr \
	--disable-static \
	--disable-testbench \
	--enable-omamqp1 PROTON_LIBS="%{_builddir}/qpid-proton-0.39.0/bld/c/libqpid-proton-core-static.a %{_builddir}/qpid-proton-0.39.0/bld/c/libqpid-proton-proactor-static.a %{_builddir}/qpid-proton-0.39.0/bld/c/libqpid-proton-static.a -lssl -lsasl2 -lcrypto" PROTON_CFLAGS="-I%{_builddir}/qpid-proton-0.39.0/bld/c/include" \
	--enable-elasticsearch \
	--enable-generate-man-pages \
	--enable-gnutls \
	--enable-openssl \
	--enable-gssapi-krb5 \
	--enable-imfile \
	--enable-imjournal \
	--enable-imkafka \
	--enable-impstats \
	--enable-imptcp \
	--enable-libcap-ng \
	--enable-mail \
	--enable-mmanon \
	--enable-mmaudit \
	--enable-mmcount \
	--enable-mmkubernetes \
	--enable-mmjsonparse \
	--enable-mmnormalize \
	--enable-mmfields \
	--enable-mmsnmptrapd \
	--enable-mmutf8fix \
	--enable-mysql \
	--enable-omhttp \
	--enable-omjournal \
	--enable-omprog \
	--enable-omstdout \
	--enable-omudpspoof \
	--enable-omuxsock \
	--enable-pgsql \
	--enable-pmaixforwardedfrom \
	--enable-pmcisconames \
	--enable-pmlastmsg \
	--enable-pmsnare \
	--enable-relp \
	--enable-snmp \
	--enable-unlimited-select \
	--enable-usertools \
	--enable-omkafka

make V=1

%check
make V=1 check

%install
make V=1 DESTDIR=%{buildroot} install

install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -d -m 700 %{buildroot}%{rsyslog_statedir}
install -d -m 700 %{buildroot}%{rsyslog_pkidir}
install -d -m 755 %{buildroot}%{rsyslog_docdir}/html
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}

install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/rsyslog.conf
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/rsyslog
install -p -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/rsyslog
install -p -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/rsyslog.service
install -p -m 644 plugins/ommysql/createDB.sql %{buildroot}%{rsyslog_docdir}/mysql-createDB.sql
install -p -m 644 plugins/ompgsql/createDB.sql %{buildroot}%{rsyslog_docdir}/pgsql-createDB.sql
dos2unix tools/recover_qi.pl
install -p -m 644 tools/recover_qi.pl %{buildroot}%{rsyslog_docdir}/recover_qi.pl
install -p -m 644 contrib/mmkubernetes/*.rulebase %{buildroot}%{rsyslog_docdir}
# extract documentation
cp -r doc/* %{buildroot}%{rsyslog_docdir}/html
# get rid of libtool libraries
rm -f %{buildroot}%{_libdir}/rsyslog/*.la
# imdiag and liboverride is only used for testing
rm -f %{buildroot}%{_libdir}/rsyslog/imdiag.so
rm -f %{buildroot}%{_libdir}/rsyslog/liboverride_gethostname.so

%post
for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	umask 066 && touch $n
done
%systemd_post rsyslog.service

%preun
%systemd_preun rsyslog.service

%postun
%systemd_postun_with_restart rsyslog.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING*
%doc AUTHORS ChangeLog README.md
%{rsyslog_docdir}
%exclude %{rsyslog_docdir}/html
%exclude %{rsyslog_docdir}/mysql-createDB.sql
%exclude %{rsyslog_docdir}/pgsql-createDB.sql
%dir %{_libdir}/rsyslog
%dir %{_sysconfdir}/rsyslog.d
%dir %{rsyslog_statedir}
%dir %{rsyslog_pkidir}
%dir %{_libexecdir}/%{name}
%{_sbindir}/rsyslogd
%{_mandir}/man5/rsyslog.conf.5.gz
%{_mandir}/man8/rsyslogd.8.gz
%{_unitdir}/rsyslog.service
%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/rsyslog
# plugins
%{_libdir}/rsyslog/fmhash.so
%{_libdir}/rsyslog/fmhttp.so
%{_libdir}/rsyslog/imfile.so
%{_libdir}/rsyslog/imjournal.so
%{_libdir}/rsyslog/imklog.so
%{_libdir}/rsyslog/immark.so
%{_libdir}/rsyslog/impstats.so
%{_libdir}/rsyslog/imptcp.so
%{_libdir}/rsyslog/imtcp.so
%{_libdir}/rsyslog/imudp.so
%{_libdir}/rsyslog/imuxsock.so
%{_libdir}/rsyslog/lmnet.so
%{_libdir}/rsyslog/lmnetstrms.so
%{_libdir}/rsyslog/lmnsd_ptcp.so
%{_libdir}/rsyslog/lmregexp.so
%{_libdir}/rsyslog/lmtcpclt.so
%{_libdir}/rsyslog/lmtcpsrv.so
%{_libdir}/rsyslog/lmzlibw.so
%{_libdir}/rsyslog/mmanon.so
%{_libdir}/rsyslog/mmcount.so
%{_libdir}/rsyslog/mmexternal.so
%{_libdir}/rsyslog/mmutf8fix.so
%{_libdir}/rsyslog/omhttp.so
%{_libdir}/rsyslog/omjournal.so
%{_libdir}/rsyslog/ommail.so
%{_libdir}/rsyslog/omprog.so
%{_libdir}/rsyslog/omstdout.so
%{_libdir}/rsyslog/omtesting.so
%{_libdir}/rsyslog/omuxsock.so
%{_libdir}/rsyslog/pmaixforwardedfrom.so
%{_libdir}/rsyslog/pmcisconames.so
%{_libdir}/rsyslog/pmlastmsg.so
%{_libdir}/rsyslog/pmsnare.so

%files logrotate
%config(noreplace) %{_sysconfdir}/logrotate.d/rsyslog

%files crypto
%{_bindir}/rscryutil
%{_mandir}/man1/rscryutil.1.gz
%{_libdir}/rsyslog/lmcry_gcry.so

%files doc
%doc %{rsyslog_docdir}/html

%files elasticsearch
%{_libdir}/rsyslog/omelasticsearch.so

%files mmaudit
%{_libdir}/rsyslog/mmaudit.so

%files mmjsonparse
%{_libdir}/rsyslog/mmjsonparse.so

%files mmnormalize
%{_libdir}/rsyslog/mmnormalize.so

%files mmfields
%{_libdir}/rsyslog/mmfields.so

%files mmsnmptrapd
%{_libdir}/rsyslog/mmsnmptrapd.so

%files mysql
%doc %{rsyslog_docdir}/mysql-createDB.sql
%{_libdir}/rsyslog/ommysql.so

%files pgsql
%doc %{rsyslog_docdir}/pgsql-createDB.sql
%{_libdir}/rsyslog/ompgsql.so

%files gssapi
%{_libdir}/rsyslog/lmgssutil.so
%{_libdir}/rsyslog/imgssapi.so
%{_libdir}/rsyslog/omgssapi.so

%files relp
%{_libdir}/rsyslog/imrelp.so
%{_libdir}/rsyslog/omrelp.so

%files gnutls
%{_libdir}/rsyslog/lmnsd_gtls.so

%files openssl
%{_libdir}/rsyslog/lmnsd_ossl.so

%files snmp
%{_libdir}/rsyslog/omsnmp.so

%files udpspoof
%{_libdir}/rsyslog/omudpspoof.so

%files omamqp1
%{_libdir}/rsyslog/omamqp1.so

%files kafka
%{_libdir}/rsyslog/imkafka.so
%{_libdir}/rsyslog/omkafka.so

%files mmkubernetes
%{_libdir}/rsyslog/mmkubernetes.so
%doc %{rsyslog_docdir}/k8s_filename.rulebase
%doc %{rsyslog_docdir}/k8s_container_name.rulebase


%changelog
* Tue Dec 12 2023 Attila Lakatos <alakatos@redhat.com> - 8.2310.0-4
- new directory for arbitrary external programs needed by omprog module
  Resolves: RHEL-8676

* Mon Nov 06 2023 Attila Lakatos <alakatos@redhat.com> - 8.2310.0-3
- Rebase to 8.2310.0
  Resolves: RHEL-5196
- Allow setting certificates for separate connections
  Resolves: RHEL-937
- Capability dropping feature can be turned off
  Resolves: RHEL-943
- imjournal: new module parameter filecreatemode
  Resolves: RHEL-949

* Wed Sep 06 2023 Patrik Koncity <pkoncity@redhat.com> - 8.2102.0-118
- Add rsyslog CI for new MR in c9s
  Resolves: RHEL-608

* Fri Jul 28 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-117
- Add back CAP_NET_RAW capability due to omudpspoof
  resolves: rhbz#2216919

* Tue Jun 27 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-116
- libcapng: do not try to drop capabilities that are not present
- add global libcapng.default to not abort when libcapng fails
  resolves: rhbz#2216919

* Mon May 22 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-115
- omelasticsearch: make compatible with elasticsearch>=8
- add new action specific parameter esversion.major
  resolves: rhbz#2209017

* Fri May 19 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-114
- Fix wrong type conversion in cstrLen()
  resolves: rhbz#2157805
- imjournal: by default retrieves _PID from journal as PID number
  resolves: rhbz#2176397
- Systemd service file hardening
  resolves: rhbz#2176403
- rsyslog.conf: load imuxsock and imjournal before loading rsyslog.d
  resolves: rhbz#2165899
- rsyslog is now started after the network service during boot
  resolves: rhbz#2074318
- imjournal: add second fallback to the message identifier
  resolves: rhbv#2129015

* Tue Mar 07 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-113
- Do not allow having selinux-policy < 38.1.3-1
  resolves: rhbz#2176386

* Mon Mar 06 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-112
- Add CAP_NET_RAW for initializing the libnet library for udpspoof
  resolves: rhbz#2176387

* Wed Feb 22 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-111
- Rebuild
  resolves: rhbz#2169748
  resolves: rhbz#2158659

* Fri Feb 17 2023 Attila Lakatos <alakatos@redhat.com> -8.2102.0-110
- Do not preserve capabilities when changing credentials
  resolves: rhbz#2169748
- Remove unnecessary capability CAP_PERFMON
- Add CAP_DAC_OVERRIDE to bypass file read and write permission checks
  resolves: rhbz#2158659

* Mon Jan 09 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-109
- Make rsyslog-relp require librelp>= 1.9.0
  resolves: rhbz#2124440
- Reorder logrotate parameters to work with POSIXLY_CORRECT env var
  resolves: rhbz#2124488

* Fri Jan 06 2023 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-108
- Fix invalid memory adressing in imklog that could case abort
  resolves: rhbz#2157659

* Mon Nov 21 2022 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-107
- Drop capabilities to only the neccessary set with libcap-ng
  resolves: rhbz#2127404

* Tue Sep 06 2022 Sergio Arroutbi <sarroutb@redhat.com> - 8.2102.0-106
- Enable multiple SSL CA files
  resolves: rhbz#2124849

* Mon May 09 2022 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-105
- Address CVE-2022-24903, Heap-based overflow in TCP syslog server
  resolves: rhbz#2081403

* Tue Apr 19 2022 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-104
- Do not save patched doc files
  resolves: rhbz#2069664

* Tue Apr 05 2022 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-103
- Add deleteStateOnFileMove imfile module option
  resolves: rhbz#2069664
- Add inotify_rm_watch() inotify API call when object needs to be destroyed
  resolves: rhbz#2070528
- Fix error handling in gtlsRecordRecv, which can cause full CPU usage

* Fri Mar 11 2022 Sergio Arroutbi <sarroutb@redhat.com> - 8.2102.0-102
- Add action.errorfile.maxsize parameter
  resolves: rhbz#2064318

* Wed Jan 19 2022 Sergio Arroutbi <sarroutb@redhat.com> - 8.2102.0-101
- Prioritize SAN
  resolves: rhbz#2021076

* Mon Jan 17 2022 Sergio Arroutbi <sarroutb@redhat.com> - 8.2102.0-100
- Enable mmfields module
  resolves: rhbz#2027971

* Tue Oct 26 2021 Davide Cavalca <dcavalca@centosproject.org> - 8.2102.0-10
- Split out logrotate config and dependency into a subpackage
  resolves: rhbz#1992155

* Fri Aug 27 2021 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-9
- Add required flags for branch protection
- Add missing tests folder
- Resolve issues detected by covscan
  resolves: rhbz#1938863

* Mon Aug 23 2021 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-8
- Resolve issues detected by covscan
  resolves: rhbz#1938863

* Wed Aug 18 2021 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-7
- Enable openssl
  resolves: rhbz#1972058
- Close dir when fsync=on
  resolves: rhbz#1972069
- Do not exit when user/group can not be found
  resolves: rhbz#1990868
- Remove abortOnIDResolution fail
- Always use message severity when comparing with ratelimit severity
  resolves: rhbz#1990869

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 8.2102.0-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 8.2102.0-5
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Mon May 31 2021 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-4
- Spec file clean up
- Port to OpenSSL 3.0
  resolves: rhbz#1964823

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 8.2102.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Mar 17 2021 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-2
- Remove rsyslog-recover-qi.pl from bindir, so it does not add dep on /usr/bin/perl
  resolves: rhbz#1939556

* Wed Mar 03 2021 Attila Lakatos <alakatos@redhat.com> - 8.2102.0-1
- rebase to upstream version 8.2102.0
  resolves: rhbz#1905363
- enable additional plugins: imkafka, mmutf8fix

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 8.2010.0-3
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.2010.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Attila Lakatos <alakatos@redhat.com> - 8.2010.0-1
- rebase to upstream version 8.2010.0
  resolves: rhbz#1890330

* Fri Sep 18 2020 Attila Lakatos <alakatos@redhat.com> - 8.2008.0-2
- rebuild package

* Thu Sep 17 2020 Attila Lakatos <alakatos@redhat.com> - 8.2008.0-1
- rebase to upstream version 8.2008.0
  resolves: rhbz#1829092
  resolves: rhbz#1823862
  resolves: rhbz#1876773
- add service file back(upstream does not ship it anymore)

* Thu Aug 27 2020 Josef Řídký <jridky@redhat.com> - 8.2002.0-5
- Rebuilt for new net-snmp release

* Thu Aug 20 2020 Attila Lakatos <alakatos@redhat.com> - 8.2002.0-4
- enable configuration reload in the service
  resolves: rhbz#1868636

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2002.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.2002.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Jiri Vymazal <jvymazal@redhat.com> - 8.2002.0-1
- rebase to upstream version 8.2002.0
  resolves: rhbz#1807097

* Mon Feb 03 2020 Jiri Vymazal <jvymazal@redhat.com> - 8.2001.0-1
- rebase to upstream version 8.2001.0
  resolves: rhbz#1790731

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1911.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1911.0-1
- rebase to upstream version 8.1911.0
  resolves: rhbz#1771468

* Thu Oct 17 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1910.0-1
- rebase to upstream version 8.1910.0
  resolves: rhbz#1743537

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1907.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1907.0-1
- rebase to upstream version 8.1905.0
  resolves: rhbz#1716391

* Mon May 13 2019 Jiri Vymazal <jvymazal@redhat.com> - 8.1904.0-1
- rebase to upstream version 8.1904.0
  resolves: rhbz#1668473

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Bogdan Dobrelya <bdobreli@redhat.com> - 8.39.0-2
- Use systemd_ordering macro

* Wed Dec 05 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.39.0-1
- rebase to upstream version 8.39.0
  resolves: rhbz#1649081
  resolves: rhbz#1615014

* Wed Oct 10 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.38.0-1
- rebase to upstream version 8.38.0
  resolves: rhbz#1632432
  resolves: rhbz#1627944

* Fri Aug 10 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.37.0-1
- added mmkubernetes rulebases as doc files
  resolves: rhbz#1614440

* Wed Aug 08 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.37.0-1
- rebase to upstream version 8.37.0
  resolves: rhbz#1612079
  resolves: rhbz#1598217
  resolves: rhbz#1544139
- dropped needless libee dependency
- bumped librelp dependency to actually needed version

* Wed Jul 25 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.36.0-3
- fixed a typo in commented-out part of default conf + reordered it
  resolves: rhbz#1579592

* Tue Jul 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 8.36.0-3
- Rebuild for unannounced net-snmp soversion bump.
- Use python3-docutils because rst2man has moved there.

* Mon Jul 23 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.36.0-2
- added gcc to buildrequires following f29 system-wide change

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.36.0-1
- rebase to 8.36.0
  - removed stdlog dependency as upstream is going to drop it
- following upstream naming of pidfile
- removed needless conditionals

* Fri Jun  8 2018 Remi Collet <remi@remirepo.net> - 8.35.0-4
- rebuild with libbson and libmongc 1.10.2 (soname back to 0)

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 8.35.0-3
- rebuild with libbson and libmongc 1.10.0

* Thu May 17 2018 Radovan Sroka <rsroka@redhat.com> - 8.35.0-2
- rebase to 8.35.0

* Thu Apr 05 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.34.0-1
- rebase to 8.34.0
- added mmkubernetes module
- added fmhttp module
- finished converting rsyslog config to new syntax
- dropped obsolete defattr statements from spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Jiri Vymazal <jvymazal@redhat.com> - 8.32.0-1
- rebase to 8.32.0
- now requires higher version of libfastjson

* Thu Dec 14 2017 Radovan Sroka <rsroka@redhat.com> - 8.31.0-2
- added also cyrus-sasl-devel dependency

* Thu Dec 14 2017 Radovan Sroka <rsroka@redhat.com> - 8.31.0-1
- update to 8.31.0
- removed upstreamed patches
- added dependecies mongo-c-driver-devel snappy-devel
- removed depricated dependecies libmongo-client
- mongodb plugin now uses new driver with TLS,...

* Tue Nov 28 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.30.0-4
- changed rsyslog-doc to noarch

* Mon Nov 20 2017 Radovan Sroka <rsoka@redhat.com> - 8.30.0-4
- rebuild due to libqpid-proton.so

* Wed Oct 25 2017 Radovan Sroka <rsroka@redhat.com> - 8.30.0-3
- rebuild

* Wed Oct 25 2017 Radovan Sroka <rsroka@redhat.com> - 8.30.0-2
- imjournal didn't work at all
- added imjournal patch for rhbz#1505853

* Mon Oct 23 2017 Radovan Sroka <rsroka@redhat.com> - 8.30.0-1
- rebase to 8.30.0
- added patch that resolves imgssapi compilation errors

* Mon Oct 9 2017 Marek Tamaskovic <mtamasko@redhat.com> - 8.29.0-4
- mysql-devel changed for mariadb-connector-c-devel
  resolves: rhbz#1493695
- repaired changelog

* Tue Aug 15 2017 Radovan Sroka <rsroka@redhat.com> - 8.29.0-2
- rebuild, bumped release number

* Tue Aug 15 2017 Marek Tamaskovic <mtamasko@redhat.com> - 8.29.0-1
- rebase to 8.29.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Radovan Sroka <rsroka@redhat.com> - 8.27.0-1
- dropped patch2 (upstreamed)
- rebase to 8.27.0

* Tue Apr 18 2017 Radovan Sroka <rsroka@redhat.com> - 8.26.0-1
- rebase to 8.26.0
- added doc patch rhbz#1436113
- dropped chdir patch, https://github.com/rsyslog/rsyslog/pull/1420
- moved dependency libgcrypt to rsyslog core

* Wed Mar 01 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.25.0-2
- rebased doc subpackage to 8.25.0 as well
- dropped upstreamed doc patch

* Tue Feb 28 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.25.0-1
- rebase to 8.25.0 upstream source version

* Mon Feb 27 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-7
- forced rebuild because of libqpid-proton rebase

* Mon Feb 20 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-6
- fixed typo in chdir location
  resolves: rhbz#1422542
- updated one more directive in default config
  resolves: rhbz#1419625

* Fri Feb 17 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-5
- new default config, using RainerScript wherever possible
  resolves: rhbz#1419625
- updated testbench guard as testbench now needs explicit configuration
  see: rhbz#1211194
- added patch to make chdir call after chroot
  resolves: rhbz#1422542

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-3
- new kafka sub-package, adding omkafka module
  see: rhbz#1418720

* Mon Jan 16 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-2
- reverted symlink to syslog.service - not needed
  see: rhbz#1343132

* Fri Jan 13 2017 Jiri Vymazal <jvymazal@redhat.com> - 8.24.0-1
- rsyslog rebase to 8.24
- changed name of created file in logrotate.d to non-generic one
  resolves: rhbz1269244
- added symlink to syslog.service
  resolves: rhbz1343132
- added documentation for recover_qi
  resolves: rhbz1286707
- changed default .conf added imuxsock, seqfault is not present anymore
  https://github.com/rsyslog/rsyslog/pull/1289

* Tue Dec 20 2016 Radovan Sroka <rsroka@redhat.com> - 8.23.0-2
- added forgoten patch rsyslog-8.23.0-msg_c_nonoverwrite_merge.patch

* Tue Dec 20 2016 Radovan Sroka <rsroka@redhat.com> - 8.23.0-1
- rebase to 8.23.0
- change build requires from libfastjson to libfastjson-devel

* Thu Nov 10 2016 Tomas Sykora <tosykora@redhat.com> 8.22.0-1
- rebase to 8.22.0
  - added omamqp1 subpackage
  - changed BuildRequires from json-c to libfastjson

* Wed Oct 05 2016 Radovan Sroka <rsroka@redhat.com> 8.21.0-1
- rebase to 8.21.0
- dropped rsyslog-8.12.0-gnutls-detection.patch
- dropped rsyslog-8.8.0-immutable-json-props.patch
  - remove from specs but nor from git
  - could be useful in future

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Tomas Heinrich <theinric@redhat.com> 8.12.0-2
- rebuild for soname bump in hiredis-0.13.2

* Tue Sep 1 2015 Radovan Sroka <rsroka@redhat.com> 8.12.0-1
- rebase to 8.12.0
  - drop patches merged upstream
- resolve detection of the new GnuTLS package
  - add autoconf to BuildRequires
- add --enable-generate-man-pages to configure parameters;
  the rscryutil man page isn't generated without it
  https://github.com/rsyslog/rsyslog/pull/469

* Wed Jun 24 2015 Tomas Heinrich <theinric@redhat.com> 8.10.0-1
- rebase to 8.10.0
- drop patches merged upstream
- use the right macro to specify the default pidfile
  resolves: rhbz#1224972
- make logrotate tolerate missing log files
  resolves: rhbz#1205889
- set the default service umask to 0066
  resolves: rhbz#1228192
- use systemctl for sending SIGHUP to the service
  related: rhbz#1224972
- add a patch to prevent a crash on empty messages
  resolves: rhbz#1224538
- add a patch to fix several default parameters for message queues
  resolves: rhbz#1205696
- add a patch to fix the storage size for a configuration option

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Remi Collet <remi@fedoraproject.org> 8.8.0-3
- rebuild for new librabbitmq

* Fri Mar 20 2015 Tomas Heinrich <theinric@redhat.com> 8.8.0-2
- add a patch to fix default syslog priority assigned to journal
  messages which have none

* Thu Mar 19 2015 Tomas Heinrich <theinric@redhat.com> 8.8.0-1
- rebase to 8.8.0
  resolves: rhbz#1069690
  - drop patches merged upstream
  - version the dependency on liblognorm-devel
  - enable mmcount, mmexternal modules,
    remove imdiag, omruleset and pmrfc3164sd modules
    resolves: rhbz#1156359
- add dos2unix to build requirements
- make the build process more verbose
- in accordance with an upstream change, the rsyslog service is now
  restarted automatically upon failure
- adjust the default configuration file for the removal of
  /etc/rsyslog.d/listen.conf by the systemd package
  resolves: rhbz#1116864
- disable the imklog module by default; kernel messages are read from journald
  resolves: rhbz#1083564
- if there is no saved position in the journal, log only messages that are
  received after rsyslog is started; this is a safety measure to prevent
  excessive resource utilization
- use documentation from the standalone rsyslog-docs project
- move documentation from all subpackages into a single directory
- mark the recover_qi.pl script as documentation

* Tue Oct 07 2014 Tomas Heinrich <theinric@redhat.com> 7.4.10-5
- fix CVE-2014-3634

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Tom Callaway <spot@fedoraproject.org> - 7.4.10-3
- fix license handling
- fix build against latest json-c

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Tomas Heinrich <theinric@redhat.com> 7.4.10-1
- rebase to 7.4.10
  - drop patches merged upstream
  - add a build dependency on liblogging-stdlog

* Thu Apr 24 2014 Tomas Mraz <tmraz@redhat.com> - 7.4.8-2
- Rebuild for new libgcrypt

* Mon Feb 10 2014 Tomas Heinrich <theinric@redhat.com> 7.4.8-1
- rebase to 7.4.8
- drop patch4, merged upstream
  rsyslog-7.4.7-bz1030044-remove-ads.patch
- add an explicit requirement on the version of libestr
- drop the "v5" string from the conf file as it's misleading
- add rsyslog-7.4.8-omjournal-warning.patch to fix
  a condition for issuing a warning in omjournal
- add rsyslog-7.4.8-dont-link-libee.patch to prevent
  linking the main binary with libee
- replace rsyslog-7.3.15-imuxsock-warning.patch
  with rsyslog-7.4.8-imuxsock-wrn.patch
- link to libhiredis explicitly
- add a patch to prevent message loss in imjournal
  rsyslog-7.4.8-bz1026804-imjournal-message-loss.patch
- move the rscryutil man page to the crypto subpackage

* Sun Feb 09 2014 Lubomir Rintel <lkundrak@v3.sk> 7.4.7-3
- Fixed 32-bit PowerPC build

* Mon Jan 27 2014 Tomas Heinrich <theinric@redhat.com> 7.4.7-2
- rebuild for libdbi-0.9.0-1

* Mon Jan 06 2014 Tomas Heinrich <theinric@redhat.com> 7.4.7-1
- rebase to 7.4.7
- install the rsyslog-recover-qi.pl tool
- fix a typo in a package description
- add missing defattr directives
- add a patch to remove references to Google ads in the html docs
  rsyslog-7.4.7-bz1030044-remove-ads.patch
  Resolves: #1030044
- add a patch to allow numeric specification of UIDs/GUIDs
  rsyslog-7.4.7-numeric-uid.patch
- change the installation prefix to "/usr"
  Resolves: #1032577

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Tomas Heinrich <theinric@redhat.com> 7.4.2-1
- rebase to 7.4.2
  most importantly, this release fixes a potential vulnerability,
  see http://www.lsexperts.de/advisories/lse-2013-07-03.txt
  the impact should be low as only those using the omelasticsearch
  plugin with a specific configuration are exposed

* Mon Jun 17 2013 Tomas Heinrich <theinric@redhat.com> 7.4.1-1
- rebase to 7.4.1
  this release adds code that somewhat mitigates damage in cases
  where large amounts of messages are received from systemd
  journal (see rhbz#974132)
- regenerate patch 0
- drop patches merged upstream: 4..8
- add a dependency on the version of systemd which resolves the bug
  mentioned above
- update option name in rsyslog.conf

* Wed Jun 12 2013 Tomas Heinrich <theinric@redhat.com> 7.4.0-1
- rebase to 7.4.0
- drop autoconf automake libtool from BuildRequires
- depends on systemd >= 201 because of the sd_journal_get_events() api
- add a patch to prevent a segfault in imjournal caused by a bug in
  systemd journal
- add a patch to prevent an endless loop in the ratelimiter
- add a patch to prevent another endless loop in the ratelimiter
- add a patch to prevent a segfault in imjournal for undefined state file
- add a patch to correctly reset state in the ratelimiter

* Tue Jun 04 2013 Tomas Heinrich <theinric@redhat.com> 7.3.15-1.20130604git6e72fa6
- rebase to an upstream snapshot, effectively version 7.3.15
  plus several more changes
- drop patches 3, 4 - merged upstream
- add a patch to silence warnings emitted by the imuxsock module
- drop the imkmsg plugin
- enable compilation of additional modules
  imjournal, mmanon, omjournal, omrabbitmq
- new subpackages: crypto, rabbitmq
- add python-docutils and autoconf to global BuildRequires
- drop the option for backwards compatibility from the
  sysconfig file - it is no longer supported
- call autoreconf to prepare the snapshot for building
- switch the local message source from imuxsock to imjournal
  the imuxsock module is left enabled so it is easy to swich back to
  it and because systemd drops a file into /etc/rsyslog.d which only
  imuxsock can parse

* Wed Apr 10 2013 Tomas Heinrich <theinric@redhat.com> 7.3.10-1
- rebase to 7.3.10
- add a patch to resolve #950088 - ratelimiter segfault, merged upstream
  rsyslog-7.3.10-ratelimit-segv.patch
- add a patch to correct a default value, merged upstream
  rsyslog-7.3.10-correct-def-val.patch
- drop patch 5 - fixed upstream

* Thu Apr 04 2013 Tomas Heinrich <theinric@redhat.com> 7.3.9-1
- rebase to 7.3.9

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Tomas Heinrich <theinric@redhat.com> 7.2.5-2
- update a line in rsyslog.conf for the new syntax

* Sun Jan 13 2013 Tomas Heinrich <theinric@redhat.com> 7.2.5-1
- upgrade to upstream version 7.2.5
- update the compatibility mode in sysconfig file

* Mon Dec 17 2012 Tomas Heinrich <theinric@redhat.com> 7.2.4-2
- add a condition to disable several subpackages

* Mon Dec 10 2012 Tomas Heinrich <theinric@redhat.com> 7.2.4-1
- upgrade to upstream version 7.2.4
- remove trailing whitespace

* Tue Nov 20 2012 Tomas Heinrich <theinric@redhat.com> 7.2.2-1
- upgrade to upstream version 7.2.2
  update BuildRequires
- remove patches merged upstream
  rsyslog-5.8.7-sysklogd-compat-1-template.patch
  rsyslog-5.8.7-sysklogd-compat-2-option.patch
  rsyslog-5.8.11-close-fd1-when-forking.patch
- add patch from Milan Bartos <mbartos@redhat.com>
  rsyslog-7.2.1-msg_c_nonoverwrite_merge.patch
- remove the rsyslog-sysvinit package
- clean up BuildRequires, Requires
- remove the 'BuildRoot' tag
- split off a doc package
- compile additional modules (some of them in separate packages):
  elasticsearch
  hiredis
  mmjsonparse
  mmnormalize
  mmaudit
  mmsnmptrapd
  mongodb
- correct impossible timestamps in older changelog entries
- correct typos, trailing spaces, etc
- s/RPM_BUILD_ROOT/{buildroot}/
- remove the 'clean' section
- replace post* scriptlets with systemd macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Tomas Heinrich <theinric@redhat.com> 5.8.11-2
- update systemd patch: remove the 'ExecStartPre' option

* Wed May 23 2012 Tomas Heinrich <theinric@redhat.com> 5.8.11-1
- upgrade to new upstream stable version 5.8.11
- add impstats and imptcp modules
- include new license text files
- consider lock file in 'status' action
- add patch to update information on debugging in the man page
- add patch to prevent debug output to stdout after forking
- add patch to support ssl certificates with domain names longer than 128 chars

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> 5.8.7-2
- libnet rebuild.

* Mon Jan 23 2012 Tomas Heinrich <theinric@redhat.com> 5.8.7-1
- upgrade to new upstream version 5.8.7
- change license from 'GPLv3+' to '(GPLv3+ and ASL 2.0)'
  http://blog.gerhards.net/2012/01/rsyslog-licensing-update.html
- use a specific version for obsoleting sysklogd
- add patches for better sysklogd compatibility (taken from upstream)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Tomas Heinrich <theinric@redhat.com> 5.8.6-1
- upgrade to new upstream version 5.8.6
- obsolete sysklogd
  Resolves: #748495

* Tue Oct 11 2011 Tomas Heinrich <theinric@redhat.com> 5.8.5-3
- modify logrotate configuration to omit boot.log
  Resolves: #745093

* Tue Sep 06 2011 Tomas Heinrich <theinric@redhat.com> 5.8.5-2
- add systemd-units to BuildRequires for the _unitdir macro definition

* Mon Sep 05 2011 Tomas Heinrich <theinric@redhat.com> 5.8.5-1
- upgrade to new upstream version (CVE-2011-3200)

* Fri Jul 22 2011 Tomas Heinrich <theinric@redhat.com> 5.8.2-3
- move the SysV init script into a subpackage
- Resolves: 697533

* Mon Jul 11 2011 Tomas Heinrich <theinric@redhat.com> 5.8.2-2
- rebuild for net-snmp-5.7 (soname bump in libnetsnmp)

* Mon Jun 27 2011 Tomas Heinrich <theinric@redhat.com> 5.8.2-1
- upgrade to new upstream version 5.8.2

* Mon Jun 13 2011 Tomas Heinrich <theinric@redhat.com> 5.8.1-2
- scriptlet correction
- use macro in unit file's path

* Fri May 20 2011 Tomas Heinrich <theinric@redhat.com> 5.8.1-1
- upgrade to new upstream version
- correct systemd scriptlets (#705829)

* Mon May 16 2011 Bill Nottingham <notting@redhat.com> - 5.7.9-3
- combine triggers (as rpm will only execute one) - fixes upgrades (#699198)

* Tue Apr 05 2011 Tomas Heinrich <theinric@redhat.com> 5.7.10-1
- upgrade to new upstream version 5.7.10

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 5.7.9-2
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Fri Mar 18 2011 Tomas Heinrich <theinric@redhat.com> 5.7.9-1
- upgrade to new upstream version 5.7.9
- enable compilation of several new modules,
  create new subpackages for some of them
- integrate changes from Lennart Poettering
  to add support for systemd
  - add rsyslog-5.7.9-systemd.patch to tweak the upstream
    service file to honour configuration from /etc/sysconfig/rsyslog

* Fri Mar 18 2011 Dennis Gilmore <dennis@ausil.us> - 5.6.2-3
- sparc64 needs big PIE

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Tomas Heinrich <theinric@redhat.com> 5.6.2-1
- upgrade to new upstream stable version 5.6.2
- drop rsyslog-5.5.7-remove_include.patch; applied upstream
- provide omsnmp module
- use correct name for lock file (#659398)
- enable specification of the pid file (#579411)
- init script adjustments

* Wed Oct 06 2010 Tomas Heinrich <theinric@redhat.com> 5.5.7-1
- upgrade to upstream version 5.5.7
- update configuration and init files for the new major version
- add several directories for storing auxiliary data
- add ChangeLog to documentation
- drop unlimited-select.patch; integrated upstream
- add rsyslog-5.5.7-remove_include.patch to fix compilation

* Tue Sep 07 2010 Tomas Heinrich <theinric@redhat.com> 4.6.3-2
- build rsyslog with PIE and RELRO

* Thu Jul 15 2010 Tomas Heinrich <theinric@redhat.com> 4.6.3-1
- upgrade to new upstream stable version 4.6.3

* Wed Apr 07 2010 Tomas Heinrich <theinric@redhat.com> 4.6.2-1
- upgrade to new upstream stable version 4.6.2
- correct the default value of the OMFileFlushOnTXEnd directive

* Thu Feb 11 2010 Tomas Heinrich <theinric@redhat.com> 4.4.2-6
- modify rsyslog-4.4.2-unlimited-select.patch so that
  running autoreconf is not needed
- remove autoconf, automake, libtool from BuildRequires
- change exec-prefix to nil

* Wed Feb 10 2010 Tomas Heinrich <theinric@redhat.com> 4.4.2-5
- remove '_smp_mflags' make argument as it seems to be
  producing corrupted builds

* Mon Feb 08 2010 Tomas Heinrich <theinric@redhat.com> 4.4.2-4
- redefine _libdir as it doesn't use _exec_prefix

* Thu Dec 17 2009 Tomas Heinrich <theinric@redhat.com> 4.4.2-3
- change exec-prefix to /

* Wed Dec 09 2009 Robert Scheck <robert@fedoraproject.org> 4.4.2-2
- run libtoolize to avoid errors due mismatching libtool version

* Thu Dec 03 2009 Tomas Heinrich <theinric@redhat.com> 4.4.2-1
- upgrade to new upstream stable version 4.4.2
- add support for arbitrary number of open file descriptors

* Mon Sep 14 2009 Tomas Heinrich <theinric@redhat.com> 4.4.1-2
- adjust init script according to guidelines (#522071)

* Thu Sep 03 2009 Tomas Heinrich <theinric@redhat.com> 4.4.1-1
- upgrade to new upstream stable version

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.2.0-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Tomas Heinrich <theinric@redhat.com> 4.2.0-1
- upgrade

* Mon Apr 13 2009 Tomas Heinrich <theinric@redhat.com> 3.21.11-1
- upgrade

* Tue Mar 31 2009 Lubomir Rintel <lkundrak@v3.sk> 3.21.10-4
- Backport HUPisRestart option

* Wed Mar 18 2009 Tomas Heinrich <theinric@redhat.com> 3.21.10-3
- fix variables' type conversion in expression-based filters (#485937)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Tomas Heinrich <theinric@redhat.com> 3.21.10-1
- upgrade

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> 3.21.9-3
- rebuild for dependencies

* Wed Jan 07 2009 Tomas Heinrich <theinric@redhat.com> 3.21.9-2
- fix several legacy options handling
- fix internal message output (#478612)

* Mon Dec 15 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.9-1
- update is fixing $AllowedSender security issue

* Mon Sep 15 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.3-4
- use RPM_OPT_FLAGS
- use same pid file and logrotate file as syslog-ng (#441664)
- mark config files as noreplace (#428155)

* Mon Sep 01 2008 Tomas Heinrich <theinric@redhat.com> 3.21.3-3
- fix a wrong module name in the rsyslog.conf manual page (#455086)
- expand the rsyslog.conf manual page (#456030)

* Thu Aug 28 2008 Tomas Heinrich <theinric@redhat.com> 3.21.3-2
- fix clock rollback issue (#460230)

* Wed Aug 20 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.3-1
- upgrade to bugfix release

* Wed Jul 23 2008 Peter Vrabec <pvrabec@redhat.com> 3.21.0-1
- upgrade

* Mon Jul 14 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.9-2
- adjust default config file

* Fri Jul 11 2008 Lubomir Rintel <lkundrak@v3.sk> 3.19.9-1
- upgrade

* Wed Jun 25 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.7-3
- rebuild because of new gnutls

* Fri Jun 13 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.7-2
- do not translate Oopses (#450329)

* Fri Jun 13 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.7-1
- upgrade

* Wed May 28 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.4-1
- upgrade

* Mon May 26 2008 Peter Vrabec <pvrabec@redhat.com> 3.19.3-1
- upgrade to new upstream release

* Wed May 14 2008 Tomas Heinrich <theinric@redhat.com> 3.16.1-1
- upgrade

* Tue Apr 08 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-5
- prevent undesired error description in legacy
  warning messages

* Tue Apr 08 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-4
- adjust symbol lookup method to 2.6 kernel

* Tue Apr 08 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-3
- fix segfault of expression based filters

* Mon Apr 07 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-2
- init script fixes (#441170,#440968)

* Fri Apr 04 2008 Peter Vrabec <pvrabec@redhat.com> 3.14.1-1
- upgrade

* Tue Mar 25 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.4-1
- upgrade

* Wed Mar 19 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.3-1
- upgrade
- fix some significant memory leaks

* Tue Mar 11 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.1-2
- init script fixes (#436854)
- fix config file parsing (#436722)

* Thu Mar 06 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.1-1
- upgrade

* Wed Mar 05 2008 Peter Vrabec <pvrabec@redhat.com> 3.12.0-1
- upgrade

* Mon Feb 25 2008 Peter Vrabec <pvrabec@redhat.com> 3.11.5-1
- upgrade

* Fri Feb 01 2008 Peter Vrabec <pvrabec@redhat.com> 3.11.0-1
- upgrade to the latests development release
- provide PostgresSQL support
- provide GSSAPI support

* Mon Jan 21 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-7
- change from requires sysklogd to conflicts sysklogd

* Fri Jan 18 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-6
- change logrotate file
- use rsyslog own pid file

* Thu Jan 17 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-5
- fixing bad descriptor (#428775)

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-4
- rename logrotate file

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-3
- fix post script and init file

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-2
- change pid filename and use logrotata script from sysklogd

* Tue Jan 15 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-1
- upgrade to stable release
- spec file clean up

* Wed Jan 02 2008 Peter Vrabec <pvrabec@redhat.com> 1.21.2-1
- new upstream release

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.19.11-2
- Rebuild for deps

* Thu Nov 29 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.11-1
- new upstream release
- add conflicts (#400671)

* Mon Nov 19 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.10-1
- new upstream release

* Wed Oct 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.6-3
- remove NUL character from recieved messages

* Tue Sep 25 2007 Tomas Heinrich <theinric@redhat.com> 1.19.6-2
- fix message suppression (303341)

* Tue Sep 25 2007 Tomas Heinrich <theinric@redhat.com> 1.19.6-1
- upstream bugfix release

* Tue Aug 28 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.2-1
- upstream bugfix release
- support for negative app selector, patch from
  theinric@redhat.com

* Fri Aug 17 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.0-1
- new upstream release with MySQL support(as plugin)

* Wed Aug 08 2007 Peter Vrabec <pvrabec@redhat.com> 1.18.1-1
- upstream bugfix release

* Mon Aug 06 2007 Peter Vrabec <pvrabec@redhat.com> 1.18.0-1
- new upstream release

* Thu Aug 02 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.6-1
- upstream bugfix release

* Mon Jul 30 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.5-1
- upstream bugfix release
- fix typo in provides

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 1.17.2-4
- rebuild for toolchain bug

* Tue Jul 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-3
- take care of sysklogd configuration files in %%post

* Tue Jul 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-2
- use EVR in provides/obsoletes sysklogd

* Mon Jul 23 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-1
- upstream bug fix release

* Fri Jul 20 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.1-1
- upstream bug fix release
- include html docs (#248712)
- make "-r" option compatible with sysklogd config (248982)

* Tue Jul 17 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.0-1
- feature rich upstream release

* Thu Jul 12 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.1-2
- use obsoletes and hadle old config files

* Wed Jul 11 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.1-1
- new upstream bugfix release

* Tue Jul 10 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.0-1
- new upstream release introduce capability to generate output
  file names based on templates

* Tue Jul 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.14.2-1
- new upstream bugfix release

* Mon Jul 02 2007 Peter Vrabec <pvrabec@redhat.com> 1.14.1-1
- new upstream release with IPv6 support

* Tue Jun 26 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-3
- add BuildRequires for zlib compression feature

* Mon Jun 25 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-2
- some spec file adjustments.
- fix syslog init script error codes (#245330)

* Fri Jun 22 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-1
- new upstream release

* Fri Jun 22 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.4-2
- some spec file adjustments.

* Mon Jun 18 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.4-1
- upgrade to new upstream release

* Wed Jun 13 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.2-2
- DB support off

* Tue Jun 12 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.2-1
- new upstream release based on redhat patch

* Fri Jun 08 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.1-2
- rsyslog package provides its own kernel log. daemon (rklogd)

* Mon Jun 04 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.1-1
- Initial rpm build
