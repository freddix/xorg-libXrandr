Summary:	X Randr extension library
Name:		xorg-libXrandr
Version:	1.4.2
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXrandr-%{version}.tar.bz2
# Source0-md5:	210ed9499a3d9c96e3a221629b7d39b0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-proto >= 7.7
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Resize and Rotate extension library.

%package devel
Summary:	Header files for libXrandr library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Resize and Rotate extension library.

This package contains the header files needed to develop programs that
use libXrandr.

%prep
%setup -qn libXrandr-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXrandr.so.?
%attr(755,root,root) %{_libdir}/libXrandr.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrandr.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xrandr.pc
%{_mandir}/man3/*.3x*

