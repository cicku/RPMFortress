Name:           nf3d
Version:        0.7
Release:        1%{?dist}
Summary:        GANTT-style visualization for Netfilter connections and logged packets
License:        GPLv3+
Url:            http://github.com/regit/nf3d
Source0:        https://home.regit.org/wp-content/uploads/2013/02/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	python-setuptools

%description
nf3d is a Netfilter visualization tool. It displays connections and
logged packets in a GANTT diagram fashion.

%prep
%setup -q

%build
export CFLAGS="%optflags"
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}
install -p -D -m 644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

%files
%{_bindir}/%{name}
%{python_sitelib}/%{name}*
%{_sysconfdir}/%{name}.conf

%changelog
* Mon May 27 2012 Christopher Meng <rpm@cicku.me> - 0.7-1
- Initial Package.
