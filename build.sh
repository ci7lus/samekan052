set -eu

amazon-linux-extras install docker
systemctl start docker
docker run --rm alpine echo hoge
CURRENT_DIR=`pwd`
# mecab
yum clean metadata
yum -y update
yum makecache fast
rpm -ivh https://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-14.noarch.rpm
yum -y -q install yum-utils swig
rpm -ivh --quiet https://packages.groonga.org/centos/groonga-release-1.5.2-1.noarch.rpm
yum makecache
yum -y -q install mecab mecab-ipadic mecab-devel make curl xz patch file
# neologd
cd /usr/local/src/
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
./bin/install-mecab-ipadic-neologd -n -y
# model生成
cd $CURRENT_DIR
mkdir -p dist # @vercel/static-buildはdist/publicを成果物フォルダとして認識する
pip3 install -r requirements.txt
python3 testMecab.py
python3 fetchTweets.py
python3 generateModel.py