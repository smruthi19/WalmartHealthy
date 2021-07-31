
from django.http import HttpResponse
from django.shortcuts import render

from django.http import JsonResponse

import pyodbc



vegetableslist=["Peas", "Broccoli", "Bell Peppers", "Beans", "Artichokes", "Lettuce", "Potatoes", "Tomatoes", "Cucumbers", "Spinach", "Carrots", "Cabbages", "Eggplant", "Corn", "Asparagus", "Celery", "Okra", "Brussel Sprouts", "Cauliflower", "Squash"]

fruitslist=["Apples", "Oranges", "Blueberries", "Strawberries", "Bananas", "Peaches", "Lemons", "Grapes"]
dairylist=["Yogurt", "Cheese", "Milk", "Butter", "Sour Cream", "Eggs", "Ice Cream", "Sorbet"]
drinkslist=["brown rice", "oats", "millet", "bread", "flour", "barley", "cereal", "wheat"]
# import pscycopg2
def getproducts():

    # conn = psycopg2.connect(host="localhost", port=5432, database="HealthyFoods", user="postgres", password="postgres")
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=eu-az-sql-serv1.database.windows.net;'
                          'Database=dxqmzljmaafhea4;'
                          'Trusted_Connection=no;'
                          'UID=ux2opka8z95s1se;'
                          'PWD=Mi$S9m%Tp39JJ*J56D6Rou#&q;'
)

    cursor = conn.cursor()
    rows=cursor.execute('SELECT * FROM dxqmzljmaafhea4.dbo.food')


    columns = [column[0] for column in rows.description]
    #print(columns)

    results = []
    list=[]
    products=[]
    imagelist=[]

    # image=images[0]
    # print(image.url)
    word=""
    for row in cursor.fetchmany(100):
         results.append(dict(zip(columns, row)))

    #print(results)
    for food in range(100):
        # if ("Broccoli" in results[food]["Certified_Products_Under_CROPS_Scope"]):
        temp=results[food]["Certified_Products_Under_CROPS_Scope"]
        temp=str(temp)
        list=temp.split(",")
        #print(list)
        products.append(list)
    #     for letter in range (len(temp)):
    #         if (letter!=","):
    #             word=word+temp[letter];
    #
    #         list.append(word)
    #         word=""
    #
    # print(list)

        #if ("broccoli" in temp):
        # print(results[food]["Certifier_Name"] + " " + results[food]["Operation_Name"])
        #list.append(temp);
    # print(products)
    organizedlist = []
    matches=dict(

    )
    dictionarylist=[]
    for sublist in products:
        for element in sublist:
            organizedlist.append(element)

    # print(organizedlist)

    for product in organizedlist:
        product=product.strip()
    for vegetable in vegetableslist:
        rows2=cursor.execute("Select Certifier_Name, Operation_Name, Physical_Address_Street_1, Physical_Address_City, Physical_Address_State_Province, Physical_Address_Country from dxqmzljmaafhea4.dbo.food where Certified_Products_Under_Crops_Scope LIKE ?", ("%"+vegetable+"%",));
        for row2 in rows2:
            if (row2[5]=="United States of America (the)"):
                matches.update({'vegetable': vegetable})
                matches.update({'CertifierName': row2[0]})
                matches.update({'Operation_Name': row2[1]})
                matches.update({'PhysicalAddressStreet1': row2[2]})
                matches.update({'PhysicalAddressCity': row2[3]})
                matches.update({'PhysicalAddressState':row2[4]})
                matches.update({'PhysicalAddressCountry': row2[5]})
                dictionarylist.append(matches.copy())
                print(dictionarylist)
                # matches["CertifierName"].append(row2[0])
                # matches["Operation_Name"].append(row2[1])
                # matches["Physical_Address_Street_1"].append(row2[2])
                # matches["Physical_Address_City"].append(row2[3])
                # matches["Physical_Address_State_Province"].append(row2[4])

                break;

    print(dictionarylist[0])


    # param_dict={"vegetable":vegetable}

    # print(rows2)




    # if (results.get('Certified_Products_Under_CROPS_Scope').contains("Broccoli")):
    #     print(results.get('Certifier_Name'))

    return dictionarylist




