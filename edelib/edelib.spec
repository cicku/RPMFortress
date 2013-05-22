Name:              edelib
Version:           2.0
Release:           1%{?dist}
Summary:           Small and portable C++ library for EDE
License:           LGPLv2
URL:               http://equinox-project.org/
Source0:           http://downloads.sourceforge.net/project/ede/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:     gettext
BuildRequires:     dbus-devel
#BuildRequires:     libpng-devel
#BuildRequires:     libjpeg-devel
BuildRequires:     fltk-devel
BuildRequires:     doxygen

%description
A small and portable C++ library for EDE (Equinox Desktop Environment). Aims 
are to provide enough background for easier EDE components construction
and development.

%package           devel
Summary:           Development files for %{name}
Requires:	   %{name}%{?_isa} = %{version}-%{release}

%description	   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name} libraries.

%prep
%setup -q
%configure --disable-static
sed -i 's|%{buildroot}||' *.pc edelib/edelib-config.h

%build
jam

%install
jam install #DESTDIR=#{buildroot}
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
jam test

%files
%doc ChangeLog COPYING README
#%{_libdir}/*.so.*

%files devel
#%doc samples/*.cc
#%{_includedir}/%{name}/
#%{_libdir}/*.so

%changelog
* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 2.0-1
- Initial Package.
