from mongoengine import *
import datetime
    # headers = {'date':'Date','location':'Description II','value':['Amount Salary','Amount BankSC','13 Drews Ct.','Work Related/Other'],'description':'Description'}


class Columns(EmbeddedDocument):
    date = StringField(max_length=200, required=True)
    location = StringField(max_length=200, required=True)
    value = ListField(StringField(max_length=50))
    description = StringField(max_length=200, required=True)

class FileProfile(EmbeddedDocument):
    filePath = StringField(max_length=200, required=True)
    source = StringField(max_length=200, required=True)
    header = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)
    columns = EmbeddedDocumentField(Columns)

class User(Document):
    username = StringField(max_length=200, required=True)
    password = StringField(max_length=200, required=True)
    finances = EmbeddedDocumentField(FileProfile)
    amex = EmbeddedDocumentField(FileProfile)
