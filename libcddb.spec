Summary:	Library to access data on a CDDB server
Summary(pl):	Biblioteka dost�pu do danych na serwerze CDDB
Name:		libcddb
Version:	0.9.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libcddb/%{name}-%{version}.tar.gz
# Source0-md5:	366095f09e1d89d91915a2dd7c7c1478
URL:		http://libcddb.sourceforge.net/
Requires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (http://freedb.org/). It
tries to be as cross-platform as possible.

%description -l pl
libcddb to biblioteka zawieraj�ca implementacje protoko��w (CDDBP,
HTTP, SMTP) dost�pu do danych na serwerze CDDB (http://freedb.org/).
Pr�buje by� przeno�na na ile to mo�liwe.

%package devel
Summary:	Header files for libcddb library
Summary(pl):	Pliki nag��wkowe biblioteki libcddb
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libcddb library.

%description devel -l pl
Pliki nag��wkowe biblioteki libcddb.

%package static
Summary:	Static libcddb library
Summary(pl):	Statyczna biblioteka libcddb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

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
