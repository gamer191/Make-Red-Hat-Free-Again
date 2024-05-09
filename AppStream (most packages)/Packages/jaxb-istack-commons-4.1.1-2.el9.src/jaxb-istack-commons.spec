Name:           jaxb-istack-commons
Version:        4.1.1
Release:        2%{?dist}
Summary:        iStack Common Utility Code
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-istack-commons
BuildArch:      noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api:2.1.0)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package runtime
Summary:        istack-commons runtime

%description runtime
This package contains istack-commons runtime.

%package test
Summary:        istack-commons test

%description test
This package contains istack-commons test.

%package tools
Summary:        istack-commons tools

%description tools
This package contains istack-commons tools.

%prep
%setup -q

pushd istack-commons

find -name 'module-info.java' -type f -delete

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin . test tools
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Missing dependency on args4j
%pom_disable_module soimp

%pom_disable_module buildtools
%pom_disable_module import-properties-plugin
%pom_disable_module maven-plugin

%mvn_package :istack-commons __noinstall
popd

%build
pushd istack-commons
# Javadoc fails on module.info files: "error: too many module declarations found"
%mvn_build -f -s -j
popd

%install
pushd istack-commons
%mvn_install
popd

%files runtime -f istack-commons/.mfiles-istack-commons-runtime
%license LICENSE.md NOTICE.md
%files test -f istack-commons/.mfiles-istack-commons-test
%license LICENSE.md NOTICE.md
%files tools -f istack-commons/.mfiles-istack-commons-tools
%license LICENSE.md NOTICE.md

%changelog
* Wed Feb 01 2023 Marián Konček <mkoncek@redhat.com> - 4.1.1-2
- Reduce dependencies, reorganize subpackages

* Tue Jan 17 2023 Marian Koncek <mkoncek@redhat.com> - 4.1.1-1
- Initial build
