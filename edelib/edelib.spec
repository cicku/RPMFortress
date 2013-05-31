Name:              edelib
Version:           2.0
Release:           2%{?dist}
Summary:           Small and portable C++ library for EDE
License:           LGPLv2
URL:               http://equinox-project.org/
Source0:           http://downloads.sourceforge.net/project/ede/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:            fix.patch

BuildRequires:     doxygen
BuildRequires:     fltk-devel
BuildRequires:     dbus-devel
BuildRequires:     gettext
BuildRequires:     jam
BuildRequires:     libX11
BuildRequires:     libjpeg-devel
BuildRequires:     libpng-devel

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

%package           doc
Summary:           Documentation for the %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}
BuildArch:         noarch

%description       doc
This package contains document files for %{name}.

%prep
%setup -q
%patch0

%build
./configure --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir}
sed -i 's|%{buildroot}||' *.pc edelib/edelib-config.h
jam

%install
jam install
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
jam test

%files
%{_bindir}/%{name}*
%{_libdir}/%{name}/

%files devel
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}/

%files doc
%{_defaultdocdir}/%{name}-2.0.0/

%changelog
* Fri May 31 2013 Christopher Meng <rpm@cicku.me> - 2.0-2
- Split out the doc package.

* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 2.0-1
- Initial Package.
