%define	date	20181204
Summary:        transparent proxy 
Name:           zapret
Version:        %{date}
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:            https://github.com/bol-van/zapret
Source0:	https://github.com/bol-van/zapret/%{name}-%{date}.tar.xz
BuildRequires:	pkgconfig(libnetfilter_queue)
Requires:	ipset


%description
Avoid ROSKOMNADZOR blocks.

%prep
%autosetup

%build
%make_build -C nfq
%make_build -C tpws


%install
install -d %{buildroot}%{_bindir}
install -m0755 tpws/tpws %{buildroot}%{_bindir}/
install -m0755 nfq/nfqws %{buildroot}%{_bindir}/

%files
%{_bindir}/tpws
%{_bindir}/nfqws
