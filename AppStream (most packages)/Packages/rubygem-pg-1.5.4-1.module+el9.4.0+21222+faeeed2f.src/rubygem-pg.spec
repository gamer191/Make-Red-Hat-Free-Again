# Generated from pg-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pg

Name: rubygem-%{gem_name}
Version: 1.5.4
Release: 1%{?dist}
Summary: A Ruby interface to the PostgreSQL RDBMS
License: (BSD-2-Clause OR Ruby) AND PostgreSQL
URL: https://github.com/ged/ruby-pg
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/ged/ruby-pg.git
# git -C ruby-pg archive -v -o pg-1.5.4-spec.tar.gz v1.5.4 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Disable RPATH.
# https://github.com/ged/ruby-pg/issues/183
Patch0: rubygem-pg-1.3.0-remove-rpath.patch
# Fix integer arithmetic on timespec struct fields on 32bit systems.
# The time_t type that is the type of timespec struct fields is not guaranteed
# to be any particular size or type. Therefore we need to explicitly retype
# to avoid buffer {over,under}flow.
# See `man 3 timespec` and `man 3 time_t` for further reference.
# https://github.com/ged/ruby-pg/issues/545
# https://github.com/ged/ruby-pg/pull/547
Patch1: rubygem-pg-1.5.4-Explicitly-retype-timespec-fields-to-int64_t.patch
# Fix possible buffer overflows.
# Found when upstream was investigating the following issue:
# https://github.com/ged/ruby-pg/issues/545
# https://github.com/ged/ruby-pg/pull/548
Patch2: rubygem-pg-1.5.4-Fix-possible-buffer-overflows-on-32-bit-systems.patch
# ext/pg_text_decoder.c
Requires: rubygem(bigdecimal)
# lib/pg/text_{de,en}coder.rb
Requires: rubygem(json)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

BuildRequires: postgresql-server libpq-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(rspec)

%description
This is the extension library to access a PostgreSQL database from Ruby.
This library works with PostgreSQL 9.3 and later.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

# Set --verbose to show detail log by $VERBOSE.
# See https://github.com/ged/ruby-pg/blob/master/spec/helpers.rb $VERBOSE
# Assign a random port to consider a case of multi builds in parallel in a host.
# https://github.com/ged/ruby-pg/pull/39
if ! PGPORT="$((54321 + ${RANDOM} % 1000))" ruby -S --verbose \
  rspec -I$(dirs +1)%{gem_extdir_mri} -f d spec; then
  echo "==== [setup.log start ] ===="
  cat tmp_test_specs/setup.log
  echo "==== [setup.log end ] ===="
  false
fi
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/BSDL
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/POSTGRES
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Contributors.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README-OS_X.rdoc
%doc %{gem_instdir}/README-Windows.rdoc
%lang(ja) %doc %{gem_instdir}/README.ja.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile*
%{gem_instdir}/rakelib/*
%{gem_instdir}/certs
%{gem_instdir}/misc
%{gem_instdir}/pg.gemspec
%{gem_instdir}/sample
# The translations are only related to README and the readme is already in
# japanese (AFAICT) when we build an RPM from the gem, so we shouldn't need
# this directory at all.
# https://github.com/ged/ruby-pg/pull/549
%exclude %{gem_instdir}/translation

%changelog
* Fri Jan 19 2024 Jarek Prokop <jprokop@redhat.com> - 1.5.4-1
- Upgrade to pg 1.5.4.
  Related: RHEL-17089

* Thu May 26 2022 Jarek Prokop - 1.3.5-1
- Update to pg 1.3.5
  Related: rhbz#2063773

* Fri May 29 2020 Jun Aruga <jaruga@redhat.com> - 1.2.3-1
- Update to pg 1.2.3 by merging Fedora master branch (commit: 5db4d26)
  Resolves: rhbz#1817135

* Wed Jun 12 2019 Jun Aruga <jaruga@redhat.com> - 1.1.4-1
- Update to pg 1.1.4 by merging Fedora master branch (commit: 397796e)
  * BuildRequires: s/postgresql-devel/libpq-devel/
  * Add marking lines at the start and end of the setup.log
  Resolves: rhbz#1672575

* Thu May 23 2019 Jun Aruga <jaruga@redhat.com> - 1.0.0-2
- Assign a random testing port.

* Tue Feb 13 2018 Vít Ondruch <vondruch@redhat.com> - 1.0.0-1
- Update to pg 1.0.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.21.0-4
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Vít Ondruch <vondruch@redhat.com> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Fri Dec 08 2017 Jun Aruga <jaruga@redhat.com> - 0.21.0-2
- Fix failed tests for PostgreSQL-10.

* Thu Aug 17 2017 Vít Ondruch <vondruch@redhat.com> - 0.21.0-1
- Update to pg 0.21.0.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Vít Ondruch <vondruch@redhat.com> - 0.20.0-1
- Update to pg 0.20.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.18.4-3
- F-26: rebuild for ruby24
- Patch from the upstream for test failure with integer unification

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Vít Ondruch <vondruch@redhat.com> - 0.18.4-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3
- Update to pg 0.18.4.

* Wed Aug 26 2015 Vít Ondruch <vondruch@redhat.com> - 0.18.2-1
- Update to pg 0.18.2.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.18.1-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Update to pg 0.18.1.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Vít Ondruch <vondruch@redhat.com> - 0.17.1-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Update to pg 0.17.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 0.14.1-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to pg 0.14.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.2-2
- Obsolete ruby-postgress, which was retired.

* Tue Jan 24 2012 Vít Ondruch <vondruch@redhat.com> - 0.12.2-1
- Rebuilt for Ruby 1.9.3.
- Upgrade to pg 0.12.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-5
- Pass CFLAGS to extconf.rb.

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-4
- Binary extension moved into ruby_sitearch dir.
- -doc subpackage made architecture independent.

* Wed Jun 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-3
- Quoted upstream license clarification.

* Mon May 30 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-2
- Removed/fixed shebang in non-executables.
- Removed sources.

* Thu May 26 2011 Vít Ondruch <vondruch@redhat.com> - 0.11.0-1
- Initial package
