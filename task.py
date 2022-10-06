# Thiago Chim Silvera - 110668

# Importa opencv
import cv2

# Abre a imagem original e a versão hsv dela
img = cv2.imread('latas refri.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Cria uma mascara dentro de um range de cores da Sprite
mask = cv2.inRange(img_hsv, (100, 10, 10), (120, 255, 255))

# Acha os contornos na mascara que é providenciada
countours, hiera = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Organiza os contornos encontrados de maior para menor e recebe o maior de todos
conto = sorted(countours, key = cv2.contourArea, reverse=True)[0]

# Cria um retangulo em volta do contorno enviado
area = cv2.boundingRect(conto)

# Recebe as cordenadas do retangulo
x, y, z, h = area

# Desenha na imagem o retangulo nas coordenadas recebidas
cv2.rectangle(img, (x, y), (x+z, y+h), (255, 0, 0), 4)

# Abre a imagem e espera uma entrada para fecha-la
cv2.imshow("Saida", img)
cv2.waitKey(0)
cv2.destroyAllWindows()