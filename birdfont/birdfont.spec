Name:           birdfont
Version:        0.19
Release:        1%{?dist}
Summary:        A editor for creating outline vector graphics and exporting fonts
License:        GPLv3+
URL:            http://birdfont.org
Source0:        http://birdfont.org/releases/%{name}-%{version}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libxml2-devel
BuildRequires:  python-doit
BuildRequires:  vala-devel
BuildRequires:  webkitgtk-devel

%description
Birdfont is a font editor that creates outline vector graphics and exports
fonts in SVG, EOT and TTF format.

%package -n     lib%{name}
Summary:        Birdfont shared library.

%description -n lib%{name}
This package provides the shared library for the birdfont editor.

%prep
%setup -q

%build
./configure
doit

%install
./install -d "%{buildroot}"

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1*
%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%files -n lib%{name}
%{_libdir}/lib%{name}.so

%changelog
* Tue Jun 18 2013 Christopher Meng <rpm@cicku.me> - 0.19-1
- New upstream release.

* Sun Apr 21 2013 Christopher Meng <rpm@cicku.me> - 0.18-1
- Initial Package.
