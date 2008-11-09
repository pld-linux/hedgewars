#
# TODO:
# - test build with server
%bcond_with	server		# build with local server

Summary:	hedgewars - free Worms-like turn based strategy game
Summary(hu.UTF-8):	hedgewars - ingyenes Worms-szerű körökre osztott stratégiai játék
Summary(pl.UTF-8):	hedgewars - strategia czasu rzeczywistego podobna do Worms
Name:		hedgewars
Version:	0.9.7
Release:	0.5
License:	GPL v2 + Public Domain fonts
Group:		X11/Applications/Games
Source0:	http://hedgewars.org/download/%{name}-src-%{version}.tar.bz2
# Source0-md5:	2326823d2827fb08885dd3944e8692ac
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://www.hedgewars.org/
BuildRequires:	QtCore-devel >= 4.4.0
BuildRequires:	QtSvg-devel >= 4.4.0
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	cmake >= 2.4.4
BuildRequires:	desktop-file-utils
BuildRequires:	fpc >= 2.2.0
%{?with_server:BuildRequires:	ghc}
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hedgewars is a free Worms-like turn based strategy game.

%description -l hu.UTF-8
Hedgewars egy ingyenes Worms-szerű körökre osztott stratégiai játék.

%description -l pl.UTF-8
Hedgewars jest wolnodostępną strategią czasu rzeczywistego podobną do
Worms.

%prep
%setup -q -n %{name}-src-%{version}
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

cd build
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

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
