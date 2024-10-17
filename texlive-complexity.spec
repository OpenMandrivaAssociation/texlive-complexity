Name:		texlive-complexity
Version:	45322
Release:	2
Summary:	Computational complexity class names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/complexity
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Complexity is a LaTeX package that defines commands to typeset
Computational Complexity Classes such as $\P$ and $\NP$ (as
well as hundreds of others). It also offers several options
including which font classes are typeset in and how many are
defined (all of them or just the basic, most commonly used
ones). The package has no dependencies other than the standard
ifthen package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/complexity/complexity.sty
%{_texmfdistdir}/tex/latex/complexity/mycomplexity.sty
%doc %{_texmfdistdir}/doc/latex/complexity/README
%doc %{_texmfdistdir}/doc/latex/complexity/complexity.pdf
%doc %{_texmfdistdir}/doc/latex/complexity/complexity.tex
%doc %{_texmfdistdir}/doc/latex/complexity/tableofclasses.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
