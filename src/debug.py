import matplotlib.pyplot as plt
import cv2

def lines(img, lines, color=(0,0,255), size=2):
	"""draw lines"""
	for a, b in lines: cv2.line(img,tuple(a),tuple(b),color,size)
	return img

def points(img, points, color=(0,0,255), size=2):
    
    i=0

    for pt in points:
        cv2.circle(img,(int(pt[0]),int(pt[1])),size,color,-1)     
        cv2.putText(img, str(i), (int(pt[0]) + 10, int(pt[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        i = i + 1
    return img

def show(images):
    
    for title, image in images: 
        cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def scatter(dataset, labels = None, cmap = 'viridis'):
    plt.scatter(dataset[:, 0], dataset[:, 1], c = labels, cmap=cmap)
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('K-Means Clustering')
    plt.show()
