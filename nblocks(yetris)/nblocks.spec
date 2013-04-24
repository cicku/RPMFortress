%global pkgname    yetris

Name:              nblocks
Version:           1.6
Release:           1%{?dist}
Summary:           Classic falling blocks on console
URL:               http://alexdantas.github.io/yetris/
Source0:           http://downloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.gz
License:           GPLv3

BuildRequires:     ncurses-devel

%description
nblocks is a customizable falling blocks game with textual interface.
It has lots of features:
* High score.
* Customizable by commandline arguments and config file.
* Up to 6 next blocks.
* Block hold and Combo sequences.

%prep
%setup -q
sed -i 's/usr\/local/usr/' Makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -p -D -m 644 doc/man/%{pkgname}.6 %{buildroot}%{_mandir}/man6

%files
%doc BUGS ChangeLog COPYING README TODO
%{_bindir}/%{pkgname}
%{_mandir}/man6/%{pkgname}.6*

%changelog
* Sat Apr 20 2013 Christopher Meng <rpm@cicku.me>  - 1.6-1
- Initial Package.
