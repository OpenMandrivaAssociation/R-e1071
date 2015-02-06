%global packname  e1071
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.6.3
Release:          2
Summary:          Misc Functions of the Department of Statistics (e1071), TU Wien

Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/e1071_1.6-3.tar.gz
Requires:         R-class 
Requires:         R-graphics R-stats R-grDevices R-utils 
Requires:         R-cluster R-mlbench R-nnet R-randomForest R-rpart R-SparseM R-xtable R-Matrix R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-class
BuildRequires:    R-graphics R-stats R-grDevices R-utils 
BuildRequires:    R-cluster R-mlbench R-nnet R-randomForest R-rpart R-SparseM R-xtable R-Matrix R-MASS 

%description
Functions for latent class analysis, short time Fourier transform, fuzzy
clustering, support vector machines, shortest path computation, bagged
clustering, naive Bayes classifier, ...

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

