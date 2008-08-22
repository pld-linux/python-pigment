Summary:	Python wrapper for Pigment library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki Pigment
Name:		python-pigment
Version:	0.3.5
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/pigment/pigment-python-%{version}.tar.gz
# Source0-md5:	63b1d174040f48b08a3ba9c76fa8c352
URL:		http://www.fluendo.com/elisa/
BuildRequires:	pigment-devel >= 0.3.5
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README RELEASE TODO ChangeLog
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitescriptdir}/pgm
%{_datadir}/pigment-python