def getfruitproducts():
    print("hi")
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=eu-az-sql-serv1.database.windows.net;'
                          'Database=dxqmzljmaafhea4;'
                          'Trusted_Connection=no;'
                          'UID=ux2opka8z95s1se;'
                          'PWD=Mi$S9m%Tp39JJ*J56D6Rou#&q;'
)
    cursor = conn.cursor()
    rows=cursor.execute('SELECT * FROM dxqmzljmaafhea4.dbo.food')
    # for row in rows:
    #     print(row)
    #print(list);

    columns = [column[0] for column in rows.description]
    #print(columns)

    results = []
    list=[]
    products=[]
    imagelist=[]

    # image=images[0]
    # print(image.url)
    word=""
    for row in cursor.fetchmany(100):
         results.append(dict(zip(columns, row)))

    #print(results)
    for food in range(100):
        # if ("Broccoli" in results[food]["Certified_Products_Under_CROPS_Scope"]):
        temp=results[food]["Certified_Products_Under_CROPS_Scope"]
        temp=str(temp)
        list=temp.split(",")
        #print(list)
        products.append(list)
    #     for letter in range (len(temp)):
    #         if (letter!=","):
    #             word=word+temp[letter];
    #
    #         list.append(word)
    #         word=""
    #
    # print(list)

        #if ("broccoli" in temp):
        # print(results[food]["Certifier_Name"] + " " + results[food]["Operation_Name"])
        #list.append(temp);
    # print(products)
    organizedlist = []
    matches=dict(

    )
    dictionarylist=[]
    for sublist in products:
        for element in sublist:
            organizedlist.append(element)

    # print(organizedlist)

    for product in organizedlist:
        product=product.strip()
    for fruit in fruitslist:
        rows2=cursor.execute("Select Certifier_Name, Operation_Name, Physical_Address_Street_1, Physical_Address_City, Physical_Address_State_Province, Physical_Address_Country from dxqmzljmaafhea4.dbo.food where Certified_Products_Under_Crops_Scope LIKE ?", ("%"+fruit+"%",));
        for row2 in rows2:
            if (row2[5]=="United States of America (the)"):
                matches.update({'fruit': fruit})
                matches.update({'CertifierName': row2[0]})
                matches.update({'Operation_Name': row2[1]})
                matches.update({'PhysicalAddressStreet1': row2[2]})
                matches.update({'PhysicalAddressCity': row2[3]})
                matches.update({'PhysicalAddressState':row2[4]})
                matches.update({'PhysicalAddressCountry': row2[5]})
                dictionarylist.append(matches.copy())
                print(dictionarylist)
                # matches["CertifierName"].append(row2[0])
                # matches["Operation_Name"].append(row2[1])
                # matches["Physical_Address_Street_1"].append(row2[2])
                # matches["Physical_Address_City"].append(row2[3])
                # matches["Physical_Address_State_Province"].append(row2[4])

                break;

    print(dictionarylist[0])


    # param_dict={"vegetable":vegetable}

    # print(rows2)




    # if (results.get('Certified_Products_Under_CROPS_Scope').contains("Broccoli")):
    #     print(results.get('Certifier_Name'))

    return dictionarylist



def getdrinkproducts():

    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=eu-az-sql-serv1.database.windows.net;'
                          'Database=dxqmzljmaafhea4;'
                          'Trusted_Connection=no;'
                          'UID=ux2opka8z95s1se;'
                          'PWD=Mi$S9m%Tp39JJ*J56D6Rou#&q;'
                )
    cursor = conn.cursor()
    rows=cursor.execute('SELECT * FROM dxqmzljmaafhea4.dbo.food')
    # for row in rows:
    #     print(row)
    #print(list);

    columns = [column[0] for column in rows.description]
    #print(columns)

    results = []
    list=[]
    products=[]
    imagelist=[]

    # image=images[0]
    # print(image.url)
    word=""
    for row in cursor.fetchmany(100):
         results.append(dict(zip(columns, row)))

    #print(results)
    for food in range(100):
        # if ("Broccoli" in results[food]["Certified_Products_Under_CROPS_Scope"]):
        temp=results[food]["Certified_Products_Under_CROPS_Scope"]
        temp=str(temp)
        list=temp.split(",")
        #print(list)
        products.append(list)
    #     for letter in range (len(temp)):
    #         if (letter!=","):
    #             word=word+temp[letter];
    #
    #         list.append(word)
    #         word=""
    #
    # print(list)

        #if ("broccoli" in temp):
        # print(results[food]["Certifier_Name"] + " " + results[food]["Operation_Name"])
        #list.append(temp);
    # print(products)
    organizedlist = []
    matches=dict(

    )
    dictionarylist=[]
    for sublist in products:
        for element in sublist:
            organizedlist.append(element)

    # print(organizedlist)

    for product in organizedlist:
        product=product.strip()
    for drink in drinkslist:
        rows2=cursor.execute("Select Certifier_Name, Operation_Name, Physical_Address_Street_1, Physical_Address_City, Physical_Address_State_Province, Physical_Address_Country from dxqmzljmaafhea4.dbo.food where Certified_Products_Under_Crops_Scope LIKE ?", ("%"+drink+"%",));
        for row2 in rows2:
            if (row2[5]=="United States of America (the)"):
                matches.update({'drink': drink})
                matches.update({'CertifierName': row2[0]})
                matches.update({'Operation_Name': row2[1]})
                matches.update({'PhysicalAddressStreet1': row2[2]})
                matches.update({'PhysicalAddressCity': row2[3]})
                matches.update({'PhysicalAddressState':row2[4]})
                matches.update({'PhysicalAddressCountry': row2[5]})
                dictionarylist.append(matches.copy())
                print(dictionarylist)
                # matches["CertifierName"].append(row2[0])
                # matches["Operation_Name"].append(row2[1])
                # matches["Physical_Address_Street_1"].append(row2[2])
                # matches["Physical_Address_City"].append(row2[3])
                # matches["Physical_Address_State_Province"].append(row2[4])

                break;

    print(dictionarylist[0])


    # param_dict={"vegetable":vegetable}

    # print(rows2)




    # if (results.get('Certified_Products_Under_CROPS_Scope').contains("Broccoli")):
    #     print(results.get('Certifier_Name'))
    return dictionarylist
