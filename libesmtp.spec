Summary:	SMTP client library
Name:		libesmtp
Version:	0.8.3
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.stafford.uklinux.net/libesmtp/%{name}-%{version}.tar.bz2
URL:		http://www.stafford.uklinux.net/libesmtp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim. It may be used as part of a Mail User Agent (MUA) or another
program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.

%package devel
Summary:	Development resources for libesmtp
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development resources for libesmtp.

%package static
Summary:	Static libesmtp libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libesmtp libraries.

%prep 
%setup -q

%build
(cd libltdl
aclocal
autoconf)
%configure \
	--with-auth-plugin-dir=%{_libdir}/esmtp-plugins \
	--enable-pthreads \
	--disable-ltdl-install \
	--enable-require-all-recipients=yes
%{__make}

gzip -9nf AUTHORS NEWS Notes README

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/esmtp-plugins
%attr(755,root,root) %{_libdir}/esmtp-plugins/*.so
%attr(755,root,root) %{_libdir}/esmtp-plugins/*.la

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/libesmtp-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/esmtp-plugins/*.a
