%global datetime   20130423145901

Name:              deepin-ui
Summary:           Linux Deepin Graphics Library
License:           GPLv3
Version:           1.0.3
Release:           git%{datetime}%{?dist}

URL:               http://www.linuxdeepin.com

Source0:           http://test.packages.linuxdeepin.com/deepin/pool/main/d/%{name}/%{name}_1+git%{datetime}.tar.gz

BuildRequires:     cairo-devel
BuildRequires:     gcc-c++
BuildRequires:     libsoup-devel
BuildRequires:     python-devel
BuildRequires:     pygtk2-devel
BuildRequires:     python-imaging
BuildRequires:     python-setuptools
BuildRequires:     python-xlib
BuildRequires:     pkgconfig(glib-2.0)
BuildRequires:     scipy
BuildRequires:     webkitgtk-devel

Requires:          webkitgtk
Requires:          deepin-utils

%description
UI toolkit libs for Linux Deepin. Awesome and Beautiful UI libs from Linux Deepin.

%prep
%setup -q -n %{name}-1+git%{datetime}

%build

%install
export CFLAGS="%{optflags}" 
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/pyshared
mv %{buildroot}%{_prefix}/dtk %{buildroot}%{_datadir}/pyshared
mv %{buildroot}/%{_datadir}/pyshared/dtk/locale %{buildroot}/%{_datadir}/locale

#Remove .po and .pot files
rm -rf %{buildroot}/%{_datadir}/locale/*.po*
cd %{buildroot}/%{_prefix}/lib/python2.7/site-packages/dtk
ln -s ../../../../share/pyshared/dtk/theme theme 

# fix permission for all theme.txt files
chmod 0644 %{buildroot}%{_datadir}/pyshared/dtk/theme/*/theme.txt
cd %{_builddir}/%{buildsubdir}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/pyshared
%{python_sitearch}/dtk*

%changelog
* Mon Apr 22 2013 Christopher Meng <rpm@cicku.me> - 1.0.3-git20130423145901.1
- Initial Package for Fedora.
