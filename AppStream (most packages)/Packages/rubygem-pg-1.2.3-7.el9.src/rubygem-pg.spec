# Generated from pg-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pg

Name: rubygem-%{gem_name}
Version: 1.2.3
Release: 7%{?dist}
Summary: A Ruby interface to the PostgreSQL RDBMS
# Upstream license clarification (https://bitbucket.org/ged/ruby-pg/issue/72/)
#
# The portions of the code that are BSD-licensed are licensed under
# the BSD 3-Clause license; the contents of the BSD file are incorrect.
#
License: (BSD or Ruby) and PostgreSQL
URL: https://github.com/ged/ruby-pg
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Disable RPATH.
# https://bitbucket.org/ged/ruby-pg/issue/183
Patch0: rubygem-pg-0.17.1-remove-rpath.patch
# Required in ext/pg_text_decoder.c
Requires: rubygem(bigdecimal)
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
This library works with PostgreSQL 9.1 and later.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1

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

# Remove useless shebangs.
sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/Rakefile
sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{gem_instdir}/Rakefile.cross

# Files under %%{gem_libdir} are not executable.
for file in `find %{buildroot}%{gem_libdir} -type f -name "*.rb"`; do
    sed -i '/^#!\/usr\/bin\/env/ d' $file \
    && chmod -v 644 $file
done

%check
pushd .%{gem_instdir}
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
%exclude %{gem_instdir}/.gemtest
%license %{gem_instdir}/BSDL
%license %{gem_instdir}/POSTGRES
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/Contributors.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README-OS_X.rdoc
%doc %{gem_instdir}/README-Windows.rdoc
%doc %{gem_instdir}/README.ja.rdoc
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile*
%{gem_instdir}/spec

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.3-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.3-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.2.3-5
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 19 2020 Jun Aruga <jaruga@redhat.com> - 1.2.3-1
- Update to pg 1.2.3.

* Fri Mar 06 2020 Jun Aruga <jaruga@redhat.com> - 1.2.2-1
- Update to pg 1.2.2.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vít Ondruch <vondruch@redhat.com> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Mon Jan 06 2020 Jun Aruga <jaruga@redhat.com> - 1.2.1-1
- Update to pg 1.2.1.

* Thu Jan 02 2020 Jun Aruga <jaruga@redhat.com> - 1.2.0-1
- Update to pg 1.2.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Thu Jan 10 2019 Vít Ondruch <vondruch@redhat.com> - 1.1.4-1
- Update to pg 1.1.4.

* Wed Jan 09 2019 Vít Ondruch <vondruch@redhat.com> - 1.1.3-2
- Fix PostgreSQL 11 compatibility.

* Tue Sep 18 2018 Jun Aruga <jaruga@redhat.com> - 1.1.3-1
- Update to pg 1.1.3.
- Update to output log when tests fail.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
