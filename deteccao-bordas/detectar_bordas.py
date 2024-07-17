import cv2 # type: ignore # 
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

def detectar_bordas(imagem_path):
    # Leia a imagem
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    # Verifique se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro ao carregar a imagem.")
        return

    # Aplique o detector de bordas Canny
    bordas = cv2.Canny(imagem, 100, 200)

    # Mostre a imagem original e a imagem com bordas
    plt.subplot(121), plt.imshow(imagem, cmap='gray')
    plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(bordas, cmap='gray')
    plt.title('Bordas Detectadas'), plt.xticks([]), plt.yticks([])
    
    plt.show()

if __name__ == "__main__":
    imagem_path = 'copo.jpg'
    detectar_bordas(imagem_path)
