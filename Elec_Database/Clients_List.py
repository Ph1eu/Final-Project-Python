from Elec_Database import Client
import datetime
import pickle

class Clients_List:
    """
    This class contain a list of all our Clients in the area
    
    Main function get display on the GUI:
        + FindClientsListbyInput(input) : 
            - Work as a search engine for the panel.
            - Return a list of all clients have the input in ID
            - Call at every key pressed

        + CreateNewClient() :
            - Create a pop up clients panel with textbox for user input (See more at Clients)
            - Need to get Contact_ID - Owner_Name - Address - Info - E_Mode to create
            - Return True when validated, the new client get add to the list   
                     False when the new ID already exist,the new client throw away

        + For now, there is no way to delete a Client out of the list, the current option is to close the contract and left :v

    GUI: 
        +a Big box show .Today
        +A small button for New_day to Simmulate a day passing by, refresh panel each time click to update time
        +A search bar and a javax.swing.JList alike to display every clients correct :v
        +THis is a Jlist of button to click on each clients and get pop up clients panel of that clients
        +A buttton to add clients
       
    
    
    """
    def __init__(self,Today) -> None:
        self.List=[]
        self.Today=Today

    def Cell(self,id,obj):
        return {'id':id,'Client_Object':obj}    

    def CountClients(self):
        return len(self.List)

    def CheckIDexist(self,id):
        return any(d['id'] == id for d in self.List)
               
    def Save_CL(self):
        file_cl = open('Object_Folder/Client_L.obj', 'wb')
        pickle.dump(self,file_cl)
        file_cl.close()

    def CreateNewClient(self,Contact_ID,Owner_Name,Address,Info,E_Mode):
        a=Client.Client(self.Today)
        a.UpdateInput(Contact_ID,Owner_Name,Address,Info,E_Mode)       
        Check=self.CheckIDexist(Contact_ID)
        if Check:
            print("Error ! ID duplicate")
        else:
            print("OK")
            self.List.append(self.Cell(Contact_ID,a))
        return not Check

    def FindClientsListbyInput(self,text):
        return [d for d in self.List if text in d['id']]

    def GetUsageDay(self):
        return [d['Client_Object'].Energy_Usage for d in self.List]

    def New_day(self,Today):
        self.Today=Today
        c=[]
        for d in self.List:
            d['Client_Object'].New_day(Today)
            a = {"Id":d['Client_Object'].Contract_ID,"Date":Today,"Energy Usage":d['Client_Object'].Energy_Usage}
            c.append(a)
        return c  

    def ListOfDict(self):
        return [d['Client_Object'].ToDict() for d in self.List]
