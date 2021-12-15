from skimage import io

root = "C:/Users/leyrisvan/Processamento-de-imagens/scikit-image-examples/img/models/"


def gorro():
    img = io.imread(root + 'gorro.png')
    return img


def boneco():
    img = io.imread(root + 'boneco.png')
    return img


def flamengo():
    img = io.imread(root + 'flamengo.png')
    return img


def noel():
    img = io.imread(root + 'noel.png')
    return img


def hiena():
    img = io.imread(root + 'hiena.png')
    return img

