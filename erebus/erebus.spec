Name:              erebus
Summary:           2D real-time Role-Playing Game
License:           GPLv3+
Version:           0.7
Release:           1%{?dist}

URL:               http://erebusrpg.sourceforge.net

Source0:           https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}src.zip
Source1:           %{name}.desktop

BuildRequires:     desktop-file-utils
BuildRequires:     gcc-c++
BuildRequires:     phonon
BuildRequires:     phonon-devel
BuildRequires:     qt-devel >= 4.7.3
BuildRequires:     qtwebkit-devel

%description
Erebus is an Open Source RPG (Role-Playing Game), for PCs, smartphones,
tablets and handhelds.

Features:
Classic point-n-click style RPG, with dungeons to explore, enemies to fight,
NPCs to talk to, sub-quests to complete, scenery to interact with, weapons,
treasure and other items to find.
Also supports Rogue-like keyboard controls.
Multiple quests (currently three, more will be added as development
progresses!)
Also provides randomly generated dungeons to explore.
Choice of starting characters (currently Barbarian, Elf, Halfling, 
Ranger, Warrior).
Start straight into the action - none of this "For your first quest, 
please find your next door neighbour's pet cat".
Vector-based world rather than tile-based - so items/scenery can be 
placed in any position, or aligned in any direction.
2D animated graphics, with zoom in/out, and lighting effects.
Completely free and Open Source - no ads, unlike many free Android 
apps.
User interface optimised to work with mouse, keyboard and/or touchscreen.

%prep
%setup -q -n %{name}src
cp %{S:1} %{_builddir}/%{name}src/%{name}.desktop

%build
qmake-qt4

#Match FHS Standard.
sed -i 's|/opt/%{name}|%{_datadir}/%{name}|g' Makefile

make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

#Add symlink for docs.
install -p -d %{buildroot}%{_datadir}/doc/%{name}
mv %{buildroot}%{_datadir}/%{name}/docs/* %{buildroot}%{_datadir}/doc/%{name}

for f in `ls %{buildroot}%{_datadir}/doc/%{name}`
do
ln -s $f %{buildroot}%{_datadir}/%{name}/docs/$f
done


#Add symlink for binary.
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

#Validate .desktop file.
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}64.png
%{_datadir}/%{name}/*
%{_datadir}/doc/%{name}/*
%{_bindir}/%{name}

%changelog
* Mon Apr 22 2013 Christopher Meng <rpm@cicku.me> - 0.7-1
- Initial Package.
