Name: helloworld
Version: 1.0
Release: 1%{?dist}
License: GPLv3+
URL: https://helloworld.com/
Source0: helloworld-1.0.tar.gz

Requires(post): info
Requires(preun): info
%description
helloworld from rpm 
%global debug_package %{nil}
%prep

%setup

%build
make PREFIX=/usr %{?_smp_mflags}

%install
make PREFIX=/usr destdir=%{?buildroot} install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/helloworld
