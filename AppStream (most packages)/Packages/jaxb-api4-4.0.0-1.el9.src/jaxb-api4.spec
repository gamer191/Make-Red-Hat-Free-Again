Name:           jaxb-api4
Version:        4.0.0
Release:        1%{?dist}
Summary:        Jakarta XML Binding API
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-api
BuildArch:      noarch

Source0:        %{url}/archive/%{version}/jaxb-api-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api:2.1.0)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaxb-api-%{version}

find -name 'module-info.java' -type f -delete

# Remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%mvn_compat_version jakarta*: 4 %{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Tue Jan 17 2023 Marian Koncek <mkoncek@redhat.com> - 4.0.0-1
- Initial build
