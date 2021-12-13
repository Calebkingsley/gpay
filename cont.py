class cont:
    
    def __init__(self,name,induvidual,phonenumber,lc):
        self.name=name
        self.identity=induvidual,
        self.mobilenumber=phonenumber
        self.lastcontacted=lc

    def contact_open(self):
        print("display contact")
        

    def name_verificaton(self):
        if type(self.name)==str:
            if(self.name)!=0:
                print("This person is available in contact")
            else:
                raise ValueError("the contact here is null")
        else:
            raise TypeError("this contact is is available")

    def mobile_verification(self):
        
        
        if (len(self.mobilenumber))==10:
                print("phone number verified")
            
        else:
            raise ValueError("the phone number should not be grater than or lesser than 10")
                
           
    def identity_verification(self):
        if (self.identity)==str:
            if type(self.identity)=="friend":
                print("this is a friend")
                
            else:
                print("this is a family friend")

                
                    
        else:
             print("this is a invlaid contact")
        
    


    def lastcontected_verification(self):
        if type(self.lastcontacted)==str:
            print("information available")
        else:
            raise ValueError("no information available")
        
            
