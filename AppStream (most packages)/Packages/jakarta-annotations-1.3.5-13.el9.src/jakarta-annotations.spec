%bcond_with bootstrap

Name:           jakarta-annotations
Version:        1.3.5
Release:        13%{?dist}
Summary:        Jakarta Annotations
License:        EPL-2.0 or GPLv2 with exceptions
URL:            https://github.com/eclipse-ee4j/common-annotations-api
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/common-annotations-api/archive/%{version}/common-annotations-api-%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

Provides:       glassfish-annotation-api = %{version}-%{release}

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of programming
that applies across a variety of Java technologies.

%{?javadoc_package}

%prep
%setup -q -n common-annotations-api-%{version}

# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent

# disable spec submodule: it's not needed, and
# it has missing dependencies (jruby, asciidoctor-maven-plugin, ...)
%pom_disable_module spec

# remove plugins not needed for RPM builds
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :findbugs-maven-plugin api
%pom_remove_plugin :spec-version-maven-plugin api

# provide aliases for the old artifact coordinates
%mvn_alias jakarta.annotation:jakarta.annotation-api \
  javax.annotation:javax.annotation-api \
  javax.annotation:jsr250-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
* Mon Jan 30 2023 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.5-13
- Rebuild to regenerate auto-requires

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.5-12
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 09 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.5-11
- Rebuild to workaround DistroBaker issue

* Tue Jun 08 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.5-10
- Bootstrap Maven for CentOS Stream 9

* Wed May 26 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.5-9
- Re-add provides on glassfish-annotation-api

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.5-8
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Jerry James <loganjerry@gmail.com> - 1.3.5-6
- Remove duplicate aliases

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Alexander Kurtakov <akurtako@redhat.com> 1.3.5-4
- Add alias for jsr250-api

* Fri Jun 19 2020 Mat Booth <mat.booth@redhat.com> - 1.3.5-3
- Remove uneeded plugin invokations

* Mon May 11 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3.5-2
- Fix typo in obsoleted package name.

* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3.5-1
- Initial package renamed from glassfish-annotation-api.
