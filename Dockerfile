From arm32v7/debian:bullseye

RUN apt-get -y update 
RUN apt-get -y install software-properties-common
RUN apt-get install wget gnupg gnupg1 gnupg2 -y
RUN wget https://archive.raspbian.org/raspbian.public.key -O - | apt-key add -
RUN apt-add-repository 'deb http://raspbian.raspberrypi.org/raspbian/ bullseye main contrib non-free rpi firmware'
RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install python3-opencv -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-qrtools -y
RUN apt-get install libzbar0 libzbar-dev -y
RUN apt-get install git -h

RUN pip3 install zbarlight web3
RUN pip3 install ipykernel
RUN pip3 install autopep8
RUN pip3 install pylint
RUN pip3 install sshkeyboard

RUN apt-get autoremove -y

# ENV READTHEDOCS=True
# RUN pip3 install picamera

ENV LD_LIBRARY_PATH="/opt/vc/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
# ENV PATH="$PATH:/opt/vc/bin"
COPY . /
CMD ["python3"]