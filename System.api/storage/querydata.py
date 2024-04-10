from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func

from sqlalchemy import String, cast,Integer ,Date ,Float
from sqlalchemy.orm import Session

from datetime import date, datetime, timedelta
from models import properties_models

#====================================================#
#                login queries                       #
#====================================================#

def check_user(db:Session,username):
    return db.query(properties_models.User).filter(properties_models.User.username == username).first()


def check_user_pass(db:Session,username,password):
    return db.query(properties_models.User).filter(properties_models.User.username == username,properties_models.User.password == password).first()

def update_times(db:Session,times,username,now_time):
    print("times",times,now_time)
    
    update = db.query(properties_models.User).filter(properties_models.User.username == username).update({'times':times,'block_date_time':now_time})
    db.commit()
    return update

def update_only_times(db:Session,username,blocked_time):
    update = db.query(properties_models.User).filter(properties_models.User.username == username).update({'block_date_time':blocked_time})
    db.commit()
    return update

def update_times_after(db:Session,username):
    update = db.query(properties_models.User).filter(properties_models.User.username == username).update({'times':'3'})
    db.commit()
    return update

def update_block(db:Session,username):
    update = db.query(properties_models.User).filter(properties_models.User.username == username).update({'block':'block'})
    db.commit()
    return update



#====================================================#
#                All Works queries                   #
#====================================================#

def get_all_works(db:Session,person):
    if person==None:
        return db.query(properties_models.AllWorks).filter(properties_models.AllWorks.active==True).all()
    else:
        return db.query(properties_models.AllWorks).filter(properties_models.AllWorks.assigned_person == person,properties_models.AllWorks.active==True).all()
    
    
def post_work(db:Session,data):
    datas = properties_models.AllWorks(**data)
    db.add(datas)
    db.commit()
    db.refresh(datas) 
    return  datas


def put_work(db:Session,bid,data):
    db.query(properties_models.AllWorks).filter_by(id=bid).update(data)
    db.commit()
    return db 
    
def delete_work(db:Session,bid,person,active):
    if active==None:
        db.query(properties_models.AllWorks).filter_by(id=bid).update({"delete_by_user":person,"active":False})
    else:
        db.query(properties_models.AllWorks).filter_by(id=bid).update({"delete_by_user":person,"active":True})
            
    db.commit()
    return db    
         
    
    
        
