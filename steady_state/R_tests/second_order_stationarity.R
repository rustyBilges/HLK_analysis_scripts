
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