def getdairyproducts():

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=eu-az-sql-serv1.database.windows.net;'
                      'Database=dxqmzljmaafhea4;'
                      'Trusted_Connection=no;'
                      'UID=ux2opka8z95s1se;'
                      'PWD=Mi$S9m%Tp39JJ*J56D6Rou#&q;'

                      )
    cursor = conn.cursor()
    rows=cursor.execute('SELECT * FROM dxqmzljmaafhea4.dbo.food')
    # for row in rows:
    #     print(row)
    #print(list);

    columns = [column[0] for column in rows.description]
    #print(columns)

    results = []
    list=[]
    products=[]
    imagelist=[]

    # image=images[0]
    # print(image.url)
    word=""
    for row in cursor.fetchmany(100):
         results.append(dict(zip(columns, row)))

    #print(results)
    for food in range(100):
        # if ("Broccoli" in results[food]["Certified_Products_Under_CROPS_Scope"]):
        temp=results[food]["Certified_Products_Under_CROPS_Scope"]
        temp=str(temp)
        list=temp.split(",")
        #print(list)
        products.append(list)
    #     for letter in range (len(temp)):
    #         if (letter!=","):
    #             word=word+temp[letter];
    #
    #         list.append(word)
    #         word=""
    #
    # print(list)

        #if ("broccoli" in temp):
        # print(results[food]["Certifier_Name"] + " " + results[food]["Operation_Name"])
        #list.append(temp);
    # print(products)
    organizedlist = []
    matches=dict(

    )
    dictionarylist=[]
    for sublist in products:
        for element in sublist:
            organizedlist.append(element)

    # print(organizedlist)

    for product in organizedlist:
        product=product.strip()
        print(dairylist )
    for dairy in dairylist:
        print(dairy)
        rows2=cursor.execute("Select Certifier_Name, Operation_Name, Physical_Address_Street_1, Physical_Address_City, Physical_Address_State_Province, Physical_Address_Country from dxqmzljmaafhea4.dbo.food where Certified_Products_Under_Crops_Scope LIKE ?", ("%"+dairy+"%",));
        for row2 in rows2:
            if (row2[5]=="United States of America (the)"):
                matches.update({'dairy': dairy})
                matches.update({'CertifierName': row2[0]})
                matches.update({'Operation_Name': row2[1]})
                matches.update({'PhysicalAddressStreet1': row2[2]})
                matches.update({'PhysicalAddressCity': row2[3]})
                matches.update({'PhysicalAddressState':row2[4]})
                matches.update({'PhysicalAddressCountry': row2[5]})
                dictionarylist.append(matches.copy())
                print(dictionarylist)
                # matches["CertifierName"].append(row2[0])
                # matches["Operation_Name"].append(row2[1])
                # matches["Physical_Address_Street_1"].append(row2[2])
                # matches["Physical_Address_City"].append(row2[3])
                # matches["Physical_Address_State_Province"].append(row2[4])

                break;

    print(dictionarylist[0])


    # param_dict={"vegetable":vegetable}

    # print(rows2)




    # if (results.get('Certified_Products_Under_CROPS_Scope').contains("Broccoli")):
    #     print(results.get('Certifier_Name'))

    return dictionarylist
def index(request):
    return render (request, 'index.html')


def checkout(request):

    return render (request,'checkout.html')

def specificcart(request):

        updatedproducts= getproducts()

        indexlist=[]

        num=0;
        for num in indexlist:
            indexlist[num]=num;
            num=num+1;
        # print(list(enumerate(updatedproducts)))
        dict(zip((indexlist),updatedproducts))


        return render(request,"specificcart.html", {'updatedproducts':updatedproducts})
def drinkcart(request):

        updatedproducts= getdrinkproducts()

        indexlist=[]

        num=0;
        for num in indexlist:
            indexlist[num]=num;
            num=num+1;
        # print(list(enumerate(updatedproducts)))
        dict(zip((indexlist),updatedproducts))


        return render(request,"drinkcart.html", {'updatedproducts':updatedproducts})


