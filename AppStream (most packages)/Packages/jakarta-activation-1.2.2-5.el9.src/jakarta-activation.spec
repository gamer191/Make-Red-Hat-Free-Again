Name:           jakarta-activation
Version:        1.2.2
Release:        5%{?dist}
Summary:        Jakarta Activation Specification and Implementation
License:        BSD
URL:            https://eclipse-ee4j.github.io/jaf/
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaf-%{version}

%pom_remove_parent
%pom_disable_module demo

%pom_remove_plugin :directory-maven-plugin
sed -i 's/${main.basedir}/${basedir}/' pom.xml

# remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin activation

# set bundle version manually instead of with osgiversion-maven-plugin
# (the plugin is only used to strip off -SNAPSHOT or -Mx qualifiers)
%pom_remove_plugin :osgiversion-maven-plugin
sed -i "s/\${activation.osgiversion}/%{version}/g" activation/pom.xml

%build
# javadoc temporairly disabled due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.md NOTICE.md

# javadoc temporairly disabled due to https://github.com/fedora-java/xmvn/issues/58
#%files javadoc -f .mfiles-javadoc
%files javadoc
%license LICENSE.md NOTICE.md

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.2-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Jun 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.2-4
- Temporarily disable javadoc generation
- Resolves: rhbz#1976997

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.2-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.2-1
- Update to version 1.2.2.
- Drop custom maven-compiler-plugin overrides in favor of upstream settings.

* Wed Jul 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-7
- Override javac source / target versions with 1.8 to fix build with Java 11.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Fabio Valentini <decathorpe@gmail.com> - 1.2.1-5
- Package unretired and renamed from jaf.

