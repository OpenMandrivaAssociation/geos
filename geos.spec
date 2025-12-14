%define major 3
%define libname	%mklibname geos
%define major_c	1
%define libname_c %mklibname geos_c
%define devel_name	%mklibname %{name} -d

Summary: GEOS (Geometry Engine, Open Source) topology library
Name:  geos
Version:	3.14.1
Release:	1
License: LGPLv2+
Group:	Sciences/Geosciences
Url:	https://trac.osgeo.org/geos
Source0: https://download.osgeo.org/geos/%{name}-%{version}.tar.bz2  
Source100: geos.rpmlintrc
BuildRequires:	cmake >= 3.15

%description
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files
%doc util/geosop/README.md
%{_bindir}/geosop

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary: Libraries for GEOS
Group: Sciences/Geosciences
Provides: %{name} lib%{name}
Obsoletes: %{libname} < %{version}-%{release}

%description -n %{libname}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{libname}
%license COPYING
%{_libdir}/lib%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{libname_c}
Summary: Libraries for GEOS
Group: Sciences/Geosciences
Obsoletes: %{libname_c} < %{version}-%{release}

%description -n %{libname_c}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{libname_c}
%license COPYING
%{_libdir}/lib%{name}_c.so.%{major_c}*

#-----------------------------------------------------------------------------

%package -n %{devel_name}
Summary: Development Libraries for the GEOS topology library
Group: Sciences/Geosciences
Requires: %{libname} = %{version}
Requires: %{libname_c} = %{version}
Provides: %{name}-devel = %{version}
Provides: lib%{name}-devel = %{version}

%description -n %{devel_name}
The GEOS library provides topological operators and simple spatial constructs:
points, lines, polygons, and collections.

%files -n %{devel_name}
%doc README.md NEWS.md
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/GEOS
%{_libdir}/pkgconfig/*.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake
%make_build


%install
%make_install -C build
