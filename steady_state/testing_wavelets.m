
dt = 1;

t = 0:dt:(numel(biomass)*dt)-dt;

f0 = 5/(2*pi);
NumVoices = 32;
a0 = 2^(1/NumVoices);

wavCenterFreq = 0.01;
minfreq = 0.001;%1000;
maxfreq = 10.0 ;71428.57;
minscale = wavCenterFreq/(maxfreq*dt);
maxscale = wavCenterFreq/(minfreq*dt);

%scales = a0.^(minscale:maxscale).*dt;

scales = {1, 0.01, fix(log2(5000)/0.01)};
cwtbat = cwtft({biomass,dt},'wavelet','morl','scales',scales);
imshow(cwtbat.cfs);
%helperCWTTimeFreqPlot(cwtbat.cfs,t.*1e6,cwtbat.frequencies./1000,...
%    'surf','Bat Echolocation (CWT)','Microseconds','kHz')


dt = 1/1000;
NumVoices = 32;
a0 = 2^(1/NumVoices);
wavCenterFreq = 5/(2*pi);
minfreq = 20;
maxfreq = 500;
minscale = wavCenterFreq/(maxfreq*dt);
maxscale = wavCenterFreq/(minfreq*dt);
minscale = floor(NumVoices*log2(minscale));
maxscale = ceil(NumVoices*log2(maxscale));
scales = a0.^(minscale:maxscale).*dt;
cwtquadchirp = cwtft({biomass,0.001},'wavelet','morl','scales',scales);
imshow(cwtbat.cfs);