Summary:	Python wrapper for Pigment library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki Pigment
Name:		python-pigment
Version:	0.3.5
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://elisa.fluendo.com/static/download/pigment/pigment-python-%{version}.tar.gz
# Source0-md5:	63b1d174040f48b08a3ba9c76fa8c352
URL:		http://www.fluendo.com/elisa/
BuildRequires:	pigment-devel >= 0.3.7
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygobject-devel >= 2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	pigment >= 0.3.7
Requires:	python-pygobject >= 2.8.0
Obsoletes:	pigment-python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a wrapper that allows Pigment applications to be
written in Python.

%description -l pl.UTF-8
Ten moduł zawiera interfejs pozwalający na pisanie w Pythonie
aplikacji wykorzystujących bibliotekę Pigment.

%prep
%setup -q -n pigment-python-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	examplesdir=%{_examplesdir}/%{name}-%{version} \
	picturesdir=%{_examplesdir}/%{name}-%{version}/pictures

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la
%py_postclean $RPM_BUILD_ROOT%{_datadir}/pigment-python/2.0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE TODO
%attr(755,root,root) %{py_sitedir}/_pgmmodule.so
%attr(755,root,root) %{py_sitedir}/_pgmgtkmodule.so
%{py_sitescriptdir}/pgm
%{_datadir}/pigment-python
%{_examplesdir}/%{name}-%{version}
