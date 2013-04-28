%global nlname     bekijk

Name:              lookat
Version:           1.4.2
Release:           1%{?dist}
Summary:           User-Friendly Text File Viewer

URL:               http://www.wagemakers.be/english/programs/lookat
License:           GPLv2+

Source0:           http://www.wagemakers.be/downloads/%{name}/%{name}_%{nlname}-%{version}.tar.gz

BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     glibc-devel
BuildRequires:     libtool
BuildRequires:     ncurses-devel
BuildRequires:     pkgconfig

%description
lookat is a program to view text files and manual pages. It is designed to be
more user-friendly than more conventional text viewers such as less. 

%prep
%setup -q -n %{name}_%{nlname}-%{version}

%build
%configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --mandir=%{_mandir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -rf \
    %{buildroot}%{_bindir}/%{nlname} \
    %{buildroot}%{_mandir}/man1/%{nlname}.1 \
    %{buildroot}%{_sysconfdir}/%{name}.conf.default \
    %{buildroot}%{_datadir}/doc/%{name}

%files
%doc AUTHORS ChangeLog COPYING README examples/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Apr 22 2013 Christopher Meng <rpm@cicku.me> - 1.4.2-1
- Initial Package.
