Summary:	Evolution extension for Exchange Web Services
Summary(pl.UTF-8):	Rozszerzenie Evolution dla Exchange Web Services
Name:		evolution-ews
Version:	3.22.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Mail
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	4c1a484705039a9f21b0bd733f0725de
Patch0:		%{name}-link.patch
URL:		http://projects.gnome.org/evolution/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	evolution-devel >= %{version}
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gtk+3-devel >= 3.0.0
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
Requires:	glib2 >= 1:2.40.0
Requires:	libsoup >= 2.42.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
servers, versions 2007 and later, through its Exchange Web Services
(EWS) interface.

%description -l pl.UTF-8
Ten pakiet pozwala programowi Evolution współpracować z serwerami
Microsoft Exchange w wersji 2007 lub nowszej poprzez interfejs EWS
(Exchange Web Services).

%package devel
Summary:	Development files for EWS libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek EWS
Group:		X11/Development/Libraries
Requires:	evolution-data-server-devel >= %{version}
Requires:	glib2-devel >= 1:2.40.0
Requires:	libsoup-devel >= 2.42.0

%description devel
This package provides development files for EWS library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne bibliotek EWS.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-data-server/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-data-server/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/modules/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/evolution-data-server/libeews-1.2.so*
%attr(755,root,root) %{_libdir}/evolution-data-server/libewsutils.so*
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/registry-modules/module-ews-backend.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%attr(755,root,root) %{_libdir}/evolution/modules/module-ews-configuration.so
%{_datadir}/evolution/errors/module-ews-configuration.error
%{_datadir}/evolution-data-server/ews
%{_datadir}/appdata/evolution-ews.metainfo.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/evolution-data-server/ews
