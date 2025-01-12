%define		evo_ver	3.54.3
Summary:	Evolution extension for Exchange Web Services
Summary(pl.UTF-8):	Rozszerzenie Evolution dla Exchange Web Services
Name:		evolution-ews
Version:	3.54.3.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	https://download.gnome.org/sources/evolution-ews/3.54/%{name}-%{version}.tar.xz
# Source0-md5:	f085f43be54dfa403b5a8f71beec9013
URL:		https://gitlab.gnome.org/GNOME/evolution/-/wikis/home
BuildRequires:	cmake >= 3.15
BuildRequires:	evolution-data-server-devel >= %{evo_ver}
BuildRequires:	evolution-data-server-gtk3-devel >= %{evo_ver}
BuildRequires:	evolution-devel >= %{evo_ver}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.68
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel >= 1.0.4
BuildRequires:	libical-glib-devel >= 3.0.5
BuildRequires:	libmspack-devel >= 0.4
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= %{evo_ver}
Requires:	evolution-data-server >= %{evo_ver}
Requires:	glib2 >= 1:2.68
Requires:	json-glib >= 1.0.4
Requires:	libical-glib >= 3.0.5
Requires:	libsoup3 >= 3.0
Obsoletes:	evolution-ews-devel < 3.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
servers, versions 2007 and later, through its Exchange Web Services
(EWS) interface.

%description -l pl.UTF-8
Ten pakiet pozwala programowi Evolution współpracować z serwerami
Microsoft Exchange w wersji 2007 lub nowszej poprzez interfejs EWS
(Exchange Web Services).

%prep
%setup -q

%build
%cmake -B build \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DENABLE_SCHEMAS_COMPILE=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/evolution-ews
%attr(755,root,root) %{_libdir}/evolution/modules/module-ews-configuration.so
%attr(755,root,root) %{_libdir}/evolution/modules/module-microsoft365-configuration.so
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendmicrosoft365.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendmicrosoft365.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelmicrosoft365.so
%{_libdir}/evolution-data-server/camel-providers/libcamelmicrosoft365.urls
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-microsoft365-backend.so
%attr(755,root,root) %{_libdir}/evolution-ews/libcamelews-priv.so
%attr(755,root,root) %{_libdir}/evolution-ews/libevolution-ews.so
%attr(755,root,root) %{_libdir}/evolution-ews/libevolution-ews-common.so
%attr(755,root,root) %{_libdir}/evolution-ews/libevolution-microsoft365.so
%{_datadir}/evolution/errors/module-ews-configuration.error
%{_datadir}/evolution-data-server/ews
%{_datadir}/metainfo/org.gnome.Evolution-ews.metainfo.xml
