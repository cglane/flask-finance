module.exports = {
  'outputName':'./files/output.csv',
  'user1':{
    'password':'1Testing!',
    'username':'charles'
  },
  'financesProfile':{
    'filePath':'./files/finances.csv',
    'source':'finances',
    'header':'infer',
    'columns':{
      'date':'Date',
      'location':'Description II',
      'value':['Amount Salary','Amount BankSC','13 Drews Ct.','Work Related/Other'],
      'description':'Description'
    }
  },
  'amexProfile':{
    'filePath':'./files/amex.csv',
    'source':'amex',
    'header':'None',
    'columns':{
      'date':'0',
      'value':'7',
      'location':'2',
      'description':''
    }
  }
}
