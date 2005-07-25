Summary:	Jabbah is simple library with very easy to understand API for jabber communicators
Summary(pl):	Jabbah to prosta biblioteka z bardzo ³atwym do zrozumienia API dla komunikatorów jabbera
Name:		jabbah
Version:	0.1
Release:	0.2
License:	GPL v2
Group:		Development
Source0:	http://download.berlios.de/jabbah/%{name}-%{version}.tar.gz
# Source0-md5:	0bbc433e630f245e8b71ecc1481b6cce
URL:		http://jabbah.bazyl.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jabbah is simple library with very easy to understand API for jabber
communicators. Its aim is to implement whole XMPP protocol and as many
JEPs as possible.

%package devel
Summary:        Header files for jabbah library
Summary(pl):    Pliki nag³ówkowe biblioteki jabbah
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       libstdc++-devel

%description devel
Header files for jabbah library.

%description devel -l pl
Pliki nag³ówkowe biblioteki jabbah.

%package static
Summary:        Static version of jabbah libraries
Summary(pl):    Statyczne wersje bibliotek jabbah
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static version of jabbah libraries.

%description static -l pl
Statyczne wersje bibliotek jabbah.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_libdir}/libjabbah*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjabbah*.so
%{_libdir}/libjabbah*.la
%{_includedir}/jabbah*

%files static
%defattr(644,root,root,755)
%{_libdir}/libjabbah*.a
