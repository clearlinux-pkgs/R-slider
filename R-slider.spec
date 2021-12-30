#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-slider
Version  : 0.2.2
Release  : 13
URL      : https://cran.r-project.org/src/contrib/slider_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/slider_0.2.2.tar.gz
Summary  : Sliding Window Functions
Group    : Development/Tools
License  : MIT
Requires: R-slider-lib = %{version}-%{release}
Requires: R-dplyr
Requires: R-ellipsis
Requires: R-glue
Requires: R-lubridate
Requires: R-rlang
Requires: R-vctrs
Requires: R-warp
BuildRequires : R-dplyr
BuildRequires : R-ellipsis
BuildRequires : R-glue
BuildRequires : R-lubridate
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : R-warp
BuildRequires : buildreq-R

%description
type. Cumulative and expanding windows are also supported. For more
    advanced usage, an index can be used as a secondary vector that
    defines how sliding windows are to be created.

%package lib
Summary: lib components for the R-slider package.
Group: Libraries

%description lib
lib components for the R-slider package.


%prep
%setup -q -c -n slider
cd %{_builddir}/slider

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625590327

%install
export SOURCE_DATE_EPOCH=1625590327
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library slider
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library slider
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library slider
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc slider || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/slider/DESCRIPTION
/usr/lib64/R/library/slider/INDEX
/usr/lib64/R/library/slider/LICENSE
/usr/lib64/R/library/slider/Meta/Rd.rds
/usr/lib64/R/library/slider/Meta/features.rds
/usr/lib64/R/library/slider/Meta/hsearch.rds
/usr/lib64/R/library/slider/Meta/links.rds
/usr/lib64/R/library/slider/Meta/nsInfo.rds
/usr/lib64/R/library/slider/Meta/package.rds
/usr/lib64/R/library/slider/Meta/vignette.rds
/usr/lib64/R/library/slider/NAMESPACE
/usr/lib64/R/library/slider/NEWS.md
/usr/lib64/R/library/slider/R/slider
/usr/lib64/R/library/slider/R/slider.rdb
/usr/lib64/R/library/slider/R/slider.rdx
/usr/lib64/R/library/slider/doc/index.html
/usr/lib64/R/library/slider/doc/rowwise.R
/usr/lib64/R/library/slider/doc/rowwise.Rmd
/usr/lib64/R/library/slider/doc/rowwise.html
/usr/lib64/R/library/slider/doc/slider.R
/usr/lib64/R/library/slider/doc/slider.Rmd
/usr/lib64/R/library/slider/doc/slider.html
/usr/lib64/R/library/slider/doc/tsibble.R
/usr/lib64/R/library/slider/doc/tsibble.Rmd
/usr/lib64/R/library/slider/doc/tsibble.html
/usr/lib64/R/library/slider/help/AnIndex
/usr/lib64/R/library/slider/help/aliases.rds
/usr/lib64/R/library/slider/help/paths.rds
/usr/lib64/R/library/slider/help/slider.rdb
/usr/lib64/R/library/slider/help/slider.rdx
/usr/lib64/R/library/slider/html/00Index.html
/usr/lib64/R/library/slider/html/R.css
/usr/lib64/R/library/slider/tests/testthat.R
/usr/lib64/R/library/slider/tests/testthat/_snaps/slide-index.md
/usr/lib64/R/library/slider/tests/testthat/helper-date.R
/usr/lib64/R/library/slider/tests/testthat/helper-long-double.R
/usr/lib64/R/library/slider/tests/testthat/helper-s3.R
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-endpoints-cannot-be-na-1.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-endpoints-must-be-ascending-1.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-generated-endpoints-cannot-be-na-1.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-index-cannot-be-na-1.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-index-cannot-be-na-2.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-index-incompatible-size-1.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-index-incompatible-type-1.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-index-incompatible-type-2.txt
/usr/lib64/R/library/slider/tests/testthat/output/test-stop-index-must-be-ascending-1.txt
/usr/lib64/R/library/slider/tests/testthat/test-block.R
/usr/lib64/R/library/slider/tests/testthat/test-conditions.R
/usr/lib64/R/library/slider/tests/testthat/test-hop-index-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-hop-index.R
/usr/lib64/R/library/slider/tests/testthat/test-hop-index2-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-hop-index2.R
/usr/lib64/R/library/slider/tests/testthat/test-hop-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-hop.R
/usr/lib64/R/library/slider/tests/testthat/test-hop2-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-hop2.R
/usr/lib64/R/library/slider/tests/testthat/test-phop-index-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-phop-index.R
/usr/lib64/R/library/slider/tests/testthat/test-phop-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-phop.R
/usr/lib64/R/library/slider/tests/testthat/test-pslide-index-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-pslide-index.R
/usr/lib64/R/library/slider/tests/testthat/test-pslide-period-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-pslide-period.R
/usr/lib64/R/library/slider/tests/testthat/test-pslide-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-pslide.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-index-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-index.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-index2-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-index2.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-period-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-period.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-period2-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-period2.R
/usr/lib64/R/library/slider/tests/testthat/test-slide-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-slide.R
/usr/lib64/R/library/slider/tests/testthat/test-slide2-vec.R
/usr/lib64/R/library/slider/tests/testthat/test-slide2.R
/usr/lib64/R/library/slider/tests/testthat/test-summary-index.R
/usr/lib64/R/library/slider/tests/testthat/test-summary-slide.R
/usr/lib64/R/library/slider/tests/testthat/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/slider/libs/slider.so
/usr/lib64/R/library/slider/libs/slider.so.avx2
/usr/lib64/R/library/slider/libs/slider.so.avx512
