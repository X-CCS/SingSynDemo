FROM ubuntu
RUN apt update && apt install ibx11-dev:i386 \
    ibc6-dev:i386 libx11-dev:i386 \
     libx11-dev g++-multilib osspd \
      git csh libx11-dev cmake gcc\
       g++ automake openssh-service
ADD ./hts_engine_API /
ADD ./HTS_for_HTK /
ADD ./SPTK /
ADD ./HTS-demo_NIT-SONG070-F001 /
RUN cd /hts_engine_API && ./configure && make && make install
RUN cd /SPTK && ./configure && make && make install
RUN cd  /HTS_for_HTK/htk  && patch -p1 -d . < HTS-2.3_for_HTK-3.4.1.patch &&  ./configure &&  make
WORKDIR /HTS-demo_NIT-SONG070-F001

