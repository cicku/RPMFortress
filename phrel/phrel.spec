%global  dname phreld
%global _hardened_build 1

Name:              phrel
Version:           1.0.2
Release:           1%{?dist}
Summary:           Per Host RatE Limiter
License:           GPLv2
URL:               http://www.digitalgenesis.com/software/phrel
Source0:           ftp://ftp.digitalgenesis.com/pub/%{name}/%{name}-%{version}.tar.bz2
Source1:           %{dname}.service

Buildrequires:     libpcap-devel
Buildrequires:     mysql-devel
Buildrequires:     net-snmp-devel
BuildRequires:     systemd
Requires:          iptables
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
PHREL is a Per Host RatE Limiter written in C to efficiently track the rate 
of incoming traffic on a per host basis and insert a chain into iptables when 
a configured threshold is crossed. The inserted chain may either rate limit 
or completely block the offending host for a period of time and will be 
automatically removed when the offending host's traffic levels return to 
normal. PHREL can be used with any type of traffic, but it is particularly 
well suited to protecting name servers from random hosts that flood DNS 
requests and preventing SSH brute force login attempts.
 
PHREL now supports IPv6 and syncronization between instances of PHREL via a 
MySQL database. The syncronization feature is designed to work in load 
balanced server farm environments or to simply provide database access to the 
hosts that PHREL is currently monitoring.

%prep
%setup -q

%build
export LDFLAGS="$LDFLAGS -pie -Wl,-z,relro"
%configure --with-snmp --with-mysql
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -D -m 644 contrib/%{dname}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{dname}
install -p -D -m 644 %{dname}.conf %{buildroot}%{_sysconfdir}/%{dname}.conf
install -d %{buildroot}%{_localstatedir}/%{dname}
install -p -D -m 644 %{S:1} %{buildroot}%{_unitdir}/%{dname}.service
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%post
%systemd_post %{S:1}

%preun
%systemd_preun %{S:1}

%postun
%systemd_postun_with_restart %{S:1}

%files
%doc AUTHORS ChangeLog COPYING README 
%doc docs/phrel-dns-article.html docs/%{name}.*
%doc docs/mysql-phrel.sql
%{_sbindir}/%{dname}
%config(noreplace) %{_sysconfdir}/%{dname}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{dname}
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.conf.5*
%{_localstatedir}/%{dname}
%{_unitdir}/%{dname}.service

%changelog
* Thu Jun 06 2013 Christopher Meng <rpm@cicku.me> - 1.0.2-1
- New release.

* Wed May 08 2013 Christopher Meng <rpm@cicku.me> - 1.0.1-1
- Initial Package.
