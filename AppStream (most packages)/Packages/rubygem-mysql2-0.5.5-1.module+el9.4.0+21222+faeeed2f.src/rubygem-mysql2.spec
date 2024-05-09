# build with tests?
%bcond_without tests

# Generated from mysql2-0.3.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mysql2

Name: rubygem-%{gem_name}
Version: 0.5.5
Release: 1%{?dist}
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
License: MIT
URL: https://github.com/brianmario/mysql2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/brianmario/mysql2.git
# cd mysql2 && git archive -v -o mysql2-0.5.5-tests.txz 0.5.5 spec/
Source1: %{gem_name}-%{version}-tests.txz
# Use the SSL pem files in the upstream repositry for the SSL tests.
# https://github.com/brianmario/mysql2/pull/1293
Patch0: rubygem-mysql2-0.5.4-use-ssl-pem-files-in-repo.patch

# Required in lib/mysql2.rb
Requires: rubygem(bigdecimal)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: gcc
BuildRequires: mariadb-connector-c-devel
%if %{with tests}
BuildRequires: mariadb-server
BuildRequires: rubygem(rspec)
# Used in mysql_install_db
BuildRequires: %{_bindir}/hostname
BuildRequires: rubygem(bigdecimal)
# Used in spec/em/em_spec.rb
# Comment out to prevent a build error by unsatisfiable dependencies.
# No matching package to install: 'rubygem(eventmachine)'
#BuildRequires: rubygem(eventmachine)
# Used in spec/ssl/gen_certs.sh
BuildRequires: %{_bindir}/openssl
%endif

%description
The Mysql2 gem is meant to serve the extremely common use-case of
connecting, querying and iterating on results. Some database libraries
out there serve as direct 1:1 mappings of the already complex C API\'s
available. This one is not.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}/spec
%patch -P 0 -p2
popd

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo.
rm -rf %{buildroot}%{gem_instdir}/ext


%if %{with tests}
%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/spec spec

TOP_DIR=$(pwd)

# Regenerate the SSL certification files from the localhost, as we cannot set
# the host mysql2gem.example.com required for the SSL tests.
# https://github.com/brianmario/mysql2/pull/1296
sed -i '/host/ s/mysql2gem\.example\.com/localhost/' spec/mysql2/client_spec.rb
sed -i '/commonName_default/ s/mysql2gem\.example\.com/localhost/' spec/ssl/gen_certs.sh
pushd spec/ssl
bash gen_certs.sh
popd

# See https://github.com/brianmario/mysql2/blob/master/ci/ssl.sh
echo "
[mysqld]
ssl-ca=${TOP_DIR}/spec/ssl/ca-cert.pem
ssl-cert=${TOP_DIR}/spec/ssl/server-cert.pem
ssl-key=${TOP_DIR}/spec/ssl/server-key.pem
" > ~/.my.cnf

# Use testing port because the standard mysqld port 3306 is occupied.
# Assign a random port to consider a case of multi builds in parallel in a host.
# https://src.fedoraproject.org/rpms/rubygem-pg/pull-request/3
MYSQL_TEST_PORT="$((13306 + ${RANDOM} % 1000))"
MYSQL_TEST_USER=$(id -un)
MYSQL_TEST_DATA_DIR="${TOP_DIR}/data"
MYSQL_TEST_SOCKET="${TOP_DIR}/mysql.sock"
MYSQL_TEST_LOG="${TOP_DIR}/mysql.log"
MYSQL_TEST_PID_FILE="${TOP_DIR}/mysql.pid"

mkdir "${MYSQL_TEST_DATA_DIR}"
mysql_install_db \
  --datadir="${MYSQL_TEST_DATA_DIR}" \
  --log-error="${MYSQL_TEST_LOG}"

%{_libexecdir}/mysqld \
  --datadir="${MYSQL_TEST_DATA_DIR}" \
  --log-error="${MYSQL_TEST_LOG}" \
  --socket="${MYSQL_TEST_SOCKET}" \
  --pid-file="${MYSQL_TEST_PID_FILE}" \
  --port="${MYSQL_TEST_PORT}" \
  --ssl &

