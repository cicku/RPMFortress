Name:              nsnake
Version:           1.5
Release:           1%{?dist}
Summary:           Classic snake game on console
URL:               http://www.alexdantas.net/projects/nsnake/
Source0:           http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:           GPLv3

BuildRequires:     ncurses-devel

%description
nSnake is a implementation of the classic snake game with textual interface.
It is playable at command-line and uses the nCurses C library for graphics.

%prep
%setup -q
sed -i 's/usr\/local/usr/' Makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc BUGS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

%changelog
* Sat Apr 20 2013 Christopher Meng <rpm@cicku.me>  - 1.5-1
- Initial Package.
