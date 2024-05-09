Name:           jaxb-dtd-parser
Version:        1.5.0
Release:        1%{?dist}
Summary:        SAX-like API for parsing XML DTDs
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
BuildArch:      noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
SAX-like API for parsing XML DTDs.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

pushd dtd-parser

find -name 'module-info.java' -type f -delete

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
popd

%build
pushd dtd-parser
%mvn_build
popd

%install
pushd dtd-parser
%mvn_install
popd

%files -f dtd-parser/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f dtd-parser/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Tue Jan 17 2023 Marian Koncek <mkoncek@redhat.com> - 1.5.0-1
- Initial build
