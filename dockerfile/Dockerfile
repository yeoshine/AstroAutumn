FROM daocloud.io/centos:7

RUN yum groupinstall -y "Development tools" && \
    yum install -y zlib zlib-devel openssl openssl-devel bzip2 bzip2-devel tkinter tk tcl wget

COPY src/* /tmp/

COPY requirements.txt /tmp/

RUN cd /tmp && \
    tar xvf Python-3.6.0.tar && \
    cd Python-3.6.0 && \
    ./configure && \
    make -j4 && make -j4 install

RUN rm -f /usr/bin/python && \
    ln -s /usr/local/bin/python3.6 /usr/bin/python && \
    sed -i 's/python/python2/g' /usr/bin/yum && \
    sed -i 's/python/python2/g' /usr/libexec/urlgrabber-ext-down && \
    ln -s /usr/local/bin/pip3.6 /usr/bin/pip

RUN pip install -r /tmp/requirements.txt

RUN cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime