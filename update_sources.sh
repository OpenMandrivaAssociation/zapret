git clone https://github.com/bol-van/zapret.git
pushd zapret
git archive --format=tar --prefix zapret-$(date +%Y%m%d)/ HEAD | xz -vf > ../zapret-$(date +%Y%m%d).tar.xz

