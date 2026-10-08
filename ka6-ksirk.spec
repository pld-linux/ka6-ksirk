#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	26.08.2
%define		kframever	6.0.0
%define		qtver		6.5.0
%define		kaname		ksirk
Summary:	ksirk
Name:		ka6-%{kaname}
Version:	26.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	33e87b2aeae175a338570e7b0cb5c5b0
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Qt5Compat-devel >= %{qtver}
BuildRequires:	Qt6Multimedia-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	ka6-libkdegames-devel >= 6.0.0
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
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

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

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

%post data
%update_desktop_database_post
%update_icon_cache hicolor

%postun data
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirk
%attr(755,root,root) %{_bindir}/ksirkskineditor

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
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
%{_datadir}/qlogging-categories6/ksirk.renamecategories
