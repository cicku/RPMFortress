Name:              ascii-design
Version:           1.0.1
Release:           2%{?dist}
Summary:           A tool to create ascii arts
License:           GPLv2

Url:               http://ascii-design.sourceforge.net
Source0:           http://downloads.sourceforge.net/project/%{name}/%{name}/Ascii-Design%20%{version}/%{name}-%{version}.tar.bz2

BuildRequires:     qt-devel
BuildRequires:     desktop-file-utils
BuildRequires:     dos2unix
Requires:          figlet

%description
Ascii Design is a free program based on figlet engine that enables you to 
create awesome ascii art text. You can create art based text for many types 
of decorations for web sites, e-mail, text files etc...
Ascii Design is also able to use dozens of special fonts to create various 
styles of ascii arts.

%prep
%setup -q 
dos2unix COPYING.TXT

%build
qmake-qt4
make %{?_smp_mflags}

%install
install -p -D -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    icon/%{name}.desktop

#Icon for .desktop
install -p -D -m 644 pics/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc COPYING.TXT
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sat May 18 2013 Christopher Meng <rpm@cicku.me> - 1.0.1-2
- Small fix.

* Thu May 02 2013 Christopher Meng <rpm@cicku.me> - 1.0.1-1
- Initial Package.
