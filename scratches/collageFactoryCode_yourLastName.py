# JES version X.XX.XXX


#open 5 pics and fix the 5 pictures to fit the criteria
#pic1 100x100
#pic2 at most 300*300 at least 100*100
#pic3 at least 200*200
#pic4 at least 200*200
#pic5 at least 801*200 (wide*tall)

pic1 = makePicture(getMediaPath('1.jpg'))
pic2 = makePicture(getMediaPath('2.jpg'))
pic3 = makePicture(getMediaPath('3.jpg'))
pic4 = makePicture(getMediaPath('4.jpg'))
pic5 = makePicture(getMediaPath('5.jpg'))



# here is the function to resize a picture
def resize(pic,target_wide,target_tall):

    real_wide = getWidth(pic)
    real_tall = getHeight(pic)

    width_scale = int(real_wide/target_wide)
    tall_scale = int(real_tall/target_tall)
    new_pic = makeEmptyPicture(target_wide,target_tall)

    for y in range(0,target_tall,tall_scale):
        for x in range(0,target_wide,width_scale):
            color = getColor(getPixel(pic,x/width_scale,y/tall_scale))

            for newy in range(y,y+tall_scale):
                for newx in range(x,x+width_scale):
                    target_pixel = getPixel(new_pic,newx,newy)
                    setColor(new_pic,color)




    return new_pic

# resizing picture
pic1 = resize(pic1,100,100)
pic2 = resize(pic2,300,300)
pic3 = resize(pic3,200,200)
pic4 = resize(pic4,200,200)
pic5 = resize(pic5,801,200)


# Copy onto ,this fucntion get called later in collogeFactory function

def copyOnto(source, target, xOffset, yOffset):

    for sourcePixel in getPixels(source):

        xSource = getX(sourcePixel)

        ySource = getY(sourcePixel)

        xTarget = xSource + xOffset

        yTarget = ySource + yOffset

        targetPixel = getPixel(target, xTarget, yTarget)

        setColor(targetPixel, getColor(sourcePixel))


def collageFactory(pic1,pic2,pic3,pic4,pic5):
    #return canvas which is initially 800*800 empty picture
    canvas = makeEmptyPicture(800,800)

    copyOnto(pic1, canvas, 0,0)

    copyOnto(pic2, canvas, 165,0)

    copyOnto(pic3, canvas, 0,100)

    copyOnto(pic4, canvas, 165,100)

    copyOnto(pic5, canvas, 165,100)

    return canvas


# Unit testing start here

# copy yout test 1 function
def test1():
    pass

# copy yout test 2 function
def test2():
    pass


# copy yout test 3 function
def test3():
    pass

# copy yout test 4 function
def test4():
    pass


