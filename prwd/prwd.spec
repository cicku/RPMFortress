Name:         prwd
Version:      1.7
Release:      2%{?dist}
Summary:      A tool can print reduced working directory
License:      ISC

URL:          http://tamentis.com/projects/prwd/
Source0:      http://tamentis.com/projects/%{name}/files/%{name}-%{version}.tar.gz

%description
Most shells read $PS1 differently and have a very rigid way to display 
the current working directory. prwd allows you to have one way to handle 
the display of your working directory and use it across multiple shells. 
It also allows you to keep an eye on your current branch when you enter 
a project handled by git or mercurial.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
make test

%files
%doc AUTHORS ChangeLog LICENSE prwdrc.example
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 1.7-2
- SPEC cleanup.

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 1.7-1
- New version.
- Fixes for debuginfo.

* Thu May 16 2013 Christopher Meng <rpm@cicku.me> - 1.6-1
- Initial Package.
