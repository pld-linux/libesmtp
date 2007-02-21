Summary:	SMTP client library
Summary(pl.UTF-8):	Biblioteka kliencka SMTP
Name:		libesmtp
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Libraries
#Source0Download: http://www.stafford.uklinux.net/libesmtp/download.html
Source0:	http://www.stafford.uklinux.net/libesmtp/%{name}-%{version}.tar.bz2
# Source0-md5:	8b4e8a794adc46268f0c6a0b3fb79486
URL:		http://www.stafford.uklinux.net/libesmtp/
BuildRequires:	automake
BuildRequires:	openssl-devel >= 0.9.7c
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
Requires:	openssl-devel >= 0.9.7c

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
%setup -q

%build
cp -f /usr/share/automake/config.sub  .
%configure \
	%{?debug:--enable-debug}%{!?debug:--disable-debug} \
	--enable-etrn \
	--enable-ntlm \
	--enable-pthreads \
	--enable-require-all-recipients=yes \
	--with-auth-plugin-dir=%{_libdir}/esmtp-plugins
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/esmtp-plugins/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS Notes README
%attr(755,root,root) %{_libdir}/libesmtp.so.*.*
%dir %{_libdir}/esmtp-plugins
%attr(755,root,root) %{_libdir}/esmtp-plugins/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libesmtp-config
%attr(755,root,root) %{_libdir}/libesmtp.so
%{_libdir}/libesmtp.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libesmtp.a
