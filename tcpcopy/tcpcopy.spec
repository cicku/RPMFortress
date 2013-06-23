Name:           tcpcopy
Version:        0.8.0
Release:        3%{?dist}
Summary:        An online request replication tool
License:        BSD
URL:            https://github.com/wangbin579/tcpcopy
Source0:        https://tcpcopy.googlecode.com/files/fedora_%{name}-%{version}.tar.gz
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
export CPPFLAGS="%{optflags}"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_bindir}/intercept

%changelog
* Fri Jun 21 2013 Christopher Meng <rpm@cicku.me> - 0.8.0-3
- Optimize the build sction.

* Wed Jun 12 2013 Christopher Meng <rpm@cicku.me> - 0.8.0-2
- Remove bundled libraries.

* Fri Jun 07 2013 Christopher Meng <rpm@cicku.me> - 0.8.0-1
- New upstream release.

* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 0.7.0-2
- Fix the incorrect license.

* Wed May 01 2013 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Initial package.
