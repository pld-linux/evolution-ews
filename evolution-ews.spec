Summary:	Evolution extension for Exchange Web Services
Summary(pl.UTF-8):	Rozszerzenie Evolution dla Exchange Web Services
Name:		evolution-ews
Version:	3.36.2
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	24fc32abc9a570a0852d8a9810ced479
URL:		https://wiki.gnome.org/Apps/Evolution
BuildRequires:	cmake >= 3.1
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	evolution-devel >= %{version}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libical-glib-devel >= 3.0.5
BuildRequires:	libmspack-devel >= 0.4
BuildRequires:	libsoup-devel >= 2.58
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= %{version}
Requires:	evolution-data-server >= %{version}
Requires:	glib2 >= 1:2.46.0
Requires:	libical-glib >= 3.0.5
Requires:	libsoup >= 2.58
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
install -d build
cd build
%cmake .. \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DENABLE_SCHEMAS_COMPILE=OFF

%{__make}

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
%{_datadir}/metainfo/org.gnome.Evolution-ews.metainfo.xml
