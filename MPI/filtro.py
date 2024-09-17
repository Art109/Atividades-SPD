import cv2
import numpy as np
from mpi4py import MPI
import time 


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

localImage = None
newImage = None
image = None
n = 0
largura = 0


if rank == 0:
    image = cv2.imread("maspcomruido.jpg",0)
    if image is None:
        print("Error: Image not loaded correctly.")
    else:
        print(f"Loaded image shape: {image.shape}")
    altura , largura = image.shape
    n = int(altura/size)
    newImage = np.zeros((altura, largura), dtype = 'uint8')
    print(f"Initialized newImage with shape: {newImage.shape}")


(n, largura) = comm.bcast((n,largura), root=0)
localImage = np.zeros((n, largura), dtype = 'uint8')

comm.Scatterv(image, localImage, root = 0)
print(f"Rank {rank}: Received localImage with shape: {localImage.shape}")



#Filtro media 3x3
def filtro(imagem):
    return cv2.blur(imagem,(3,3))

localImage = filtro(localImage)
print(f"Rank {rank}: Filtered localImage")

comm.Gatherv(localImage, newImage, root = 0 )

if(rank == 0):
    if newImage is None or newImage.size == 0:
        print("Error: Filtered image not gathered correctly.")
    else:
        cv2.imshow("original image", image)
        cv2.imshow("filtered image", newImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()