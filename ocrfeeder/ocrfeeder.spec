Name:               ocrfeeder
Summary:            A document layout analysis and optical character recognition system
Version:            0.7.11
Release:            1%{?dist}
License:            GPLv3+ and LGPLv2+
URL:                http://live.gnome.org/OCRFeeder
Source0:            http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.7/%{name}-%{version}.tar.xz
Source1:            %{name}.desktop

BuildArch:          noarch
BuildRequires:      desktop-file-utils
BuildRequires:      gnome-doc-utils
BuildRequires:      gnome-python2-gtkspell
BuildRequires:      intltool
BuildRequires:      pygoocanvas-devel
BuildRequires:      pygtk2-devel
BuildRequires:      python-enchant
BuildRequires:      python-pillow-sane
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
Requires:           python-pillow
Requires:           python-pillow-sane
Requires:           python-reportlab
Requires:           unpaper

%description
OCRFeeder is a document layout analysis and optical character recognition 
system. Given the images it will automatically outline its contents, 
distinguish between what's graphics and text and perform OCR over the latter.
It generates multiple formats being its main one ODT. And it features a 
complete GTK graphical user interface that allows the users to correct 
any unrecognized characters, defined or correct bounding boxes, set paragraph 
styles, clean the input images, import PDFs, save and load the project, 
export everything to multiple formats, etc.

%prep
%setup -q
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|g' bin/%{name}.in

%build
%configure --libdir=%{_datadir}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{S:1}

#Icon for .desktop
install -p -D -m 644 resources/icons/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/*
%{_datadir}/gnome/help/%{name}/*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man1/*.1*
%{python_sitelib}/*

%changelog
* Wed Feb 27 2013 Christopher Meng <rpm@cicku.me> - 0.7.11-1
- Initial Package.
