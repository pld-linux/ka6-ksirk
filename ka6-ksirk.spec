#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.02.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ksirk
Summary:	ksirk
Name:		ka6-%{kaname}
Version:	24.02.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	77bb592fd79c9465b3224c7d06389327
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-kwallet-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel
BuildRequires:	qca-qt6-devel >= 2.1.0
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KsirK is a computerized version of the well known strategic board game
Risk. The goal of the game is simply to conquer the world by attacking
your neighbors with your armies. Features. Support for 1-6 human or
computer (AI) players.

%description -l pl.UTF-8
KsirK jest skomputeryzowaną wersją dobrze znanej strategicznej gry
planszowej Ryzyko. Celem gry jest po prostu podbić świat atakując
sąsiadów przy użyciu swoich armii. Wspiera od 1 do 6 ludzkich lub
komputerowych (AI) graczy.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirk
%attr(755,root,root) %{_bindir}/ksirkskineditor
%{_desktopdir}/org.kde.ksirk.desktop
%{_desktopdir}/org.kde.ksirkskineditor.desktop
%{_datadir}/config.kcfg/ksirksettings.kcfg
%{_datadir}/config.kcfg/ksirkskineditorsettings.kcfg
%{_iconsdir}/hicolor/*x*/apps/ksirk.png
%{_iconsdir}/hicolor/scalable/apps/ksirk.svgz
%{_datadir}/ksirk
%{_datadir}/ksirkskineditor
%{_datadir}/metainfo/org.kde.ksirk.appdata.xml
%{_datadir}/qlogging-categories6/ksirk.categories
%{_datadir}/knsrcfiles/ksirk.knsrc
