%global tl_name complexity
%global tl_revision 45322

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.81a
Release:	%{tl_revision}.1
Summary:	Computational complexity class names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/complexity
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Complexity is a LaTeX package that defines commands to typeset
Computational Complexity Classes such as $\P$ and $\NP$ (as well as
hundreds of others). It also offers several options including which font
classes are typeset in and how many are defined (all of them or just the
basic, most commonly used ones). The package has no dependencies other
than the standard ifthen package.

