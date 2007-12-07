Summary:	CAMD: constrainted approximate minimum degree
Name:		CAMD
Version:	2.2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/camd/%{name}-%{version}.tar.gz
# Source0-md5:	d80d35bbdb113da3d79e8b52d7b32144
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/camd/
BuildRequires:	UFconfig
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CAMD is a set of routines for ordering a sparse matrix prior
to Cholesky factorization (or for LU factorization with diagonal
pivoting).

%package devel
Summary:	Header files for CAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CAMD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for CAMD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CAMD.

%package static
Summary:	Static CAMD library
Summary(pl.UTF-8):	Statyczna biblioteka CAMD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CAMD library.

%description static -l pl.UTF-8
Statyczna biblioteka CAMD.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	F77="gfortran" \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/camd

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/camd

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libcamd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcamd.so
%{_libdir}/libcamd.la
%{_includedir}/camd

%files static
%defattr(644,root,root,755)
%{_libdir}/libcamd.a
