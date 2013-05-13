Name:              sanewall
Version:           1.1.1
Release:           1%{?dist}
Summary:           A powerful firewall builder

License:           GPLv2+
URL:               http://www.sanewall.org/
Source0:           http://download.sanewall.org/releases/%{version}/%{name}-%{version}.tar.xz
Source1:           %{name}.service

BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     libxslt
Requires:	   iproute
Requires:	   iptables
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

Conflicts:         firehol

%description
Sanewall is a firewall builder for Linux which uses an elegant language 
abstracted to just the right level. This makes it powerful as well as 
easy to use, audit, and understand. It allows you to create very 
readable configurations even for complex stateful firewalls.

Sanewall can be used for almost any firewall need, including:

control of any number of internal/external/virtual interfaces
control of any combination of routed traffic
setting up DMZ routers and servers
all kinds of NAT
providing strong protection (flooding, spoofing, etc.)
transparent caches
source MAC verification
blacklists, whitelists

%prep
%setup -q

%build
%configure --docdir=%{_defaultdocdir}/%{name}-%{version}/
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -d %{buildroot}%{_localstatedir}/spool/%{name}
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{S:1}

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}

%files
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_sysconfdir}/%{name}/services
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_sbindir}/%{name}
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_unitdir}/%{name}.service
%{_localstatedir}/spool/%{name}

%changelog
* Tue May 07 2013 Christopher Meng <rpm@cicku.me> - 1.1.1-1
- New Upstream Release.

* Thu May 02 2013 Christopher Meng <rpm@cicku.me> - 1.1.0-1
- Initial Package.
