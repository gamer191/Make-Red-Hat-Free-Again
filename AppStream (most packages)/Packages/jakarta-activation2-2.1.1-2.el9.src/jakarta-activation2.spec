Name:           jakarta-activation2
Version:        2.1.1
Release:        2%{?dist}
Summary:        Jakarta Activation API
# the whole project is licensed under (EPL-2.0 or BSD)
# the source code additionally can be licensed under GPLv2 with exceptions
# we only ship built source code
License:        EPL-2.0 or BSD or GPLv2 with exceptions
URL:            https://jakartaee.github.io/jaf-api/
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
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
%setup -q -n jaf-api-%{version}

pushd api
%pom_remove_parent

# remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%mvn_compat_version jakarta*: 2 %{version} 2.1.0 2.0.1 2.0.0
popd

%build
pushd api
%mvn_build
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%files javadoc -f api/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Wed Feb 01 2023 Marián Konček <mkoncek@redhat.com> - 2.1.1-2
- Reduce dependencies

* Tue Jan 17 2023 Marian Koncek <mkoncek@redhat.com> - 2.1.1-1
- Initial build
