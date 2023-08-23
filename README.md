
# Chess camera AI

Project dedicated to detect the positions of a chessboard with a mobile phone camera or webcam in real time.

![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

### Made with:

[![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-orange?style=for-the-badge&logo=Jupyter&logoColor=white)](https://jupyter.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-red?style=for-the-badge&logo=Opencv&logoColor=white)](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html)
![NumPy](https://img.shields.io/badge/numpy-black?style=for-the-badge&logo=numpy)


## Development detailed

I think, initially, this project could be solved being divided into three main parts or areas, this are grid recognition, pieces recognition and board visualization.

#### Grid recognition:

The code of this section can be found at `src/grid_recog.ipynb`

1. Take the image and convert to greyscale.
2. Convert the image to canny *__1__
3. Do a hough transform to detect chessboard borders *__2__
4. Delete the lines with less difference within others, for getting only four borders
5. Find intersections to get the four corners of the board
6. Create a black mask excluiding the quadrangle formed by the corners *__3__
7. Use `cv2.goodFeaturesToTrack()` to recognize all inner corners.

#### Grid recognition Issues:

1. The canny threshold has to be very precise and setted by the user, I think there's probably a better option for this
2. This needs to be done without pieces, before the game starts.
3. With this mask you can't move the board during the game

#### Images:



| Original image  | Canny | Hough lines | Board corners | Try of mask :b |
| --------------- |-------|-------------|---------------|----------------|
| ![b46f5b3c-ae09-49bd-936f-49f04a0f9758.jpg](https://i.postimg.cc/PfVQncpj/b46f5b3c-ae09-49bd-936f-49f04a0f9758.jpg)|![image.png](https://i.postimg.cc/tRzW9csT/image.png)|![image.png](https://i.postimg.cc/tCc4td1y/image.png)|![image.png](https://i.postimg.cc/wxyNKBh6/image.png)|![image.png](https://i.postimg.cc/brhpFLxS/image.png)|


#### Pieces recognition:
The pieces recognition still not in development, will actualize here when it does. Will be done with machine learning, so probably incluiding `scikit-learn` in future.

#### Board visualization:

The code of this section can be found at `src/board.py`

Creates the visualization with `Pygame` library and svg images of pieces. For moving pieces you call on `src/main.py` the function `board.move(move_notation)`
The `move_notation` parameter is a string type variable, Eg: "NG1-F3", who abbreviates from "Knight on G1 to F3"

Board positions is defined by a pandas dataframe:

           A  B  C  D  E  F  G  H
        8  r  n  b  q  k  b  n  r
        7  p  p  p  p  p  p  p  p
        6  .  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .  .
        2  P  P  P  P  P  P  P  P
        1  R  N  B  Q  K  B  N  R


 After "pD7-D5" and "NG1-F3":

![image.png](https://i.postimg.cc/vZW1GQLC/image.png)


30/7/23: Created brach "develop" Camera configured


## Workflow and Colaborate

This projet is being developed with a git Flow structure, for clean and organizated flow of work.
![gitflow-1.png](https://i.postimg.cc/YCt5Y6hC/gitflow-1.png)

You're invited to colaborate forking this repo and creating a pull request. Always with a detailed dsecription and clean code.

You can contact me at: jomarkow@gmail.com
