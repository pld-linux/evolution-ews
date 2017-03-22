Summary:	Evolution extension for Exchange Web Services
Summary(pl.UTF-8):	Rozszerzenie Evolution dla Exchange Web Services
Name:		evolution-ews
Version:	3.24.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/3.24/%{name}-%{version}.tar.xz
# Source0-md5:	f6be8655dc4b63248e993967e18b15cf
URL:		http://projects.gnome.org/evolution/
BuildRequires:	cmake >= 3.1
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	evolution-devel >= %{version}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libical-devel
BuildRequires:	libmspack-devel >= 0.4
BuildRequires:	libsoup-devel >= 2.42.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= %{version}
Requires:	evolution-data-server >= %{version}
Requires:	glib2 >= 1:2.46.0
Requires:	libsoup >= 2.42.0
Obsoletes:	evolution-ews-devel
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
%cmake \
	-DLIBEXEC_INSTALL_DIR=%{_libdir} \
	-DENABLE_SCHEMAS_COMPILE=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/evolution-ews
%attr(755,root,root) %{_libdir}/evolution-ews/libcamelews-priv.so
%attr(755,root,root) %{_libdir}/evolution-ews/libevolution-ews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%attr(755,root,root) %{_libdir}/evolution/modules/module-ews-configuration.so
%{_datadir}/evolution/errors/module-ews-configuration.error
%{_datadir}/evolution-data-server/ews
%{_datadir}/appdata/evolution-ews.metainfo.xml
