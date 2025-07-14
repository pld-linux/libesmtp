Summary:	SMTP client library
Summary(pl.UTF-8):	Biblioteka kliencka SMTP
Name:		libesmtp
Version:	1.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/libesmtp/libESMTP/releases
Source0:	https://github.com/libesmtp/libESMTP/archive/v%{version}/libESMTP-%{version}.tar.gz
# Source0-md5:	1c89f9af9f56b74ec4dce3fc59a7236f
Patch0:		%{name}-soname.patch
URL:		https://libesmtp.github.io/
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	openssl-devel >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim. It may be used as part of a Mail User Agent (MUA) or another
program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.

%description -l pl.UTF-8
LibESMTP to biblioteka obsługująca wysyłanie poczty elektronicznej
przy użyciu SMTP do prekonfigurowanego MTA, np. exima. Może być
używana jako część MTA lub innego programu, który musi umieć wysyłać
pocztę.

%package devel
Summary:	Development resources for libesmtp
Summary(pl.UTF-8):	Pliki dla programistów używających libesmtp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel >= 1.1.0

%description devel
Development resources for libesmtp.

%description devel -l pl.UTF-8
Pliki dla programistów używających libesmtp.

%package static
Summary:	Static libesmtp libraries
Summary(pl.UTF-8):	Statyczne biblioteki libesmtp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libesmtp libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libesmtp.

%prep
%setup -q -n libESMTP-%{version}
%patch -P0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# plugin interface, not installed by meson
cp -p auth-plugin.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md docs/{ChangeLog.md,NEWS.md,authors.md,bugreport.md,changes-since-v1.0.6.md}
%attr(755,root,root) %{_libdir}/libesmtp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libesmtp.so.6
%dir %{_libdir}/esmtp-plugins-6.2.0
%attr(755,root,root) %{_libdir}/esmtp-plugins-6.2.0/sasl-crammd5.so
%attr(755,root,root) %{_libdir}/esmtp-plugins-6.2.0/sasl-login.so
%attr(755,root,root) %{_libdir}/esmtp-plugins-6.2.0/sasl-ntlm.so
%attr(755,root,root) %{_libdir}/esmtp-plugins-6.2.0/sasl-plain.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesmtp.so
%{_includedir}/auth-client.h
%{_includedir}/auth-plugin.h
%{_includedir}/libesmtp.h
%{_pkgconfigdir}/libesmtp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libesmtp.a
