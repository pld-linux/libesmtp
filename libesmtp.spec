# libesmtp.spec.in
# Based on original file by Carlos Morgado <chbm@chbm.nu>

Summary:  	SMTP client library

%define package	libesmtp
%define ver	0.8.1
%define rel    	2
%define prefix 	/usr
%define plugindir %{prefix}/lib/esmtp-plugins

Name:     	%{package}
Version:  	%{ver}
Release:  	%{rel}

Copyright:	LGPL
Group:    	System Environment/Libraries
Source:  	%{package}-%{ver}.tar.bz2

URL:       	http://www.stafford.uklinux.net/libesmtp/
BuildRoot:	/var/tmp/%{package}-root
Prefix:		%{prefix}

Packager:	Carlos Morgado <chbm@chbm.nu>
Provides:	%{package}
Docdir:		%{_docdir}

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim.  It may be used as part of a Mail User Agent (MUA) or another
program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.
 
%prep 
%setup -T -b 0
#%patch

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --with-auth-plugin-dir=%{plugindir} --enable-pthreads --enable-require-all-recipients=yes
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.GPL NEWS Notes README
%{prefix}/include/libesmtp.h
%{prefix}/include/auth-client.h
%{prefix}/lib/libesmtp.*
%{plugindir}/sasl-*
