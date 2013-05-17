Name:           gfeedline
Version:        2.1.1
Release:        1%{?dist}
Summary:        A Social Networking Client

Group:          Applications/Internet
License:        GPL
URL:            http://code.google.com/p/gfeedline/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python2-devel
BuildRequires:  python-distutils-extra
BuildRequires:  pyxdg
Requires:       glib2
Requires:       libproxy-python
Requires:       pygobject2
Requires:       python-twisted-web
Requires:       python-BeautifulSoup
Requires:       python-oauth
Requires:       python-dateutil
Requires:       pyOpenSSL

%description
GFeedLine is a social networking client which supports Twitter, Facebook 
& Tumblr.

%prep
%setup -q
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install share/com.googlecode.gfeedline.gschema.xml.in \
 %{buildroot}%{_datadir}/glib-2.0/schemas/com.googlecode.gfeedline.gschema.xml

%build
glib-compile-schemas %{buildroot}%{_datadir}/glib-2.0/schemas

%install
%{__python} setup.py install --force --root %{buildroot}

desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 644 share/icons/48x48/apps/gfeedline.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -m 644 share/icons/scalable/apps/gfeedline.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc changelog COPYING GPL README
%{_bindir}/*
%{python_sitelib}/*
%{_datarootdir}/gfeedline/*
%{_datarootdir}/glib-2.0/schemas/com.googlecode.gfeedline.gschema.xml
%{_datarootdir}/icons/hicolor/48x48/apps/*
%{_datarootdir}/icons/hicolor/scalable/apps/*
%{_datarootdir}/indicators/messages/applications/gfeedline.indicator
%{_datarootdir}/locale/*/LC_MESSAGES/gfeedline.mo
%{_datarootdir}/applications/gfeedline.desktop

%changelog
* Tue May 14 2013 Christopher Meng <rpm@cicku.me> - 2.1.1-1
- Initial Package.
