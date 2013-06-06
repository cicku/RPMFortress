%global rev c8e9781

Name:            python-tvrage
Version:         0.4.1
Release:         3%{?dist}
Summary:         Python client for the tvrage.com XML API
License:         BSD
Url:             https://pypi.python.org/pypi/python-tvrage
Source0:         https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:       noarch
BuildRequires:   python2-devel python-setuptools
Requires:        python-BeautifulSoup

%description
python-tvrage is a python based object oriented client interface for 
tvrage.com's XML based api feeds.

%prep
%setup -q -n ckreutzer-%{name}-%{rev}
sed -i '1,2d' tvrage/exceptions.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%check
%{__python} quickinfo_tests.py && %{__python} api_tests.py

%files
%doc AUTHORS LICENSE NEWS README.rst
%{python_sitelib}/tvrage/
%{python_sitelib}/*.egg-info

%changelog
* Sun Jun 02 2013 Christopher Meng <rpm@cicku.me> - 0.4.1-3
- Fix the python env issue.

* Fri May 31 2013 Christopher Meng <rpm@cicku.me> - 0.4.1-2
- Fix rpmlint issues.

* Fri Dec 28 2012 Christopher Meng <rpm@cicku.me> - 0.4.1-1
- Initial Package.
