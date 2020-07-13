#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE02B14E5030A2708 (security@celeryproject.org)
#
Name     : case
Version  : 1.5.3
Release  : 22
URL      : https://files.pythonhosted.org/packages/31/5a/9f1040ffb91e62c7ed6068dab6da5e1cb9ca3642d9b63c2254c3393af483/case-1.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/5a/9f1040ffb91e62c7ed6068dab6da5e1cb9ca3642d9b63c2254c3393af483/case-1.5.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/31/5a/9f1040ffb91e62c7ed6068dab6da5e1cb9ca3642d9b63c2254c3393af483/case-1.5.3.tar.gz.asc
Summary  : Python unittest Utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: case-license = %{version}-%{release}
Requires: case-python = %{version}-%{release}
Requires: case-python3 = %{version}-%{release}
Requires: nose
Requires: python-mock
Requires: setuptools
Requires: six
Requires: unittest2
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : nose
BuildRequires : python-mock
BuildRequires : setuptools
BuildRequires : six
BuildRequires : unittest2
BuildRequires : unittest2-python

%description
=====================================================================
 Python unittest utilities
=====================================================================

|build-status| |coverage| |license| |wheel| |pyversion| |pyimp|

:Version: 1.5.3
:Web: http://case.readthedocs.org/
:Download: http://pypi.python.org/pypi/case/
:Source: http://github.com/celery/case/
:Keywords: testing utilities, python, unittest, mock

About
=====

.. _case-installation:

Installation
============

You can install case either via the Python Package Index (PyPI)
or from source.

To install using `pip`,::

    $ pip install -U case

To install using `easy_install`,::

    $ easy_install -U case

.. _case-installing-from-source:

Downloading and installing from source
--------------------------------------

Download the latest version of case from
http://pypi.python.org/pypi/case/

You can install it by doing the following,::

    $ tar xvfz case-0.0.0.tar.gz
    $ cd case-0.0.0
    $ python setup.py build
    # python setup.py install

The last command must be executed as a privileged user if
you are not currently using a virtualenv.

.. _case-installing-from-git:

Using the development version
-----------------------------

With pip
~~~~~~~~

You can install the latest snapshot of case using the following
pip command::

    $ pip install https://github.com/celery/case/zipball/master#egg=case

.. |build-status| image:: https://secure.travis-ci.org/celery/case.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/celery/case

.. |coverage| image:: https://codecov.io/github/celery/case/coverage.svg?branch=master
    :target: https://codecov.io/github/celery/case?branch=master

.. |license| image:: https://img.shields.io/pypi/l/case.svg
    :alt: BSD License
    :target: https://opensource.org/licenses/BSD-3-Clause

.. |wheel| image:: https://img.shields.io/pypi/wheel/case.svg
    :alt: Case can be installed via wheel
    :target: http://pypi.python.org/pypi/case/

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/case.svg
    :alt: Supported Python versions.
    :target: http://pypi.python.org/pypi/case/

.. |pyimp| image:: https://img.shields.io/pypi/implementation/case.svg
    :alt: Support Python implementations.
    :target: http://pypi.python.org/pypi/case/

%package license
Summary: license components for the case package.
Group: Default

%description license
license components for the case package.


%package python
Summary: python components for the case package.
Group: Default
Requires: case-python3 = %{version}-%{release}

%description python
python components for the case package.


%package python3
Summary: python3 components for the case package.
Group: Default
Requires: python3-core
Provides: pypi(case)

%description python3
python3 components for the case package.


%prep
%setup -q -n case-1.5.3
cd %{_builddir}/case-1.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582903725
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/case
cp %{_builddir}/case-1.5.3/LICENSE %{buildroot}/usr/share/package-licenses/case/ddd4bd958c52e8beea1fb6184e6a327b6ea42e3b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/case/ddd4bd958c52e8beea1fb6184e6a327b6ea42e3b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
