from Trainer import Trainer
from SimpleCV.ImageClass import Image, ImageSet, ColorSpace
import random

classes = ['orange','potato','tomato']

def main():
    trainPaths = ['/home/temp/'+c+'/train/' for c in classes ]
    testPaths =  ['/home/temp/'+c+'/test/'   for c in classes ]

    trainer = Trainer(classes,trainPaths)
    trainer.train()
    tree = trainer.classifiers[1]
    
    imgs = ImageSet()
    for p in testPaths:
        print "path"+p
        imgs += ImageSet(p)
    random.shuffle(imgs)

    print "Result test"
    trainer.test(testPaths)

    trainer.visualizeResults(tree,imgs)

main()