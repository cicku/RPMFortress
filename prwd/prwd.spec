Name:         prwd
Version:      1.6
Release:      1%{?dist}
Summary:      A tool can print reduced working directory
License:      ISC

URL:          http://tamentis.com/projects/prwd/
Source0:      http://tamentis.com/projects/prwd/files/prwd-%{version}.tar.gz

%description
Most shells read $PS1 differently and have a very rigid way to display 
the current working directory. prwd allows you to have one way to handle 
the display of your working directory and use it across multiple shells. 
It also allows you to keep an eye on your current branch when you enter 
a project handled by git or mercurial.

%prep
%setup -q
gzip %{name}.1

%build
./configure
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%check
make test

%files
%doc AUTHORS ChangeLog LICENSE prwdrc.example
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu May 16 2013 Christopher Meng <rpm@cicku.me> - 1.6-1
- Initial Package.
