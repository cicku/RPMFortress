#%global __requires_exclude_from ^%{buildroot}%{_datadir}/%{name}/.*$


Name:              RemoteBox
Version:           1.5
Release:           1%{?dist}
Summary:           Open Source VirtualBox Client with Remote Management

License:           GPLv2+
URL:               http://knobgoblin.org.uk

Source0:           http://knobgoblin.org.uk/downloads/%{name}-%{version}.tar.bz2
Source1:           %{name}.desktop

BuildArch:         noarch
BuildRequires:     desktop-file-utils

Requires:          perl-Gtk2
Requires:          perl(SOAP::Lite)
Requires:          perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:          perl-libwww-perl
Requires:          rdesktop
AutoReq:           no

%description
VirtualBox is traditionally considered to be a virtualisation solution aimed at the desktop as opposed to
other solutions such as KVM, Xen and VMWare ESX which are considered more server orientated
solutions. While it is certainly possible to install VirtualBox on a server, it offers few remote management
features beyond using the vboxmanage command line. RemoteBox aims to fill this gap by providing a
graphical VirtualBox client which is able to communicate with and manage a VirtualBox server
installation. RemoteBox achieves this by using the vboxwebsrv feature of VirtualBox that allows its API
to be accessed using a protocol called SOAP, even across a network. RemoteBox is very similar in look
and feel to the native VirtualBox interface and allows you to perform most of the same tasks, including
accessing the display of guests – completely remotely. In addition, because both VirtualBox and
RemoteBox are supported on many platforms you can for example manage a VirtualBox instance
running on a Windows server using the RemoteBox client installed on Linux or FreeBSD.

%prep
%setup -q

#Add shebangs for .pl
perl -pi -e 'print "#!/usr/bin/perl\n" if $. == 1' share/remotebox/*.pl

%build

%install
install -p -d %{buildroot}%{_datadir}/%{name}
cp -r share/remotebox/* %{buildroot}%{_datadir}/%{name}/
install -p -D -m 755 remotebox %{buildroot}%{_bindir}/remotebox

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE1}

#Icon for .desktop
install -p -D -m 644 share/remotebox/icons/remotebox.png %{buildroot}%{_datadir}/pixmaps/remotebox.png

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc docs/changelog.txt docs/remotebox.pdf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/remotebox.png
%{_datadir}/%{name}/*
%{_bindir}/remotebox

%changelog
* Thu Apr 18 2013 Christopher Meng <rpm@cicku.me> - 1.5-1
- Initial Package.
