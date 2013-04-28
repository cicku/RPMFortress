Name:               minised
Version:            1.14
Release:            1%{?dist}
Summary:            A smaller, cheaper, faster SED implementation
License:            BSD
URL:                http://www.exactcode.de/site/open_source/minised/

Source0:            http://dl.exactcode.de/oss/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	    dietlibc-devel >= 0.32

%description
This is a smaller, cheaper, faster SED implementation. Minix uses it. GNU used
to use it, until they built their own sed around an extended (some would say
over-extended) regexp package. For embedded use we searched for a tiny sed
implementation especially for use with the dietlibc and found Eric S. Raymond's
sed implementation quite handy. Though it suffered several bugs and was not
under active maintenance anymore. After sending a bunch of fixes we agreed to
continue maintaining this lovely, historic sed implementation.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1*

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Feb 21 2013 Christopher Meng <rpm@cicku.me> - 1.14-1
- Initial package.
