Name:              razercfg
Version:           0.20
Release:           1%{?dist}
Summary:           Razer device configuration tool
License:           GPLv3+
Url:               http://bues.ch/cms/hacking/razercfg.html
Source0:           http://bues.ch/%{name}/%{name}-%{version}.tar.bz2
Source1:           razerd.service

BuildRequires:     cmake
BuildRequires:     libusbx-devel
BuildRequires:     python-qt4
BuildRequires:     python-devel

%description
This is the next generation Razer device configuration tool bringing the 
Razer gaming experience to the free open source world. This utility is a 
replacement for the old deathaddercfg tool. The tool architecture is based 
on "razerd", which is a background daemon doing all of the lowlevel 
privileged hardware accesses. The user interface tools are "razercfg", a 
commandline tool;and "qrazercfg", a QT4 based graphical device configuration 

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_unitdir}/

%{__install} -m 0755 %{SOURCE1} -D %{buildroot}%{_unitdir}/razerd.service

%files

%doc COPYING README
%{_bindir}/*
%{_sbindir}/razerd
%{_unitdir}/razerd.service
%{_libdir}/librazer.so
%{_sysconfdir}/pm/sleep.d/50-razer
%{_udevrulesdir}/01-razer-udev.rules

%changelog
* Sat Apr 27 2013 Christopher Meng <rpm@cicku.me> - 0.20-1
- Initial Package.
