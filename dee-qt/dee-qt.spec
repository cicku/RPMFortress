%global bzr     1
%global ubuntu  14.04
%global bzrdate 20140317
%global dpkgver %{?ubuntu}.%{?bzrdate}

Name:           dee-qt
Summary:        Qt bindings and QML plugins for Dee
Version:        3.3
Release:        1%{?bzr:.%{?bzrdate}bzr}%{dist}
License:        GPLv3+
URL:            https://launchpad.net/dee-qt
Source0:        http://archive.ubuntu.com/ubuntu/pool/main/d/dee-qt/%{name}_%{version}%{?bzr:+%{?dpkgver}}.orig.tar.gz
Patch0:         0001-dee-qt-cmakefile-multi-lib-support.patch
BuildRequires:  cmake
# I don't have time to package it, it's dead upstream, all Ubuntu softwares suck.
# BuildRequires:  dbus-test-runner
BuildRequires:  dee-devel >= 1.2.5

%description
dee-qt is a Qt library developed by the Canonical Desktop Experience team 
which provides a set of Qt bindings and QML plugins for dee.

This package contains 2 subpackages, dee-qt4 and dee-qt5, which are 
corresponding to the different Qt versions (currently Qt 4 and Qt 5).

%package -n     dee-qt4
Summary:        Qt4 binding and QML plugin for Dee
BuildRequires:  qt4-devel

%description -n dee-qt4
dee-qt is a Qt library developed by the Canonical Desktop Experience team 
which provides a set of Qt bindings and QML plugins for dee.

This package contains Qt4 binding and QML plugin for Dee.

%package -n     dee-qt4-devel
Summary:        Development files for %{name}
Requires:       dee-qt4%{?_isa} = %{version}-%{release}

%description -n dee-qt4-devel
This package contains libraries and header files for
developing applications that use dee-qt4.

%package -n     dee-qt5
Summary:        Qt5 binding and QML plugin for Dee
BuildRequires:  qt5-qtbase-devel

%description -n dee-qt5
dee-qt is a Qt library developed by the Canonical Desktop Experience team 
which provides a set of Qt bindings and QML plugins for dee.

This package contains Qt5 binding and QML plugin for Dee.

%package -n     dee-qt5-devel
Summary:        Development files for %{name}
Requires:       dee-qt5%{?_isa} = %{version}-%{release}

%description -n dee-qt5-devel
This package contains libraries and header files for
developing applications that use dee-qt5.

%prep
%setup -q %{?bzr:-n %{name}-%{version}+%{?dpkgver}}
%patch0 -p1

# pkgconfig file multi-lib-support.
sed -i 's|${exec_prefix}/lib|${libdir}|' libdee-qt.pc.in

%build
mkdir {build_qt4,build_qt5}
pushd build_qt4
%cmake ..
popd
pushd build_qt5
%cmake -DWITHQT5=1 ..
popd
#make_build
make %{?_smp_mflags} -C build_qt4
make %{?_smp_mflags} -C build_qt5

%install
%make_install -C build_qt4
%make_install -C build_qt5

%check
# Missing BR for %%check.
# make test

%post -n dee-qt4 -p /sbin/ldconfig

%post -n dee-qt5 -p /sbin/ldconfig

%postun -n dee-qt4 -p /sbin/ldconfig

%postun -n dee-qt5 -p /sbin/ldconfig

%files -n dee-qt4
%license COPYING
%{_libdir}/libdee-qt4.so.*
%{_qt4_importdir}/Dee.3/libDeePlugin.so
%{_qt4_importdir}/Dee.3/qmldir

%files -n dee-qt4-devel
%{_libdir}/libdee-qt4.so
%{_libdir}/pkgconfig/libdee-qt4.pc
%{_includedir}/libdee-qt4/deelistmodel.h

%files -n dee-qt5
%license COPYING
%{_libdir}/libdee-qt5.so.*
%{_libdir}/qt5/qml/Dee.3/libDeePlugin.so
%{_libdir}/qt5/qml/Dee.3/qmldir

%files -n dee-qt5-devel
%{_libdir}/libdee-qt5.so
%{_libdir}/pkgconfig/libdee-qt5.pc
%{_includedir}/libdee-qt5/deelistmodel.h

%changelog
* Thu Apr 17 2014 Christopher Meng <rpm@cicku.me> - 3.3-1.14.04.20140317bzr
- Update to 3.3+14.04.20140317

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 3.0-1
- Initial Package.
