%global datetime   20130418131616

Name:              deepin-screenshot
Version:           2.0
Release:           1%{?dist}
Summary:           Screenshot tool from Linux Deepin
License:           GPLv3
URL:               http://www.linuxdeepin.com/

Source0:           http://test.packages.linuxdeepin.com/deepin/pool/main/d/%{name}/%{name}_%{version}+git%{datetime}.tar.gz
Source1:           %{name}.desktop

Requires:          deepin-ui
Requires:          GConf2
Requires:          gnome-python2-libwnck
Requires:          python-pycurl
Requires:          python-xlib
Requires:          pyxdg
Requires:          pywebkitgtk
Requires:          zbar

BuildRequires:     desktop-file-utils
BuildArch:         noarch

%description
Deepin Screenshot Tool provides a quite easy-to-use screenshot tool.
Features:
    * Global hotkey to triggle screenshot tool
    * Take screenshot of a selected area
    * Easy to add text and line drawings onto the screenshot

%prep
%setup -q -n %{name}-%{version}+git%{datetime}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -R {src,theme,locale} %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/src/%{name} %{buildroot}%{_bindir}/%{name}

mv %{buildroot}/%{_datadir}/%{name}/locale %{buildroot}/%{_datadir}/locale

#Remove .po and .pot files
rm -rf %{buildroot}/%{_datadir}/locale/*.po*

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{S:1}

#Icon for .desktop
install -p -D -m 644 theme/logo/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/%{name}/*

%changelog
* Mon Apr 22 2013 Christopher Meng <rpm@cicku.me>  - 2.0-1
- Initial Package for Fedora.
