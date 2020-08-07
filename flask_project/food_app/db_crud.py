

class DataManager():

    def __init__(self,db):
        self.db=db

    @staticmethod
    def add(db,model,**kwargs):
        instance= model(**kwargs)
        

    @staticmethod
    def delete(db,model):
        pass

    @staticmethod
    def update(db,model):
        pass

    @staticmethod
    def retrieve(model,**kwargs):
        return model.query.all()


