%global pkgname  RemoteBox

Name:            remotebox
Version:         1.5
Release:         2%{?dist}
Summary:         Open Source VirtualBox Client with Remote Management
License:         GPLv2+
URL:             http://knobgoblin.org.uk
Source0:         http://knobgoblin.org.uk/downloads/%{pkgname}-%{version}.tar.bz2
Source1:         %{pkgname}.desktop

BuildArch:       noarch
BuildRequires:   desktop-file-utils
Requires:        perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:        perl-Gtk2
Requires:        perl(SOAP::Lite)
Requires:        perl-libwww-perl
Requires:        rdesktop
Requires:        xdg-utils

AutoReq:         no

%description
VirtualBox is traditionally considered to be a virtualisation solution aimed 
at the desktop as opposed to other solutions such as KVM, Xen and VMWare ESX 
which are considered more server orientated solutions. While it is certainly 
possible to install VirtualBox on a server, it offers few remote management 
features beyond using the vboxmanage command line. RemoteBox aims to fill 
this gap by providing a graphical VirtualBox client which is able to 
communicate with and manage a VirtualBox server installation. 

RemoteBox achieves this by using the vboxwebsrv feature of VirtualBox that 
allows its API to be accessed using a protocol called SOAP, even across a 
network. RemoteBox is very similar in look and feel to the native VirtualBox 
interface and allows you to perform most of the same tasks, including 
accessing the display of guests – completely remotely.

%prep
%setup -q -n %{pkgname}-%{version}

# We need to tell RemoteBox where to find it's files
sed -i 's|$Bin/docs|%{_defaultdocdir}/%{name}-%{version}|g' %{name}
sed -i 's|$Bin/|%{_prefix}/|g' %{name} share/%{name}/*.pl

%build

%install
install -p -d %{buildroot}%{_datadir}/%{name}
cp -r share/%{name}/* %{buildroot}%{_datadir}/%{name}/
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{S:1}

#Icon for .desktop
install -p -D -m 644 share/%{name}/icons/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{pkgname}.desktop

%files
%doc docs/changelog.txt docs/%{name}.pdf
%{_datadir}/applications/%{pkgname}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_bindir}/%{name}

%changelog
* Thu Jun 06 2013 Christopher Meng <rpm@cicku.me> - 1.5-2
- SPEC cleanup.
- Fix errors of desktop file.

* Thu Apr 18 2013 Christopher Meng <rpm@cicku.me> - 1.5-1
- Initial Package.
