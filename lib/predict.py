from readCsv  import readCSV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
import numpy as np
from sklearn import svm
from scipy.sparse import coo_matrix, hstack
import csv
# financesPath = './csvFiles/finances.csv'
# headers = {'location':'Description II','value':['Amount Salary','Amount BankSC','13 Drews Ct.','Work Related/Other'],'description':'Description'}


"Initialize svm and create bag of words features from finances file"
def trainSVM(financesPath,headers):
    data_dict = readCSV(financesPath).valuesLocationsDescriptions(headers)
    clf,vectorizer = train_data(data_dict)

def writeToCSV(outputName,transactions):
    with open(outputName , "wb") as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for item in transactions:
            #Write item to outcsv
            writer.writerow([item[0], item[1],'','','', item[2],item[3]])
"Write for API clients"
def writeToCSVPublic(outputName,transactions):
    with open(outputName,'wb')as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Date','Value','Location','Description'])
        for item in transactions:
            #Write item to outcsv
            writer.writerow([item[0], item[1],item[2],item[3]])
"Adds value parameter to bag of words array"
def training_feature(vectorizer,location,value):
    location_matrix = vectorizer.transform([location])
    value_matrix = coo_matrix([value])
    return hstack([location_matrix,value_matrix]).toarray()
"Training svm with financial spreadsheet using bag of words and value"
def train_data(data_dict):
    vectorizer = CountVectorizer()
    vectorizerArray = vectorizer.fit(data_dict['locations'])

    locations_matrix = vectorizer.fit_transform(data_dict['locations'])
    values_matrix = coo_matrix(data_dict['values'])
    ###Add values to locations matrix, create array
    features = hstack([locations_matrix,values_matrix]).toarray()
    labels = data_dict['descriptions']

    clf = svm.LinearSVC(random_state=0)
    clf.fit(features, labels)
    return clf,vectorizer

"Use svm to predict description and write new csv file for all transactions"
def predictDescription(input_list,clf,vectorizer,outputName = './files/output.csv',header = None, source = 'Amex', ignoreLocations = ['ONLINE PAYMENT ']):
    print 'Predict Description'
    transactions = []
    for item in input_list:
        predict_array = training_feature(vectorizer,(item['location'].split('-')[0]),(item['value']))
        transactions.append((item['date'],item['value'],item['location'],clf.predict(predict_array)[0]))
    writeToCSVPublic(outputName,transactions=transactions)
    return outputName
def testPredict(filePath,headers):
        data_dict = readCSV('./files/finances.csv').valuesLocationsDescriptions(headers)
        clf,vectorizer = train_data(data_dict)
        predict_array = training_feature(vectorizer,'Exxon',-23.2)
        prediction = clf.predict(predict_array)[0]
        return prediction
def makePredictions(finances,creditCard,outputName):
    print 'Read Finances'
    data_dict=readCSV(finances.filePath,header=finances.header,source=finances.source).valuesLocationsDescriptions(finances.columns)
    print 'Train Data'
    clf,vectorizer = train_data(data_dict)
    print 'Read Credit Card'
    input_list = readCSV(creditCard.filePath,source=creditCard.source).dateValueLocation(creditCard.columns)
    print input_list
    print 'Make Predictions'
    outputName = predictDescription(input_list,
                                    clf ,
                                    vectorizer,
                                    outputName = outputName)
    return outputName

def readFinances(f):
    try:
        data_dict=readCSV(f.filePath,header=f.header,source=f.source).valuesLocationsDescriptions(f.columns)
        return 'Success'
    except Exception as e:
        print e
        return 'Failure'

def readCreditCard(f):
    try:
        data_dict = readCSV(f.filePath,source=f.source).dateValueLocation(f.columns)
        return 'Success'
    except Exception as e:
        print e
        return 'Failure'
