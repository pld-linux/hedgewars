#
# TODO:
# - fix server build (it requires dataenc package from HackageDB - http://hackage.haskell.org/package/dataenc) 
#
%bcond_with	server		# build with local server
#

# there is no ghc on ppc
%ifarch ppc
%undefine	with_server
%endif

Summary:	hedgewars - free Worms-like turn based strategy game
Summary(hu.UTF-8):	hedgewars - ingyenes Worms-szerű körökre osztott stratégiai játék
Summary(pl.UTF-8):	hedgewars - strategia czasu rzeczywistego podobna do Worms
Name:		hedgewars
Version:	0.9.12
Release:	1
License:	GPL v2 + Public Domain fonts
Group:		X11/Applications/Games
Source0:	http://hedgewars.org/download/%{name}-src-%{version}.tar.bz2
# Source0-md5:	10e9815d19df066b5df074fc2cd08c26
Patch0:		%{name}-desktop.patch
URL:		http://www.hedgewars.org/
BuildRequires:	QtCore-devel >= 4.4.0
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel >= 4.4.0
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	cmake >= 2.6.0
BuildRequires:	desktop-file-utils
BuildRequires:	fpc >= 2.2.0
%{?with_server:BuildRequires:	ghc}
%{?with_server:BuildRequires:	gmp-devel}
BuildRequires:	openssl-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hedgewars is a free Worms-like turn based strategy game.

%description -l hu.UTF-8
Hedgewars egy ingyenes Worms-szerű körökre osztott stratégiai játék.

%description -l pl.UTF-8
Hedgewars jest wolnodostępną strategią czasu rzeczywistego podobną do
Worms.

%package server
Summary:	Network server for hedgewars
Summary(pl.UTF-8):	Sieciowy serwer dla hedgewars
Group:		X11/Applications/Games

%description server
Server for playing networked games of hedgewars.

%description server -l pl.UTF-8
Serwer do prowadzenia sieciowych gier hedgewars.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1
mkdir build

%build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_usr} \
	%{?with_server:-DWITH_SERVER=1} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install misc/hedgewars.desktop $RPM_BUILD_ROOT%{_desktopdir}
install misc/hedgewars.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Fonts_LICENSE.txt ChangeLog.txt
%attr(755,root,root) %{_bindir}/hedgewars
%attr(755,root,root) %{_bindir}/hwengine
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop

%if %{with server}
%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hedgewars-server
%endif
