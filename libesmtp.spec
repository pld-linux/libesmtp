Summary:	SMTP client library
Summary(pl):	Biblioteka kliencka SMTP
Name:		libesmtp
Version:	1.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.stafford.uklinux.net/libesmtp/%{name}-%{version}.tar.bz2
URL:		http://www.stafford.uklinux.net/libesmtp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim. It may be used as part of a Mail User Agent (MUA) or another
program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.

%description -l pl
LibESMTP to biblioteka obs³uguj±ca wysy³anie poczty elektronicznej
przy u¿yciu SMTP do prekonfigurowanego MTA, np. exima. Mo¿e byæ
u¿ywana jako czê¶æ MTA lub innego programu, który musi umieæ wysy³aæ
pocztê.

%package devel
Summary:	Development resources for libesmtp
Summary(pl):	Pliki dla programistów u¿ywaj±cych libesmtp
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development resources for libesmtp.

%description devel -l pl
Pliki dla programistów u¿ywaj±cych libesmtp.

%package static
Summary:	Static libesmtp libraries
Summary(pl):	Statyczne biblioteki libesmtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libesmtp libraries.

%description static -l pl
Statyczne biblioteki libesmtp.

%prep
%setup -q

%build
%configure \
	%{?debug:--enable-debug}%{!?debug:--disable-debug} \
	--with-auth-plugin-dir=%{_libdir}/esmtp-plugins \
	--enable-pthreads \
	--disable-ltdl-install \
	--enable-require-all-recipients=yes \
	--enable-etrn
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/esmtp-plugins
%attr(755,root,root) %{_libdir}/esmtp-plugins/*.so

%files devel
%defattr(644,root,root,755)
%doc AUTHORS NEWS Notes README
%attr(755,root,root) %{_bindir}/libesmtp-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/esmtp-plugins/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/esmtp-plugins/*.a
