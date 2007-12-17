
%define lib_name	%mklibname %{name} 2
%define lib_name_c %mklibname %{name}_c 1

Name:        geos
Version:     2.2.3
Release:     %mkrel 2
License:     LGPL
Summary:     GEOS (Geometry Engine, Open Source) topology library
URL:         http://geos.refractions.net
Source:      %{name}-%{version}.tar.bz2
Group:       Sciences/Geosciences
BuildRequires: multiarch-utils

%description
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%package -n %{lib_name}
Summary:	Libraries for GEOS
Group:		Sciences/Geosciences
Provides:	%{name} lib%{name}

%description -n %{lib_name}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%package -n %{lib_name_c}
Summary:	Libraries for GEOS
Group:		Sciences/Geosciences

%description -n %{lib_name_c}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%package -n %{lib_name}-devel
Summary:	Development Libraries for the GEOS topology library
Group:		Sciences/Geosciences
Requires:	%{lib_name} = %{version}
Requires:	%{lib_name_c} = %{version}
Provides:	%{name}-devel lib%{name}-devel

%description -n %{lib_name}-devel
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.


%prep
%setup -q

%build
%configure
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall
%{__rm} -f %{buildroot}/%{_libdir}/*.la
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/geos-config

%clean
rm -Rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%post -n %{lib_name_c} -p /sbin/ldconfig
%postun -n %{lib_name_c} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libgeos.so.*

%files -n %{lib_name_c}
%defattr(-,root,root)
%{_libdir}/libgeos_c.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/geos-config
%{_bindir}/geos-config
%{_bindir}/XMLTester
%dir %{_includedir}/geos
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a



