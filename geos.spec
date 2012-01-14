Name:  geos
Version: 3.3.2
Release: 1
License: LGPLv2+
Summary: GEOS (Geometry Engine, Open Source) topology library
URL: http://trac.osgeo.org/geos
Source0: http://download.osgeo.org/geos/%{name}-%{version}.tar.bz2  
Group: Sciences/Geosciences
BuildRequires: multiarch-utils

%description
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

#-----------------------------------------------------------------------------

%define major 3
%define libname	%mklibname geos %{major}

%package -n %{libname}
Summary: Libraries for GEOS
Group: Sciences/Geosciences
Provides: %{name} lib%{name}

%description -n %{libname}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgeos-%{version}.so

#-----------------------------------------------------------------------------

%define major_c	1
%define libname_c %mklibname geos_c %{major_c}

%package -n %{libname_c}
Summary: Libraries for GEOS
Group: Sciences/Geosciences

%description -n %{libname_c}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{libname_c}
%defattr(-,root,root)
%{_libdir}/libgeos_c.so.%{major_c}*

#-----------------------------------------------------------------------------

%define devel_name	%mklibname %{name} -d

%package -n %{devel_name}
Summary: Development Libraries for the GEOS topology library
Group: Sciences/Geosciences
Requires: %{libname} = %{version}
Requires: %{libname_c} = %{version}
Provides: %{name}-devel = %{version}
Provides: libgeos-devel = %{version}
Obsoletes: %{mklibname -d geos 3}

%description -n %{devel_name}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{devel_name}
%defattr(-,root,root)
%{_bindir}/geos-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%multiarch %{multiarch_bindir}/geos-config

%exclude %{_libdir}/libgeos-%{version}.so

#-----------------------------------------------------------------------------

%define devel_name_static %mklibname %{name} -d -s

%package -n %{devel_name_static}
Summary: Development Libraries for the GEOS topology library
Group: Sciences/Geosciences
Requires: %{devel_name} = %{version}
Provides: %{name}-static-devel = %{version}
Provides: libgeos-static-devel = %{version}
Obsoletes: %{mklibname -d geos 3}
Obsoletes: %{mklibname -d -s geos 3}

%description -n %{devel_name_static}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{devel_name_static}
%defattr(-,root,root)
%{_libdir}/*.a


#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/geos-config

