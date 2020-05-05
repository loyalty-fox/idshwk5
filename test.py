from sklearn.ensemble import RandomForestClassifier
import numpy as np
domainlist = []
class Domain:
	
	def __init__(self,_name,_label,_length):
		self.name = _name
		self.label = _label
		self.length = _length
		
	def returnData(self):
		return processData(self.name)

	def returnLabel(self):
		if self.label == "notdga":
			return 0
		else:
			return 1
		
def processData(name):
	num=0;
	for i in name:
		if i.isdigit():
			num=num+1;
	return [len(name),num];

def TrainData(filename):
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line.startswith("#") or line =="":
				continue
			tokens = line.split(",")
			name = tokens[0]
			label = tokens[1]
			length = len(tokens[0])
			domainlist.append(Domain(name,label,length))
def main():
	TrainData("train.txt")
	featureMatrix = []
	labelList = []
	for item in domainlist:
		featureMatrix.append(item.returnData())
		labelList.append(item.returnLabel())
		
	clf = RandomForestClassifier(random_state=0)
	clf.fit(featureMatrix,labelList)
	
	f=open("test.txt",mode='r');
	foutput=open("result.txt",mode='w');
	for line in f:
		line = line.strip()
		if line.startswith("#") or line =="":
			continue
		tokens = line.split(",")
		name = tokens[0]
		result=clf.predict([processData(name)]);
		if(result ==0):
			foutput.write(name+","+"notdga\n")
		else:
			foutput.write(name+","+"dga\n")
	f.close();
	foutput.close();

if __name__ == '__main__':
	main()
