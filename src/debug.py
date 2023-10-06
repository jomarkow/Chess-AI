import matplotlib.pyplot as plt
import cv2

def lines(img, lines, color=(0,0,255), size=2):
	"""draw lines"""
	for a, b in lines: cv2.line(img,tuple(a),tuple(b),color,size)
	return img

def points(img, points, color=(0,0,255), size=2):
	"""draw points"""
	for pt in points: cv2.circle(img,(int(pt[0]),int(pt[1])),size,color,-1)
	return img

def scatter(dataset, cmap = ''):
    plt.scatter(dataset[:, 0], dataset[:, 1], cmap=cmap)
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('K-Means Clustering')
    plt.show()
