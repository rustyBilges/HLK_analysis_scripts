
# From Guy Nason : http://www.maths.bris.ac.uk/~guy/Research/LSTS/TOS.html

library('fractal')
library('astsa')
library('locits')
library(tseries)

data("eqexp")
dim(eqexp)
exP <- eqexp[1:1024, 14]
ts.plot(exP)

## PSR test
stationarity(exP)
## Nason wavelet test
ans <- hwtos2(exP)
ans
plot(ans)

### first loading all 3 series (hi,rw,ns) and cutting out transience so all are length 49001, then:
stationarity(hi)
stationarity(rw)
stationarity(ns)
kpss.test(hi)
kpss.test(rw)
kpss.test(ns)
adf.test(hi)
adf.test(rw)
adf.test(ns)

## now looking at increasing window lengths for stationarity (forwards and backwards):
wl = 1000
psr <- list()
adf_p <- list()
adf_s <- list()
kpss_p <- list()
kpss_s <- list()
for (t in seq(1000,49000,by=wl)){
    
    #hi_sb <- hi[(0):(t+wl+1)];
    
    hi_sb <- hi[(49001-t):49001];
    
    ans <- stationarity(hi_sb);
    pv <- attr(ans,"pvals");
    psr[[length(psr)+1]] = pv[[1]];
    
    ans <- adf.test(hi_sb);
    pv <- ans$p.value
    st <- ans$statistic
    adf_p[[length(adf_p)+1]] = pv[[1]];
    adf_s[[length(adf_s)+1]] = st[[1]];
    
    ans <- kpss.test(hi_sb);
    pv <- ans$p.value
    st <- ans$statistic
    kpss_p[[length(kpss_p)+1]] = pv[[1]];
    kpss_s[[length(kpss_s)+1]] = st[[1]];
}


########################################################################
dat = read.csv("output_pops_long.csv", header = FALSE)

biomass = rowSums(dat)
biomass_no_transience = biomass[1000:50000]
mean(biomass_no_transience)
sqrt(var(biomass_no_transience))

ts.plot(biomass[1000:50000])

td = biomass[33617:50000]
td = biomass[2000:5000]
stationarity(td)
ts.plot(td)
length(td)
ans <- hwtos2(td)
ans

plot(ans)

