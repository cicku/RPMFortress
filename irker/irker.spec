%global _unpackaged_files_terminate_build 0
%global hookdir %{_prefix}/lib/%{name}
%global dname   irkerd

Name:              irker
Version:           1.19
Release:           1%{?dist}
Summary:           IRC Message Relay
License:           BSD
URL:               http://www.catb.org/esr/irker/
Source0:           http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
Source1:           %{dname}.service

BuildRequires:     docbook-style-xsl
BuildRequires:     systemd
BuildRequires:     xmlto
Requires:          python-irc
Requires:          python-simplejson
BuildArch:         noarch

%description
An IRC client that runs as a daemon accepting notification requestsas JSON 
objects presented to a listening socket. It is meant to be used by hook 
scripts in version-control repositories, allowing them to send commit 
notifications to project IRC channels.

%prep
%setup -q
sed -i 's/-o 0 -g 0 //' Makefile

%build
make

%install
make install DESTDIR=%{buildroot}
install -p -D -m 755 irkerhook.py %{buildroot}%{hookdir}/irkerhook.py
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{dname}.service

%post
%systemd_post %{S:1}

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}

%files
%doc COPYING hacking.txt NEWS README security.txt
%{_bindir}/%{dname}
%{_unitdir}/%{dname}.service
%{_mandir}/man*/%{name}*
%{hookdir}/irkerhook.py

%changelog
* Mon May 06 2013 Christopher Meng <rpm@cicku.me> - 1.19-1
- Initial Package.
