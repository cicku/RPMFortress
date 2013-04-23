%global datetime   20130423144914

Name:              deepin-music-player
Summary:           A Deepin UI-based music player with brilliant features
License:           GPLv3
Version:           1.0.1
Release:           git%{datetime}%{?dist}

URL:               http://www.linuxdeepin.com

Source0:           http://test.packages.linuxdeepin.com/deepin/pool/main/d/%{name}/%{name}_1+git%{datetime}.tar.gz
Source1:           %{name}.desktop
Source2:           %{name}.png

BuildArch:         noarch
BuildRequires:     gettext
BuildRequires:     python-devel
BuildRequires:     desktop-file-utils

Requires:          dbus-python
Requires:          deepin-ui
Requires:          gstreamer-plugins-bad-free
Requires:          gstreamer-plugins-good
Requires:          gstreamer-python
Requires:          python-CDDB
Requires:          python-chardet
Requires:          pygtk2
Requires:          python-cssselect
Requires:          python-imaging
Requires:          python-keybinder
Requires:          python-mutagen
Requires:          python-pycurl
Requires:          python-pyquery
Requires:          python-xlib
Requires:          scipy

%description
Deepin Music Player with brilliant and tweakful UI Deepin-UI based,
gstreamer front-end, with features likes search music by pinyin,
quanpin, colorful lyrics supports, and more powerful functions.

%prep
%setup -q -n %{name}-1+git%{datetime}

#Tell dmusic where the application is
sed -i 's/dirname/\/usr\/share\/deepin-music-player/' dmusic

%build
cd locale
msgfmt zh_CN.po -o zh_CN.mo
msgfmt zh_HK.po -o zh_HK.mo
msgfmt zh_TW.po -o zh_TW.mo

%install
install -p -D -m 755 dmusic %{buildroot}%{_bindir}/dmusic
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -R app_theme %{buildroot}%{_datadir}/%{name}
cp -R skin %{buildroot}%{_datadir}/%{name}
cp -R src %{buildroot}%{_datadir}/%{name}
install -p -D -m 644 locale/zh_CN.mo %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo
install -p -D -m 644 locale/zh_HK.mo %{buildroot}%{_datadir}/locale/zh_HK/LC_MESSAGES/%{name}.mo
install -p -D -m 644 locale/zh_TW.mo %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{S:1}

#Icon for .desktop
install -p -D -m 644 %{S:2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_bindir}/dmusic

%changelog
* Mon Apr 22 2013 Christopher Meng <cickumqt@gmail.com>  - 1.0.1-git20130423144914.1
- Initial Package for Fedora.
