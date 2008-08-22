Summary:	Pigment python files
Summary(pl.UTF-8):	Pytonowe pliki Pigmenta
Name:		pigment-python
Version:	0.3.5
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.gz
# Source0-md5:	63b1d174040f48b08a3ba9c76fa8c352
URL:		http://www.fluendo.com/elisa/
BuildRequires:	pigment-devel >= 0.3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a wrapper that allows Pigment applications to be
written in Python.

%description -l pl.UTF-8
This module contains a wrapper that allows Pigment applications to be
written in Python.

%prep
%setup -q

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
%{py_sitedir}/*.so
%{py_sitescriptdir}/pgm
%{_datadir}/%{name}
