pkgname=crossword
pkgver=0.3.1
pkgrel=1
arch=('x86_64')
pkgdesc="Generator,editor a crossword from words list and print a png results"
url="https://github.com/oditynet/crossword"
license=('GPL')
depends=('python3' 'python-pip' )
makedepends=('pkgconfig')
optdepends=('')
source=(https://github.com/oditynet/${pkgname}/archive/refs/tags/${pkgver}.tar.gz)
md5sums=('406a733e9907e712d97f0ff67a9b2ccb')

build() {
  pip3 install image
  pip3 install tk
}

package() {
  install -D -m755 "${srcdir}/crossword-${pkgver}/main.py" "${pkgdir}"/usr/bin/crossword.py
  echo "[Desktop Entry]\nType=Application\nName=jcrossword\nPath=/usr/bin\nExec=python3 crossword.py\nTerminal=false\n" > "${srcdir}/${pkgname}.desktop"
  install -D -m 644 "${srcdir}/${pkgname}.desktop" ${pkgdir}/usr/share/applications/${pkgname}.desktop
}

