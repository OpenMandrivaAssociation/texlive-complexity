Name:		texlive-complexity
Version:	0.76
Release:	1
Summary:	Computational complexity class names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/complexity
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Complexity is a LaTeX package that defines commands to typeset
Computational Complexity Classes such as $\P$ and $\NP$ (as
well as hundreds of others). It also offers several options
including which font classes are typeset in and how many are
defined (all of them or just the basic, most commonly used
ones). The package has no dependencies other than the standard
ifthen package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
