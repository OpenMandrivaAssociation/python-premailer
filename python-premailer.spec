Name:		python-premailer
Version:	3.10.0
Release:	2
Summary:	Turns CSS blocks into style attributes
License:	Python-2.0
Group:		Development/Python
URL:		https://pypi.org/project/premailer/
Source0:	premailer-3.10.0.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(cssselect)
BuildRequires:	python%{pyver}dist(cssutils)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(cachetools)
BuildArch:	noarch
%description
Turns CSS blocks into style attributes.

%files
%{py_sitedir}/*
