from Trainer import Trainer

classes = ['orange','potato','tomato']

def main():
    trainPaths = ['/home/temp/'+c+'/train/' for c in classes ]
    testPaths =  ['/home/temp/'+c+'/test/'   for c in classes ]

    trainer = Trainer(classes,trainPaths)
    trainer.train()
    tree = trainer.classifiers[1]
    
    imgs = ImageSet()
    for p in testPaths:
        imgs += ImageSet(p)
    random.shuffle(imgs)

    print "Result test"
    trainer.test(testPaths)

    trainer.visualizeResults(tree,imgs)

main()