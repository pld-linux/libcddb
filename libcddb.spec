Summary:	Library to access data on a CDDB server
Summary(pl):	Biblioteka dostêpu do danych na serwerze CDDB
Name:		libcddb
Version:	0.9.6
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libcddb/%{name}-%{version}.tar.gz
# Source0-md5:	80269beda3a7a7099bf5492330180e78
URL:		http://libcddb.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libcdio-devel >= 0.67
BuildRequires:	pkgconfig
Requires:	libcdio >= 0.67
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
cp -f /usr/share/automake/config.sub .
%configure
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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
