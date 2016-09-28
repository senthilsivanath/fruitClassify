
from flask import Flask, request
import base64
from SimpleCV.ImageClass import Image, ImageSet, ColorSpace
from Trainer import Trainer
classes = ['orange','potato','tomato']
trainPaths = ['/home/temp/'+c+'/train/' for c in classes ]
testPaths = ['/home/temp/test' for c in classes ]
app = Flask(__name__)
trainer = Trainer(classes,trainPaths)
trainer.train()
tree = trainer.classifiers[1]
    
@app.route('/classify',methods = ['POST'])
def hello_world():
   data = request.form['image']
   g = open("test/flask.jpg", "w")
   g.write(base64.decodestring(data))
   g.close()   
   imgs = ImageSet()
   for p in testPaths:
        print "path"+p
        imgs += ImageSet(p)
   className = trainer.classifyName(tree,imgs)
   return className

if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0')
