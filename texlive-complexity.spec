# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/complexity
# catalog-date 2007-02-03 21:01:24 +0100
# catalog-license lppl
# catalog-version 0.76
Name:		texlive-complexity
Version:	0.76
Release:	7
Summary:	Computational complexity class names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/complexity
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/complexity.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.76-2
+ Revision: 750413
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.76-1
+ Revision: 718111
- texlive-complexity
- texlive-complexity
- texlive-complexity
- texlive-complexity

