#4th page. Checking how many are available and adding available amount to the cart.

class AddtoCart():
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.findQuantity_by_xpath = "//*[@id='qtySubTxt']/span"
        self.driver.clearQuantity_by_name = "quantity"
        self.driver.addNewQuantity_by_name = "quantity"
    
    

    def checkQuantity(self,driver):
        available = self.driver.find_element_by_xpath(self.driver.findQuantity_by_xpath).text
        print available
            
       ## Next step is to fiigure our how to include this in the Main function     
        def addQuantity(self,driver):
            self.driver.find_element_by_name(self.driver.clearQuantity_by_name).clear(); 
        
            #Separating the integer from the rest of the string
            avail_string = available
            number = []
            for word in avail_string.split():
                if word.isdigit():
                    number.append(int(word))
                    print number[0]
        
            #convert int back to string
            converted = str(number[0])
            return converted
        
            #add converted number to the quantity box
            #self.driver.find_element_by_name(self.driver.addNewQuantity_by_name).send_keys(converted)
        return addQuantity(driver)
       
    
    
   # def addTotheCart(self):
        
        
        
        
        
        