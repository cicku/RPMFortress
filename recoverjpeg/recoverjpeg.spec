Name:         recoverjpeg
Summary:      Recover jpeg pictures and mov movies from damaged devices
License:      GPLv2
Version:      2.2.3
Release:      1%{?dist}
URL:          http://www.rfc1149.net/devel/recoverjpeg
Source0:      http://www.rfc1149.net/download/%{name}/%{name}-%{version}.tar.gz

Requires:     ImageMagick
Requires:     exif

%description
recoverjpeg tries to recover JFIF (JPEG) pictures 
and MOV movies (using recovermov) from a peripheral. 
This may be useful if you mistakenly overwrite a 
partition or if a device such as a digital camera memory card is bogus.

%prep

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=%{buildroot}

%files
%doc ChangeLog COPYING
%{_bindir}/recovermov
%{_bindir}/remove-duplicates
%{_bindir}/sort-pictures
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
* Mon May 27 2013 Christopher Meng <rpm@cicku.me> - 2.2.3-2
- SPEC cleanup.

* Wed May 01 2013 Christopher Meng <rpm@cicku.me> - 2.2.3-1
- New upstream release with minor fixes.

* Sun Apr 14 2013 Christopher Meng <rpm@cicku.me> - 2.2.2-1
- Initial Package.
