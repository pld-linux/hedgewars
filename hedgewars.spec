#
# Server requires some haskel components that are not available in PLD

Summary:	hedgewars - free Worms-like turn based strategy game
Summary(hu.UTF-8):	hedgewars - ingyenes Worms-szerű körökre osztott stratégiai játék
Summary(pl.UTF-8):	hedgewars - strategia czasu rzeczywistego podobna do Worms
Name:		hedgewars
Version:	1.0.2
Release:	0.2
License:	GPL v2 + Public Domain fonts
Group:		X11/Applications/Games
Source0:	https://www.hedgewars.org/download/releases/%{name}-src-%{version}.tar.bz2
# Source0-md5:	1a91a973201c91bba2a494d428cadfbf
URL:		https://www.hedgewars.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	SDL2_image-devel >= 2.0
BuildRequires:	SDL2_mixer-devel >= 2.0
BuildRequires:	SDL2_net-devel >= 2.0
BuildRequires:	SDL2_ttf-devel >= 2.0
BuildRequires:	cmake >= 2.8.0
BuildRequires:	desktop-file-utils
BuildRequires:	fpc >= 2.2.0
BuildRequires:	libpng-devel
BuildRequires:	lua51-devel
BuildRequires:	openssl-devel
BuildRequires:	physfs-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme


%description
Hedgewars is a free Worms-like turn based strategy game.

%description -l hu.UTF-8
Hedgewars egy ingyenes Worms-szerű körökre osztott stratégiai játék.

%description -l pl.UTF-8
Hedgewars jest wolnodostępną strategią czasu rzeczywistego podobną do
Worms.

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%prep
%setup -q -n %{name}-src-%{version}

%build
mkdir build
cd build
%cmake \
	-DNOSERVER=ON \
	-DNOVIDEOREC=ON \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p ../misc/hedgewars.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Fonts_LICENSE.txt ChangeLog.txt
%attr(755,root,root) %{_bindir}/hedgewars
%attr(755,root,root) %{_bindir}/hwengine
%attr(755,root,root) %{_libdir}/libphyslayer.so
%attr(755,root,root) %{_libdir}/libphyslayer.so.1.0
%{_datadir}/%{name}
%{_datadir}/appdata/hedgewars.appdata.xml
%{_desktopdir}/hedgewars.desktop
%{_pixmapsdir}/hedgewars.png
%{_pixmapsdir}/hedgewars.xpm
