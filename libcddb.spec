%bcond_without	static_libs	# don't build static library
Summary:	Library to access data on a CDDB server
Summary(pl):	Biblioteka dostêpu do danych na serwerze CDDB
Name:		libcddb
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libcddb/%{name}-%{version}.tar.gz
# Source0-md5:	a8f8549cc1afb3bc702a96c7d71d2241
URL:		http://libcddb.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libcdio-devel >= 0.74
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcdio >= 0.74
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org/). It
tries to be as cross-platform as possible.

%description -l pl
libcddb to biblioteka zawieraj±ca implementacje protoko³ów (CDDBP,
HTTP, SMTP) dostêpu do danych na serwerze CDDB (http://freedb.org/).
Próbuje byæ przeno¶na na ile to mo¿liwe.

%package devel
Summary:	Header files for libcddb library
Summary(pl):	Pliki nag³ówkowe biblioteki libcddb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcddb library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libcddb.

%package static
Summary:	Static libcddb library
Summary(pl):	Statyczna biblioteka libcddb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcddb library.

%description static -l pl
Statyczna biblioteka libcddb.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cddb
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
