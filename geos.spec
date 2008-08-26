%define major		3
%define major_c		1
%define lib_name	%mklibname %{name} %{major}
%define lib_name_c	%mklibname %{name}_c %{major_c}
%define devel_name	%mklibname %{name} -d

Name:        geos
Version:     3.0.0
Release:     %mkrel 3
License:     LGPLv2+
Summary:     GEOS (Geometry Engine, Open Source) topology library
URL:         http://geos.refractions.net
Source:      http://geos.refractions.net/downloads/%{name}-%{version}.tar.bz2
Patch0:      geos-gcc43.patch
Group:       Sciences/Geosciences
BuildRoot:   %{_tmppath}/%{name}-%{version}-root
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

%package -n %{devel_name}
Summary:	Development Libraries for the GEOS topology library
Group:		Sciences/Geosciences
Requires:	%{lib_name} = %{version}
Requires:	%{lib_name_c} = %{version}
Provides:	%{name}-devel lib%{name}-devel
Obsoletes:	%{lib_name}-devel

%description -n %{devel_name}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.


%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall
%{__rm} -f %{buildroot}/%{_libdir}/*.la
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/geos-config

%clean
rm -Rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post -n %{lib_name_c} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name_c} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/libgeos-%{major}.*.so

%files -n %{lib_name_c}
%defattr(-,root,root)
%{_libdir}/libgeos_c.so.%{major_c}
%{_libdir}/libgeos_c.so.%{major_c}.*

%files -n %{devel_name}
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/geos-config
%{_bindir}/geos-config
%{_bindir}/XMLTester
%dir %{_includedir}/geos
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a



