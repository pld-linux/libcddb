#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library to access data on a CDDB server
Summary(pl.UTF-8):	Biblioteka dostępu do danych na serwerze CDDB
Name:		libcddb
Version:	1.3.2
Release:	5
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libcddb/%{name}-%{version}.tar.bz2
# Source0-md5:	8bb4a6f542197e8e9648ae597cd6bc8a
URL:		http://libcddb.sourceforge.net/
BuildRequires:	autoconf >= 2.55
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.4
BuildRequires:	libcdio-devel >= 0.76
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcdio >= 0.76
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org/). It
tries to be as cross-platform as possible.

%description -l pl.UTF-8
libcddb to biblioteka zawierająca implementacje protokołów (CDDBP,
HTTP, SMTP) dostępu do danych na serwerze CDDB (http://freedb.org/).
Próbuje być przenośna na ile to możliwe.

%package devel
Summary:	Header files for libcddb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcddb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcddb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcddb.

%package static
Summary:	Static libcddb library
Summary(pl.UTF-8):	Statyczna biblioteka libcddb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcddb library.

%description static -l pl.UTF-8
Statyczna biblioteka libcddb.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install examples
install examples/*.{c,h} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcddb.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/cddb_query
%attr(755,root,root) %{_libdir}/libcddb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcddb.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcddb.so
%{_includedir}/cddb
%{_pkgconfigdir}/libcddb.pc
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcddb.a
%endif
