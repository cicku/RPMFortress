Name:              nsnake
Version:           1.7
Release:           2%{?dist}
Summary:           Classic snake game on console
URL:               http://www.alexdantas.net/projects/nsnake/
Source0:           http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:           %{name}.6
License:           GPLv3+

BuildRequires:     dos2unix
BuildRequires:     doxygen
BuildRequires:     ncurses-devel

%description
nSnake is a implementation of the classic snake game with textual interface.
It is playable at command-line and uses the nCurses C library for graphics.

%prep
%setup -q
find . -type f -exec dos2unix {} \;
cp -p %{S:1} doc/man/%{name}.6
gzip doc/man/%{name}.6

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}
make doc

%install
install -p -D -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man6
install -p -D -m 644 doc/man/%{name}.6.gz %{buildroot}%{_mandir}/man6/%{name}.6.gz
install -d %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp -pr doc/html/ %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp -pr doc/logo.png %{buildroot}%{_defaultdocdir}/%{name}-%{version}

%files
%doc BUGS ChangeLog COPYING README TODO
%attr(-, -, -)%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

%changelog
* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 1.7-2
- Fix upstream messup.

* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 1.7-1
- New verson with manpages fix.

* Tue May 14 2013 Christopher Meng <rpm@cicku.me> - 1.5-3
- Fix debuginfo.

* Sun May 12 2013 Christopher Meng <rpm@cicku.me> - 1.5-2
- Some fixes.

* Sat Apr 20 2013 Christopher Meng <rpm@cicku.me> - 1.5-1
- Initial Package.