def dairycart(request):

        updatedproducts= getdairyproducts()

        indexlist=[]

        num=0;
        for num in indexlist:
            indexlist[num]=num;
            num=num+1;
        # print(list(enumerate(updatedproducts)))
        dict(zip((indexlist),updatedproducts))


        return render(request,"dairycart.html", {'updatedproducts':updatedproducts})
def fruitcart(request):

        updatedproducts= getfruitproducts()

        indexlist=[]

        num=0;
        for num in indexlist:
            indexlist[num]=num;
            num=num+1;
        # print(list(enumerate(updatedproducts)))
        dict(zip((indexlist),updatedproducts))


        return render(request,"fruitcart.html", {'updatedproducts':updatedproducts})

def dairy (request):
    imagelist=[]
    updateddairyproducts=getdairyproducts()
    # for fruit in fruitslist:
    #     params = {
    #     "q": fruit,
    #     "tbm": "isch",
    #     "ijn": "0",
    #     "api_key": "bc494c7d9f1093f0ac7785ef01767bb6b2c94ed641d2911c2c2cde37a593258b"
    #     }
    #
    #     search = GoogleSearch(params)
    #     results = search.get_dict()
    #     # if (results['search_metadata']['original']!=None):
    #     imagelist.append(results['images_results'][3]['original'])
    #     print(imagelist)
    #     print("imagelist")
    return render (request, 'dairy.html', {'updateddairyproducts': updateddairyproducts, 'imagelist':imagelist})
def fruits (request):
    # from serpapi import GoogleSearch
    imagelist=[]
    updatedfruitproducts=getfruitproducts()
    # for fruit in fruitslist:
    #     params = {
    #     "q": fruit,
    #     "tbm": "isch",
    #     "ijn": "0",
    #     "api_key": "bc494c7d9f1093f0ac7785ef01767bb6b2c94ed641d2911c2c2cde37a593258b"
    #     }
    #
    #     search = GoogleSearch(params)
    #     results = search.get_dict()
    #     # if (results['search_metadata']['original']!=None):
    #     imagelist.append(results['images_results'][3]['original'])
    #     print(imagelist)
    #     print("imagelist")
    return render (request, 'fruits.html', {'updatedfruitproducts': updatedfruitproducts, 'imagelist':imagelist})
def drink (request):
    # from serpapi import GoogleSearch
    imagelist=[]
    updatedproducts=getdrinkproducts()
    # for fruit in fruitslist:
    #     params = {
    #     "q": fruit,
    #     "tbm": "isch",
    #     "ijn": "0",
    #     "api_key": "bc494c7d9f1093f0ac7785ef01767bb6b2c94ed641d2911c2c2cde37a593258b"
    #     }
    #
    #     search = GoogleSearch(params)
    #     results = search.get_dict()
    #     # if (results['search_metadata']['original']!=None):
    #     imagelist.append(results['images_results'][3]['original'])
    #     print(imagelist)
    #     print("imagelist")
    return render (request, 'drink.html', {'updatedproducts': updatedproducts, 'imagelist':imagelist})
def cart(request):
    return render (request,'cart.html')


def about(request):
    return render (request,'about.html')
def blog(request):
    return render(request, 'blog.html')
def category(request):
    import json
    updatedproducts= getproducts()
    updatedfruitproducts=getfruitproducts()
    indexlist=[]
    updatedimagelist=[]
    num=0;
    for num in indexlist:
        indexlist[num]=num;
        num=num+1;
    # print(list(enumerate(updatedproducts)))
    dict(zip((indexlist),updatedproducts))
    # print(updatedproducts)
    # from serpapi import GoogleSearch
    imagelist=[]
    # for vegetable in vegetableslist:
    #     params = {
    #     "q": vegetable,
    #     "tbm": "isch",
    #     "ijn": "0",
    #     "api_key": "bc494c7d9f1093f0ac7785ef01767bb6b2c94ed641d2911c2c2cde37a593258b"
    #     }
    #
    #     search = GoogleSearch(params)
    #     results = search.get_dict()
    #     print(results)
        # if (results['search_metadata']['original']!=None):
        # imagelist.append(results['images_results'][3]['original'])
        # print(imagelist)
        # print("imagelist")


    # for fruit in fruitslist:
        # params = {
        # "q": fruit,
        # "tbm": "isch",
        # "ijn": "0",
        # "api_key": "bc494c7d9f1093f0ac7785ef01767bb6b2c94ed641d2911c2c2cde37a593258b"
        # }
        #
        # search = GoogleSearch(params)



    return render (request,'category.html', {'updatedproducts': updatedproducts, 'imagelist':imagelist, 'updatedfruitproducts': updatedfruitproducts})
