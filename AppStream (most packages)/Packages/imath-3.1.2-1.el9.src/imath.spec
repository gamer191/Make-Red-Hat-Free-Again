%global srcname Imath
%global sover 29
%global pyver_under %(%{python3} -Esc "import sys; sys.stdout.write('{0.major}_{0.minor}'.format(sys.version_info))")

Name:           imath
Version:        3.1.2
Release:        1%{?dist}
Summary:        Library of 2D and 3D vector, matrix, and math operations for computer graphics

License:        BSD
URL:            https://github.com/AcademySoftwareFoundation/Imath
Source0:        https://github.com/AcademySoftwareFoundation/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Patch1:         imath-python-test.patch

BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  python3-devel
# For documentation generation
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  python3-breathe

%description
Imath is a basic, light-weight, and efficient C++ representation of 2D and 3D
vectors and matrices and other simple but useful mathematical objects,
functions, and data types common in computer graphics applications, including
the “half” 16-bit floating-point type.


%package -n python3-%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Python module for Imath

%description -n python3-%{name}
%{summary}.


%package devel
Summary:        Development files for Imath
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       python3-devel

%description devel
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%cmake -DPYTHON=ON -DCMAKE_INSTALL_PREFIX=%{_usr}
%cmake_build

# Generate man docs
cd docs
doxygen
cd ..
PYTHONPATH=${PWD} sphinx-build-3 docs/ html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
DESTDIR=%{buildroot} %cmake_install


%check
# https://github.com/AcademySoftwareFoundation/Imath/issues/151
%ifnarch i686
%ctest
%endif


%files
%license LICENSE.md
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md SECURITY.md
%{_libdir}/libImath-3_1.so.%{sover}*

%files -n python3-%{name}
%{_libdir}/libPyImath_Python%{pyver_under}-3_1.so.%{sover}*
%{python3_sitearch}/imath.so
%{python3_sitearch}/imathnumpy.so

%files devel
%doc html/
%{_includedir}/Imath/
%{_libdir}/pkgconfig/Imath.pc
%{_libdir}/pkgconfig/PyImath.pc
%{_libdir}/cmake/Imath/
%{_libdir}/libImath.so
%{_libdir}/libImath-3_1.so
%{_libdir}/libPyImath_Python%{pyver_under}-3_1.so


%changelog
* Thu Aug 05 2021 Josef Ridky <jridky@redhat.com> - 3.1.2-1
- New upstream release 3.1.2

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.2-4
- Rebuilt for Python 3.10

* Thu May 27 2021 Richard Shaw <hobbes1069@gmail.com> - 3.0.2-3
- Add main package as dependency to python package.

* Tue May 25 2021 Richard Shaw <hobbes1069@gmail.com> - 3.0.2-2
- Update spec per reviewer comments.

* Thu May 20 2021 Richard Shaw <hobbes1069@gmail.com> - 3.0.2-1
- Update to 3.0.2.

* Wed Apr 07 2021 Richard Shaw <hobbes1069@gmail.com> - 3.0.1-1
- Initial packaging.
