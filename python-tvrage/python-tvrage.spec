%global rev c8e9781

Name:            python-tvrage
Version:         0.4.1
Release:         1%{?dist}
Summary:         Python client for the tvrage.com XML API
License:         BSD
Url:             https://pypi.python.org/pypi/python-tvrage
Source0: 	 https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:       noarch
BuildRequires:   python-devel python-setuptools
Requires:        python-BeautifulSoup

%description
python-tvrage is a python based object oriented client interface for 
tvrage.com's XML based api feeds.

%prep
%setup -q -n ckreutzer-%{name}-%{rev}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%doc AUTHORS LICENSE NEWS README.rst
%{python_sitelib}/*

%changelog
* Fri Dec 28 2012 Christopher Meng <rpm@cicku.me> - 0.4.1-1
- Initial Package.
