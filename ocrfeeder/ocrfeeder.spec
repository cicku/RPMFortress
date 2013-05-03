Name:               ocrfeeder
Summary:            Optical Character Recognition program
Version:            0.7.11
Release:            1%{?dist}
License:            GPLv3
URL:                http://live.gnome.org/OCRFeeder
Source0:            http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.7/%{name}-%{version}.tar.xz

BuildRequires:      gnome-doc-utils
BuildRequires:      gnome-python2-gtkspell
BuildRequires:      intltool
BuildRequires:      pygoocanvas-devel
BuildRequires:      pygtk2-devel
BuildRequires:      python-enchant
BuildRequires:      python-imaging-sane
BuildRequires:      python-reportlab
BuildRequires:      python-setuptools
BuildRequires:      sane-backends-libs
Requires:           ghostscript
Requires:           gnome-python2-gtkspell
Requires:           tesseract
Requires:           pygoocanvas
Requires:           pygtk2
Requires:           python
Requires:           python-enchant
Requires:           python-imaging
Requires:           python-imaging-sane
Requires:           python-reportlab
Requires:           unpaper

%description
OCRFeeder is a document layout analysis and optical character recognition 
system. Given the images it will automatically outline its contents, 
distinguish between what's graphics and text and perform OCR over the latter.
It generates multiple formats being its main one ODT.

%prep
%setup -q

%build
%configure --libdir=%{_datadir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}/*/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.1.gz
%{python_sitelib}/*

%changelog
* Wed Feb 27 2013 Christopher Meng <rpm@cicku.me> - 0.7.11-1
- Initial Package.
