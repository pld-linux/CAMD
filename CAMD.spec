Summary:	CAMD: Constrainted Approximate Minimum Degree
Summary(pl.UTF-8):	CAMD - przybliżony ograniczony algorytm minimalnego stopnia
Name:		CAMD
Version:	2.4.0
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/camd/%{name}-%{version}.tar.gz
# Source0-md5:	cc9c726fed34365d18e45380890707c2
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/camd/
BuildRequires:	SuiteSparse_config-devel >= 4.3.0
BuildRequires:	libtool >= 2:1.5
Requires:	SuiteSparse_config-libs >= 4.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CAMD is a set of routines for ordering a sparse matrix prior to
Cholesky factorization (or for LU factorization with diagonal
pivoting).

%description -l pl.UTF-8
CAMD to zbiór procedur do porządkowania macierzy rzadkich przed
rozkładem Cholesky'ego (lub do rozkładu LU z obrotami diagonalnymi).

%package devel
Summary:	Header files for CAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CAMD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SuiteSparse_config >= 4.3.0

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
	CFLAGS="%{rpmcflags}" \
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
%doc README.txt Doc/{ChangeLog,License}
%attr(755,root,root) %{_libdir}/libcamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcamd.so.0

%files devel
%defattr(644,root,root,755)
%doc Doc/CAMD_UserGuide.pdf
%attr(755,root,root) %{_libdir}/libcamd.so
%{_libdir}/libcamd.la
%{_includedir}/camd

%files static
%defattr(644,root,root,755)
%{_libdir}/libcamd.a
