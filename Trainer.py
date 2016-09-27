from SimpleCV.Features import HueHistogramFeatureExtractor, EdgeHistogramFeatureExtractor, HaarLikeFeatureExtractor
from SimpleCV.MachineLearning import SVMClassifier, TreeClassifier, NaiveBayesClassifier, KNNClassifier

class Trainer():

    def __init__(self,classes, trainPaths):
        self.classes = classes
        self.trainPaths = trainPaths


    def getExtractors(self):
        hhfe = HueHistogramFeatureExtractor(10)
        ehfe = EdgeHistogramFeatureExtractor(10)
        haarfe = HaarLikeFeatureExtractor(fname='/SimpleCV-master/SimpleCV/Features/haar.txt')
        return [hhfe,ehfe,haarfe]

    def getClassifiers(self,extractors):
       
        svm = SVMClassifier([HueHistogramFeatureExtractor()])
        tree = TreeClassifier(extractors)
        bayes = NaiveBayesClassifier(extractors)
        knn = KNNClassifier(extractors)
        return [svm,tree,bayes,knn]

    def train(self):
        self.classifiers = self.getClassifiers(self.getExtractors())
        print "after getting classifiers"+str(len(self.classifiers))
        for classifier in self.classifiers:
            print self.classes
            classifier.train(self.trainPaths,self.classes,verbose=True)

    def test(self,testPaths):
       
        for classifier in self.classifiers:
            print classifier.test(testPaths,self.classes,verbose=True)

    def visualizeResults(self,classifier,imgs):
        for img in imgs:
            className = classifier.classify(img)
            img.drawText(className,10,10,fontsize=60,color=Color.BLUE)         
        #imgs.save('test.jpg')