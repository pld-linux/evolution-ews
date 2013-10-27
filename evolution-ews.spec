Summary:	Evolution extension for Exchange Web Services
Name:		evolution-ews
Version:	3.10.1
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	49c396c3c454377741ba859ebfac3319
URL:		http://projects.gnome.org/evolution/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	evolution-data-server-devel >= %{version}
BuildRequires:	evolution-devel >= %{version}
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libical-devel
BuildRequires:	libmspack-devel >= 0.4
BuildRequires:	libsoup-devel >= 2.38.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= %{version}
Requires:	evolution-data-server >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
servers, versions 2007 and later, through its Exchange Web Services
(EWS) interface.

%package devel
Summary:	Development files for ews library
Group:		Development/Libraries
Requires:	evolution-data-server-devel >= %{version}
Requires:	libsoup-devel >= 2.38.1

%description devel
This package provides development files for ews library.

%prep
%setup -q

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
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/modules/*.la

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
%attr(755,root,root) %{_libdir}/evolution/3.10/modules/module-ews-configuration.so
%{_datadir}/evolution/3.10/errors/module-ews-configuration.error

%files devel
%defattr(644,root,root,755)
%{_includedir}/evolution-data-server/ews
