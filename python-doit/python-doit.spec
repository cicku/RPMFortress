%global pkgname     doit

%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Name:               python-doit
Version:            0.20.0
Release:            1%{?dist}
Summary:            Python automation tool
License:            MIT
Url:                http://pydoit.org/
Source0:            http://pypi.python.org/packages/source/d/%{pkgname}/%{pkgname}-%{version}.tar.gz

%if 0%{?with_python3}
BuildRequires:      python3-devel
BuildRequires:      python3-inotify
BuildRequires:      python3-mock
BuildRequires:      python3-setuptools
BuildRequires:      python3-sphinx

Requires:           python3-inotify
%else
BuildRequires:      python-devel
BuildRequires:      python-inotify
BuildRequires:      python-mock
BuildRequires:      python-setuptools
BuildRequires:      python-sphinx

Requires:           python-inotify
%endif

BuildArch:          noarch

%description
doit is a build tool (in the same class as make, cmake, scons,
ant and others)

doit can be used as:
  * a build tool (generic and flexible)
  * home of your management scripts (it helps you organize and combine
   shell scripts and python scripts)
  * a functional tests runner (combine together different tools)
  * a configuration management system
  * manage computational pipelines

%if 0%{?with_python3}
%package -n         python3-doit
Summary:            Python automation tool
Requires:           python3-inotify

%description -n python3-doit
doit is a build tool (in the same class as make, cmake, scons,
ant and others)

doit can be used as:
  * a build tool (generic and flexible)
  * home of your management scripts (it helps you organize and combine
   shell scripts and python scripts)
  * a functional tests runner (combine together different tools)
  * a configuration management system
  * manage computational pipelines

%endif

%package            doc
Summary:            Documentation for %{name}
Requires:           %{name} = %{version}-%{release}

%description        doc
Documentation of %{pkgname}

%prep
%setup -q -n %{pkgname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

%build
CFLAGS="%{optflags}" %{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="%{optflags}" %{__python3} setup.py build
popd
%endif

#docs
cd doc
make html
rm -rf _build/html/_sources/ _build/html/.buildinfo
cd -

%install
pushd %{py3dir}
%{__python3} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}
popd
%{__python} setup.py install --skip-build --prefix=%{_prefix} --root %{buildroot}

install -p -D -m 644 bash_completion_%{pkgname} %{buildroot}%{_sysconfdir}/bash_completion.d/%{pkgname}

%check
#%{__python} setup.py test
#pushd %{py3dir}
#%{__python3} setup.py test
#popd

%files
%doc AUTHORS CHANGES LICENSE TODO.txt
%{python_sitelib}/*
%_bindir/%{pkgname}
%{_sysconfdir}/bash_completion.d

%files -n python3-%{pkgname}
%doc AUTHORS CHANGES LICENSE TODO.txt
%{python3_sitelib}/*
%_bindir/%{pkgname}
%{_sysconfdir}/bash_completion.d

%files doc
%doc doc/tutorial
%doc doc/_build/html

%changelog
* Fri Apr 26 2013 Christopher Meng <rpm@cicku.me> - 0.20.0-1
- Initial Package.
