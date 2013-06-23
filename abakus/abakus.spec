Name:          abakus
Version:       0.92
Release:       1%{?dist}
Summary:       The simple KDE calculator
License:       GPLv2
URL:           http://purinchu.net/abakus
Source0:       http://purinchu.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: bison
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: kdelibs-devel
BuildRequires: qt-devel

%description
Abakus is a simple calculator for KDE, based on a concept of Roberto 
Alsina's. Think of it as bc (the command-line calculator) with a nice GUI.

%prep
%setup -q

%build
%{cmake}

%install
make install DESTDIR=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%post
touch --no-create %{_iconsdir}/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_iconsdir}/hicolor &> /dev/null
gtk-update-icon-cache %{_iconsdir}/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_iconsdir}/hicolor &> /dev/null || :

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/applications/kde4/*.desktop
%{_kde4_appsdir}/%{name}/

%changelog
* Sun Jan 27 2013 Christopher Meng <rpm@cicku.me> - 0.92-1
- Initial Package.
