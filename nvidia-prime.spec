Name:		nvidia-prime
Version:	1.0.0
Release:	1
#Source0:	self-fulfilling package
Summary:	NVIDIA Prime Render Offload utilities
URL:		https://gitlab.archlinux.org/archlinux/packaging/packages/nvidia-prime
License:	GPL
Group:		System/Utilities
BuildArch: noarch

Requires:	nvidia
Suggests:	envycontrol

%description
NVIDIA Prime Render Offload utilities.

%prep

cat <<EOF >>prime-run
#!/bin/bash
# Created on $(date)
__NV_PRIME_RENDER_OFFLOAD=1 __VK_LAYER_NV_optimus=NVIDIA_only __GLX_VENDOR_LIBRARY_NAME=nvidia "\$@"

EOF

%install
install -Dm755 prime-run %{buildroot}%{_bindir}/prime-run

%files
%{_bindir}/prime-run
