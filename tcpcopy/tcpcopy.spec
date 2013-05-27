Name:           tcpcopy
Version:        0.7.0
Release:        1%{?dist}
Summary:        An online request replication tool
License:        3 clause BSD
URL:            http://code.google.com/p/tcpcopy
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  libnetfilter_queue-devel
Requires:       iptables

%description
It can help you find bugs without deploying your server software on your 
production servers. It can also be used to do smoke testing.
For example, when you want to migrate from Apache to Nginx, tcpcopy can help 
you test it. Apache is running online, while tcpcopy can copy the TCP flows 
from Apache to Nginx. To Nginx, the TCP flows are just forwarding to it. 
This will not affect Apache at all except cost a little network 
bandwidth and CPU load.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_bindir}/intercept

%changelog
* Wed May 01 2013 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Initial package.
