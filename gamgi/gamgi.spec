Name:           gamgi	
Version:        0.16.4
Release:        1%{?dist}
Summary:        Build, View and Analyse Atomic Structures
License:        GPLv2	
URL:            http://www.gamgi.org

Source0:        http://www.gamgi.org/src/%{name}-all-%{version}.tar.gz
Source1:        %{name}.desktop
Patch1:         fontpath.patch
Patch2:         arch.patch

BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  freetype-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  ImageMagick
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pango-devel

Requires:       bitstream-vera-sans-fonts
Requires:       bitstream-vera-sans-mono-fonts
Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts
Requires:       netpbm-progs

%description
GAMGI (General Atomistic Modelling Graphic Interface) aims to be useful for: 
  1) the scientific community working in atomistic modelling, who needs 
a graphic interface to build and analyse atomic structures
  2) the scientific community at large, who needs a graphic interface 
to study atomic structures and to prepare images for presentations
  3) teaching the atomic structure of matter in schools and universities, 
even inviting students to run GAMGI at home
  4) science promotion, in exhibitions and science museums.

GAMGI can determine any point group of symmetry, can build crystals for 
any space group of symmetry, can build Random Close Packing structures, 
Voronoi and coordination polyhedra for arbitrary structures. GAMGI 
comes with comprehensive atomic data, including ionic radius and 
isotopic data. GAMGI can handle an arbitrary number of independent windows, 
layers (with different referentials, projections, viewports 
and visibilities), lights (directional, positional and spot), 3D text 
fonts (extruded and stroked). Actions can be performed in a single object 
or in a list of objects previously selected. GAMGI comes with detailed 
but concise documentation, just one click away for each task. 

%prep
%setup -q -n %{name}%{version}
%patch1 -p1 -b .ttf
%ifarch x86_64
%patch2 -p1 -b .x86_64
%endif
gzip doc/man/page

%build
cd src
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_datadir}/%{name}
install -p -D -m 755 src/%{name} %{buildroot}%{_bindir}/%{name}
cp -af dat/* %{buildroot}%{_datadir}/%{name}
install -p -D -m 644 doc/icon/%{name}48.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}/%{_mandir}/man1
install -p -D -m 644 doc/man/page.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

#Install .desktop file with no vendor support.
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{S:1}

%files
%doc AUTHORS CONTRIBUTORS SUPPORTERS doc/LICENSE doc/changelogs/
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Apr 29 2013 Christopher Meng <rpm@cicku.me> - 0.16.4-1
- Initial Package.
