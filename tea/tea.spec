Name:              tea
Version:           35.0.0
Release:           2%{?dist}
Summary:           A text editor with the hundreds of features
URL:               http://semiletov.org
License:           GPLv3 and Public Domain

Source0:           http://semiletov.org/%{name}/dloads/%{name}-%{version}.tar.bz2
Source1:           %{name}.desktop

BuildRequires:     aspell-devel
BuildRequires:     desktop-file-utils
BuildRequires:     hunspell-devel
BuildRequires:     libpng-devel
BuildRequires:     qt-devel

%description
TEA is a powerful and easy-to-use Qt4-based editor with many useful features 
for HTML, Docbook, and LaTeX editing. It features a small footprint, 
a tabbed layout engine, support for multiple encodings, code snippets, 
templates, customizable hotkeys, an "open at cursor" function for HTML files 
and images, miscellaneous HTML tools, preview in external browser, string 
manipulation functions, Morse-code tools, bookmarks, syntax highlighting, 
and more.

%prep
%setup -q

%build
qmake-qt4 PREFIX=%{_bindir}
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
install -p -D -m 755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 icons/%{name}_icon_v2.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{S:1}

%files
%doc AUTHORS COPYING ChangeLog NEWS NEWS-RU README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Apr 30 2013 Christopher Meng <rpm@cicku.me> - 35.0.0-2
- Errors fixed.

* Tue Mar 26 2013 Christopher Meng <rpm@cicku.me> - 35.0.0-1
- Initial Package.
