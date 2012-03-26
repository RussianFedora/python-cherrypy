%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-cherrypy
Version:        3.1.2
Release:        2%{?dist}
Summary:        Pythonic, object-oriented web development framework
Group:          Development/Libraries
License:        BSD
URL:            http://www.cherrypy.org/

Source0:        http://download.cherrypy.org/cherrypy/%{version}/CherryPy-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python-setuptools
BuildRequires:  python-devel

%description
CherryPy allows developers to build web applications in much the same way 
they would build any other object-oriented Python program. This usually 
results in smaller source code developed in less time.

%prep
%setup -q -n CherryPy-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%doc cherrypy/tutorial
%{_bindir}/cherryd
%{python_sitelib}/*

%changelog
* Mon Mar 26 2012 Konstantin Kozlov <mackoel@gmail.com> - 3.1.2-2
- Corrected first line of spec, removed Packager and Vendor

* Mon Oct 25 2010 Fabian Arrotin <fabian.arrotin@arrfab.net> - 3.1.2 - 9200/arrfab
- Initial package
