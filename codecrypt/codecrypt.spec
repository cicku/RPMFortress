Name:              codecrypt
Version:           1.1
Release:           1%{?dist}
Summary:           The post-quantum cryptography tool
URL:               http://e-x-a.org/codecrypt
Source0:           http://e-x-a.org/%{name}/files/%{name}-%{version}.tar.gz
License:           GPLv3+

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

%files
%doc COPYING README
%{_bindir}/ccr

%changelog
* Wed May 22 2013 Christopher Meng <rpm@cicku.me> - 1.1-1
- Initial Package.
