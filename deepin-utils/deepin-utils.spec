%global datetime   20130423150025

Name:              deepin-utils
Summary:           Basic modules needed by most Linux Deepin applications
License:           GPLv2+
Version:           0.0.1
Release:           git%{datetime}%{?dist}

Url:               http://www.linuxdeepin.com

Source0:           http://test.packages.linuxdeepin.com/deepin/pool/main/d/%{name}/%{name}_%{version}-1+git%{datetime}.tar.gz

BuildRequires:     libsoup-devel
BuildRequires:     pkgconfig(cairo)
BuildRequires:     pkgconfig(pygobject-2.0)
BuildRequires:     pkgconfig(glib-2.0)
BuildRequires:     pkgconfig(gtk+-2.0)
BuildRequires:     pkgconfig(webkit-1.0)
BuildRequires:     python-devel
BuildRequires:     pygtk2-devel
BuildRequires:     python-setuptools
BuildRequires:     webkitgtk-devel

Requires:          numpy
Requires:          webkitgtk

%description
Basic modules needed by most Linux Deepin applications(deepin-prefix).

%prep
%setup -q

%build

%install
export CFLAGS="%{optflags}" 
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc debian/copyright README
%{python_sitearch}/*

%changelog
* Mon Apr 22 2013 Christopher Meng <rpm@cicku.me> - 0.0.1-git20130423150025.1
- Initial Package for Fedora.
