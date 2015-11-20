

## population file:
#pops <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/highIM/output_pops_long.csv", header=F)
pops <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/network_7_highIM/output_pops.csv", header=F)
l_pops <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/network_7_highIM/output_pops_long.csv", header=F)

biomass = rowSums(pops)
l_biomass = rowSums(l_pops)

par(mfrow=c(2,1))
plot(1:length(biomass), biomass, type="n")
lines(1:length(biomass), biomass)
plot(1:length(l_biomass), l_biomass, type="n")
lines(1:length(l_biomass), l_biomass)

## test stationarity:
library('fractal')
library('astsa')
library('locits')
library(tseries)

st = 1000
en = 50000
stationarity(l_biomass[st:en])
kpss.test(l_biomass[st:en])
adf.test(l_biomass[st:en])

mean(l_biomass[st:en])
sqrt(var((l_biomass[st:en])))

## species info file
sps <- read.csv("~/Documents/phd files/habitat_loss_project/python_analysis_scripts/steady_state/test_files/highIM/output_species_long.csv", header=F)

## for this simulation (vegetarian) the most abundant species are 20,6,59,46,47
##                                  the least abundant species are 58, 3, 2, 7, 45

## for network 7 example the most abundant species are 59, 30, 47
##                                  the least abundant species are 14, 16, 52

sp59 = pops$V59
sp30 = pops$V30
sp47 = pops$V47

sp14 = pops$V14
sp16 = pops$V16
sp52 = pops$V52


st = 9500
en = 10000
adf.test(sp59[st:en])
adf.test(sp30[st:en])
adf.test(sp47[st:en])

adf.test(sp14[st:en])
adf.test(sp16[st:en])
adf.test(sp52[st:en])