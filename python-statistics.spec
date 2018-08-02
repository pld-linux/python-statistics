Summary:	Mathematical statistics functions
Summary(pl.UTF-8):	Matematyczne funkcje statystyczne
Name:		python-statistics
Version:	1.0.3.5
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/statistics/
Source0:	https://files.pythonhosted.org/packages/source/s/statistics/statistics-%{version}.tar.gz
# Source0-md5:	d6d97f3a1a7b3192cff99e0f2b5956c3
URL:		https://pypi.org/project/statistics/
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of Python 3.4 statistics module to Python 2.x.

%description -l pl.UTF-8
Port modułu statistics z Pythona 3.4 do Pythona 2.x.

%prep
%setup -q -n statistics-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/statistics
%{py_sitescriptdir}/statistics-%{version}-py*.egg-info
