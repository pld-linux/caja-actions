Summary:	Caja file manager extension to launch programs through the popup menu of selected files
Summary(pl.UTF-8):	Rozszerzenie zarządcy plików Caja do uruchamiania programów poprzez menu dla wybranych plików
Name:		caja-actions
Version:	1.26.0
Release:	1
License:	GPL v2+ (code), FDL v1.3+ (help)
Group:		X11/Applications
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	bc708b6f077008bf93a7442e800e2ee4
URL:		https://wiki.mate-desktop.org/mate-desktop/components/caja-actions/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	caja-devel >= 1.17.1
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.32.1
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	libgtop-devel >= 1:2.23.1
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6
BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel >= 1.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	caja >= 1.17.1
Requires:	glib2 >= 1:2.32.1
Requires:	gtk+3 >= 3.10
Requires:	hicolor-icon-theme
Requires:	libgtop >= 1:2.23.1
Requires:	libxml2 >= 1:2.6
Requires:	xorg-lib-libSM >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Caja-actions is an extension for Caja file manager which allows the
user to add arbitrary program to be launched through the Caja file
manager popup menu of selected files.

%description -l pl.UTF-8
Caja-actions to rozszerzenie zarządcy plików Caja, pozwalające
użytkownikowi dodawać dowolne programy do uruchamiania poprzez
rozwijane menu dla wybranych plików w zarządcy plików.

%package devel
Summary:	Caja-Actions extension interface
Summary(pl.UTF-8):	Interfejs rozszerzeń Caja-Actions
Group:		Development/Libraries
Requires:	glib2-devel >= 1:2.32.1
# doesn't require base

%description devel
Caja-Actions extension interface.

%description devel -l pl.UTF-8
Interfejs rozszerzeń Caja-Actions.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/libcaja-actions-*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja-actions/libna-*.la

# files packaged as %doc + HTML and PDF version of help
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/caja-actions

# not supported by glibc (2.34)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,ku_IQ}

# caja-actions gettext domain, caja-actions-config-tool help
%find_lang %{name} --with-mate --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/caja-actions-config-tool
%attr(755,root,root) %{_bindir}/caja-actions-new
%attr(755,root,root) %{_bindir}/caja-actions-print
%attr(755,root,root) %{_bindir}/caja-actions-run
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so
%dir %{_libdir}/caja-actions
%attr(755,root,root) %{_libdir}/caja-actions/libna-core.so
%attr(755,root,root) %{_libdir}/caja-actions/libna-io-desktop.so
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/caja-actions
%endif
%attr(755,root,root) %{_libexecdir}/caja-actions/na-print-schemas
%attr(755,root,root) %{_libexecdir}/caja-actions/na-set-conf
%{_datadir}/caja-actions
%{_desktopdir}/cact.desktop
%{_iconsdir}/hicolor/*x*/apps/caja-actions.png
%{_iconsdir}/hicolor/scalable/apps/caja-actions.svg

%files devel
%defattr(644,root,root,755)
%{_includedir}/caja-actions
