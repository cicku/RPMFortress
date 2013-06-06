Name:              codecrypt
Version:           1.2
Release:           1%{?dist}
Summary:           The post-quantum cryptography tool
URL:               http://e-x-a.org/codecrypt
Source0:           http://e-x-a.org/%{name}/files/%{name}-%{version}.tar.gz
License:           LGPLv3+ and 3 clause BSD and 2 clause BSD

BuildRequires:     gmp-devel

%description
This is a GnuPG-like unix program for encryption and signing that uses only 
quantum-computer-resistant algorithms:
McEliece cryptosystem (compact quasi-dyadic variant) for encryption;
Hash-based Merkle tree algorithm (FMTSeq variant) for digital signatures.

%prep
%setup -q

%build
%configure
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
gzip %{buildroot}%{_mandir}/man1/ccr.1

%files
%doc COPYING README
%{_bindir}/ccr
%{_mandir}/man1/*.1*

%changelog
* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 1.2-1
- New upstream release.

* Wed May 22 2013 Christopher Meng <rpm@cicku.me> - 1.1-1
- Initial Package.
