Name:          tsung
Version:       1.5.0
Release:       1%{?dist}
Summary:       A distributed multi-protocol load testing tool
License:       GPLv2
URL:           http://tsung.erlang-projects.org/
Source0:       http://tsung.erlang-projects.org/dist/%{name}-%{version}.tar.gz

BuildRequires: erlang
Requires:      erlang
Requires:      perl(Template)

%description
tsung is a distributed load testing tool. It is protocol-independent and can 
currently be used to stress and benchmark HTTP, Jabber/XMPP, PostgreSQL, 
MySQL and LDAP servers.
It simulates user behaviour using an XML description file, reports many 
measurements in real time (statistics can be customized with transactions, 
and graphics generated using gnuplot).
For HTTP, it supports 1.0 and 1.1, has a proxy mode to record sessions, 
supports GET and POST methods, Cookies, and Basic WWW-authentication. 
It also has support for SSL.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc CHANGES CONTRIBUTORS COPYING README TODO
%{_bindir}/%{name}*
%{_bindir}/tsplot
%{_libdir}/erlang/lib
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man1/tsplot.1*
%{_defaultdocdir}/%{name}/

%changelog
* Sat May 25 2013 Christopher Meng <rpm@cicku.me> - 1.5.0-1
- Initial Package.
