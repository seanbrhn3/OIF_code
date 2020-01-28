FROM ubuntu:latest
RUN apt-get update -y && \
 apt-get install python3-pip -y && \
 apt-get install git -y && \
git clone https://github.com/madronac/openc2-yuuki && \
pip3 install ./openc2-yuuki
CMD ["python3", "-m", "yuuki.actuator"]
