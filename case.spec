#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : case
Version  : 1.5.2
Release  : 6
URL      : http://pypi.debian.net/case/case-1.5.2.tar.gz
Source0  : http://pypi.debian.net/case/case-1.5.2.tar.gz
Summary  : Python unittest Utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: case-python
BuildRequires : coverage-python
BuildRequires : linecache2-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : unittest2-python

%description
=====================================================================
Python unittest utilities
=====================================================================

%package python
Summary: python components for the case package.
Group: Default
Requires: nose-python
Requires: six-python
Requires: unittest2-python

%description python
python components for the case package.


%prep
%setup -q -n case-1.5.2

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
