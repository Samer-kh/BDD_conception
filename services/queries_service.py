from persistance.inter_tables import *

''' List all the publications registered in the library system (Do not show duplicates owned
    by different labs).'''
    
def execute_query_one():
    with engine.connect() as con:
        rows=[]
        query='SELECT DISTINCT * FROM publication'
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        print(keys)
        for row in rs:
            rows.append(row)
        print(rows)
        return (rows,keys)
    

'''For a given user, list all the publications issued to her/him and owned by any lab/ a
    particular lab'''

        
def execute_query_two(user_id,lab_id):
    if (lab_id==None) :
        with engine.connect() as con:
            rows=[]
            query='SELECT p.publication_id , year_publication , state FROM user_publication u , publication p where p.publication_id=u.publication_id and u.user_id={}'.format(user_id)
            keys=list(con.execute(query).keys())
            rs = con.execute(query)
            print(keys)
            for row in rs:
                rows.append(row)
            print(rows)
            return (rows,keys)
    else:
        with engine.connect() as con:
            rows=[]
            query="SELECT p.publication_id , year_publication , state FROM user_publication u , publication p , pub_lab_hascppy c where p.publication_id=u.publication_id and u.user_id= {} and c.lab_id = {}".format(user_id,lab_id)
            keys=list(con.execute(query).keys())
            rs = con.execute(query)
            print(keys)
            for row in rs:
                rows.append(row)
            print(rows)
            return (rows,keys)
        
''' Evaluate the price of all publications owned by a particular lab in €. (at the running rate
    of other currencies)'''    
     
def execute_query_three(lab_id):

    with engine.connect() as con:
        rows=[]
        query=''' SELECT ((select NVL(SUM(value),0) from cost c , regularbooks b , publication p where c.currancy='Dollar' and b.cost_id=c.cost_id and p.lab_id={} and p.publication_id=b.ISBN)
              + (select NVL(SUM(value*pound_to_dollar),0) from cost c, exchange e , regularbooks b , publication p where c.currancy='Pound' and b.cost_id=c.cost_id and p.lab_id={} and p.publication_id=b.ISBN and c.id_echange=e.exchange_id)
              + (select NVL(SUM(value*euro_to_dollar),0) from cost c, exchange e , regularbooks b , publication p where c.currancy='Euro' and b.cost_id=c.cost_id and p.lab_id={} and p.publication_id=b.ISBN and c.id_echange=e.exchange_id)
              + (select NVL(SUM(value),0) from cost c , periodics b , publication p where c.currancy='Dollar' and b.cost_id=c.cost_id and p.lab_id={} and p.publication_id=b.periodic_id)
              + (select NVL(SUM(value*euro_to_dollar),0) from cost c, exchange e , periodics b , publication p where c.currancy='Euro' and b.cost_id=c.cost_id and p.lab_id={} and p.publication_id=b.periodic_id and c.id_echange=e.exchange_id)
              + (select NVL(SUM(value*pound_to_dollar),0) from cost c, exchange e , periodics b , publication p where c.currancy='Pound' and b.cost_id=c.cost_id and p.lab_id={} and p.publication_id=b.periodic_id and c.id_echange=e.exchange_id)
              ) as total'''.format(lab_id,lab_id,lab_id,lab_id,lab_id,lab_id)
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        print(keys)
        for row in rs:
            rows.append(row)
        print(rows)
        return (rows,keys)
    
''' For a given user, evaluate whether (s)he can borrow a particular publication at a given
    time. (will depend on the availability status and the accessrights)'''  
     
def execute_query_four(user_id,pub_id):

    with engine.connect() as con:
        rows=[]
        query=" select user_id from user u, publication p where u.user_id= {} and p.state='On rack' and {} in ( select user_id from user_lab_auth a where a.lab_id=p.lab_id )".format(user_id,pub_id)
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        print(keys)
        for row in rs:
            rows.append(row)
        print(rows)
        return (rows,keys)