conn_found=false
for i in $(seq 10); do
  echo "Waiting for the DB server to accept connections... ${i}"
  sleep 1
  if grep -q 'ready for connections' "${MYSQL_TEST_LOG}"; then
    conn_found=true
    break
  fi
done
if ! "${conn_found}"; then
  echo "ERROR: Failed to connect the DB server."
  cat "${MYSQL_TEST_LOG}"
  exit 1
fi

# Reset password for the root user due to MariaDB 10.4 authentication change.
# See https://mariadb.com/kb/en/authentication-from-mariadb-104/#altering-the-user-account-to-revert-to-the-previous-authentication-method
mysql -u ${MYSQL_TEST_USER} \
  -e "ALTER USER 'root'@'localhost' IDENTIFIED VIA mysql_native_password USING PASSWORD('')" \
  -S "${MYSQL_TEST_SOCKET}" \
  -P "${MYSQL_TEST_PORT}"

# See https://github.com/brianmario/mysql2/blob/master/ci/setup.sh
mysql -u root \
  -e 'CREATE DATABASE /*M!50701 IF NOT EXISTS */ test' \
  -S "${MYSQL_TEST_SOCKET}" \
  -P "${MYSQL_TEST_PORT}"

# See https://github.com/brianmario/mysql2/blob/master/tasks/rspec.rake
cat <<EOF > spec/configuration.yml
root:
  host: localhost
  username: root
  password:
  database: test
  port: ${MYSQL_TEST_PORT}
  socket: ${MYSQL_TEST_SOCKET}

user:
  host: localhost
  username: ${MYSQL_TEST_USER}
  password:
  database: mysql2_test
  port: ${MYSQL_TEST_PORT}
  socket: ${MYSQL_TEST_SOCKET}
EOF

rspec -Ilib:%{buildroot}%{gem_extdir_mri} -f d spec
popd

# Clean up
kill "$(cat "${MYSQL_TEST_PID_FILE}")"

%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/support
%license %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md


%changelog
* Fri Jan 19 2024 Jarek Prokop <jprokop@redhat.com> - 0.5.5-1
- Upgrade to mysql2 0.5.5.
  Related: RHEL-17089

* Mon May 23 2022 Jarek Prokop <jprokop@redhat.com> - 0.5.4-1
- New upstream release 0.5.4 by merging Fedora rawhide branch (commit: e21b5b9)
  Resolves: rhbz#2063773

* Fri May 29 2020 Jun Aruga <jaruga@redhat.com> - 0.5.3-1
- New upstream release 0.5.3 by merging Fedora master branch (commit: 674d475)
  Resolves: rhbz#1817135

* Tue Jun 11 2019 Jun Aruga <jaruga@redhat.com> - 0.5.2-1
- New upstream release 0.5.2 by merging Fedora master branch (commit: cc15309)
  Resolves: rhbz#1672575

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.4.10-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.10-2
- F-28: rebuild for ruby25

* Thu Nov 23 2017 Jun Aruga <jaruga@redhat.com> - 0.4.10-1
- New upstream release 0.4.10

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Adam Williamson <awilliam@redhat.com> - 0.4.8-1
- New upstream release 0.4.8 (builds against MariaDB 10.2)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Jun 09 2016 Miroslav Suchý <msuchy@redhat.com> - 0.4.4-1
- New upstream release 0.4.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Tue Sep  8 2015 Miroslav Suchý <msuchy@redhat.com> 0.4.0-1
- rebase to mysql2-0.4.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.3.16-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Miroslav Suchý <msuchy@redhat.com> 0.3.16-1
- rebase to mysql2-0.3.16

* Tue Apr 15 2014 Vít Ondruch <vondruch@redhat.com> - 0.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Feb 11 2014 Miroslav Suchý <msuchy@redhat.com> 0.3.15-2
- rebase to mysql2-0.3.15

* Wed Sep 11 2013 Alexander Chernyakhovsky <achernya@mit.edu> - 0.3.13-1
- Initial package
