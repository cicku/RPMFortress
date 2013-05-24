Name:               freecode-submit
Version:            2.5
Release:            2%{?dist}
Summary:            A tool help submit release information to freecode.com
License:            BSD
URL:                http://www.catb.org/~esr/freecode-submit/
Source0:            http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz

BuildRequires:      python xmlto
BuildArch:          noarch

%description
freecode-submit is a script that supports remote submission of release 
updates to Freecode via its JSON API. It is intended for use in project 
release scripts. It reads the metadata from an RFC-2822-like message on 
standard input, possibly with overrides by command-line switches. It 
supersedes freshmeat-submit, which no longer works following the site 
name change.

%prep
%setup -q
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|g' %{name}

%build
make %{name}.html

%install
install -p -D -m 755 %{name} "%{buildroot}%{_bindir}/%{name}"
install -p -D -m 644 %{name}.1 "%{buildroot}%{_mandir}/man1/%{name}.1"

%files
%doc AUTHORS COPYING README gold-mega.png %{name}.html
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat May 18 2013 Christopher Meng <rpm@cicku.me> - 2.5-2
- Fix build section.

* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 2.5-1
- Initial package.
