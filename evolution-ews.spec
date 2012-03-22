Summary:	Evolution extension for Exchange Web Services
Name:		evolution-ews
Version:	3.3.92
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/evolution-ews/3.3/%{name}-%{version}.tar.xz
# Source0-md5:	7569af1532e519bf8fd9ead82823e72f
URL:		http://projects.gnome.org/evolution/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.9
BuildRequires:	evolution-data-server-devel >= 3.3.0
BuildRequires:	evolution-devel >= 3.3.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libical-devel
BuildRequires:	libsoup-devel >= 2.30.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	evolution >= 3.3.0
Requires:	evolution-data-server >= 3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows Evolution to interact with Microsoft Exchange
servers, versions 2007 and later, through its Exchange Web Services
(EWS) interface.

%package devel
Summary:	Development files for ews library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	evolution-data-server-devel >= 3.3.0
Requires:	libsoup-devel >= 2.30.0

%description devel
This package provides development files for ews library.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution-data-server/*/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evolution/*/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/liblzx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblzx.so.0
%attr(755,root,root) %{_libdir}/evolution-data-server-3.4/libeews-1.2.so*
%attr(755,root,root) %{_libdir}/evolution-data-server-3.4/libewsutils.so*
%attr(755,root,root) %{_libdir}/evolution-data-server/addressbook-backends/libebookbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/calendar-backends/libecalbackendews.so
%attr(755,root,root) %{_libdir}/evolution-data-server/camel-providers/libcamelews.so
%{_libdir}/evolution-data-server/camel-providers/libcamelews.urls
%attr(755,root,root) %{_libdir}/evolution/3.4/plugins/liborg-gnome-exchange-ews.so
%{_libdir}/evolution/3.4/plugins/org-gnome-exchange-ews.eplug

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblzx.so
%{_includedir}/evolution-data-server-3.4
%{_pkgconfigdir}/libeews-1.2.pc
