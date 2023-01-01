from persistance.inter_tables import *

''' List all the publications registered in the library system (Do not show duplicates owned
    by different labs).'''
    
def execute_query_one():
    with engine.connect() as con:
        rows=[]
        query='SELECT DISTINCT * FROM publication'
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        for row in rs:
            rows.append(row)
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
            for row in rs:
                rows.append(row)
            return (rows,keys)
    else:
        with engine.connect() as con:
            rows=[]
            query="SELECT p.publication_id , year_publication , state FROM user_publication u , publication p , pub_lab_hascppy c where p.publication_id=u.publication_id and u.user_id= {} and c.lab_id = {}".format(user_id,lab_id)
            keys=list(con.execute(query).keys())
            rs = con.execute(query)
            for row in rs:
                rows.append(row)
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
        for row in rs:
            rows.append(row)
        return (rows,keys)
    
''' For a given user, evaluate whether (s)he can borrow a particular publication at a given
    time. (will depend on the availability status and the accessrights)'''  
     
def execute_query_four(user_id,pub_id):

    with engine.connect() as con:
        rows=[]
        query='''SELECT 
    CASE WHEN EXISTS  
    (( SELECT * from user u , publication p , user_lab_auth l WHERE
    u.user_id=l.user_id and p.lab_id=l.lab_id and p.state='On Rack' and u.user_id='{}'
    and p.publication_id='{}' ) UNION (select * from user u , publication p , user_lab_auth l ,lab b, pub_lab_hascppy c 
    where u.user_id=l.user_id and b.lab_id=c.lab_id and p.publication_id=c.publication_id and p.state='On Rack' 
    and u.user_id='{}' and p.publication_id='{}'  )   ) THEN 'TRUE'
    ELSE 'FALSE'
END'''.format(user_id,pub_id,user_id,pub_id)
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        keys=["Exists"]
        for row in rs:
            rows.append(row)
        return (rows,keys)
 
''' If there is a publication such that a particular user has rights to borrow it (a copy), but it
is (all copies for which the user has rights are) issued to some one else then show the
email address(es) of all those users who presently have a borrowed copy of the
publication that this user has also right to borrow.'''    

def execute_query_five(user_id,pub_id):

    with engine.connect() as con:
        rows=[]
        query=''' '''
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        keys=["Exists"]
        for row in rs:
            rows.append(row)
        return (rows,keys) 
 
    
'''  List all publication belonging to a particular category, and costing less than a particular
     amount.'''
def execute_query_six(id_cat,amount):

    with engine.connect() as con:
        rows=[]
        query='''select * from regularbooks b , categories c , cost o , regular_books_category e where b.ISBN=e.ISBN and 
        e.Category_id=c.Category_id and b.cost_id=o.cost_id and o.value < {} and c.Category_id = {}
        '''.format(amount,id_cat)
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        for row in rs:
            rows.append(row)
        return (rows,keys)
    
'''  List all publications authored by a particular author, and published after a particular year'''

def execute_query_seven(year,id_auth):

    with engine.connect() as con:
        rows=[]
        query=''' (select p.publication_id as ID from regularbooks b , publication p , author a , regular_books_author r where r.ISBN=b.ISBN and a.author_id = r.author_id
        and p.publication_id=b.ISBN and a.author_id = {} and p.year_publication > DATE '{}')
        UNION (select publication_id  from ecl_thesis t ,internal_reports e, publication p where 
        p.publication_id=e.report_id and e.report_id=t.Id_thesis  and t.Author_id = '{}' and p.year_publication > DATE '{}')
        UNION (select publication_id  from scientific_reports t ,internal_reports e, publication p , scientific_author s ,author a where 
        p.publication_id=e.report_id and e.report_id=t.Id_Report and 
        s.Id_Report=t.Id_Report and a.author_id=s.author_id and
        a.Author_id = '{}' and p.year_publication > DATE '{}')
        '''.format(id_auth,year,id_auth,year,id_auth,year)
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        for row in rs:
            rows.append(row)
        return (rows,keys)

def execute_query_eight(pub):

    with engine.connect() as con:
        rows=[]
        query=''' select * from regularbooks b , publication p  where p.publication_id=b.ISBN  and b.publisher='{}' 
        order by p.year_publication
        '''.format(pub)
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        for row in rs:
            rows.append(row)
        return (rows,keys)
    
''' List all lost regular books (title, publisher, ISBN) along with owner and price, sorting
    them according to owner, and then ISBN.'''
    
def execute_query_nine():

    with engine.connect() as con:
        rows=[]
        query=''' SELECT b.ISBN ,b.title , b.publisher , u.email , c.value ,c.currancy  FROM publication p , regularbooks b ,user u , user_publication e ,cost c where p.publication_id=b.ISBN and p.state='Lost' and 
                  c.cost_id = b.cost_id and e.publication_id=p.publication_id and u.user_id=e.user_id order by u.email , b.ISBN
        '''
        keys=list(con.execute(query).keys())
        rs = con.execute(query)
        for row in rs:
            rows.append(row)
        return (rows,keys)