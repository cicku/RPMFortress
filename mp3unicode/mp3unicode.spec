Name:           mp3unicode
Version:        1.2.1
Release:        1%{?dist}
Summary:        Convert MP3 tags to Unicode
License:        GPLv2+
URL:            http://mp3unicode.sourceforge.net/
Source0:        https://github.com/downloads/alonbl/mp3unicode/mp3unicode-%{version}.tar.bz2
BuildRequires:  libxslt
BuildRequires:  taglib-devel

%description
MP3Unicode is a command line utility to convert ID3 tags in mp3 files 
between different encodings.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

rm -frv %{buildroot}%{_pkgdocdir}

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/mp3unicode
%{_mandir}/man1/mp3unicode.1*

%changelog
* Sat Feb 02 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-1
- Initial Package.
