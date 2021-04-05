#4th page. Checking how many are available and adding available amount to the cart.

class AddtoCart():
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.findQuantity_by_xpath = "//*[@id='qtySubTxt']/span"
        self.driver.addtocart_by_id = 'atcRedesignId_btn'
        self.driver.gotoCart_by_link_text = "Go to cart"
    

    def checkQuantity(self,driver):
        available = self.driver.find_element_by_xpath(self.driver.findQuantity_by_xpath).text
        print available
             
        def addQuantity(self):
            
            #Separating the integer from the rest of the string
            avail_string = available
            number = []
            for word in avail_string.split():
                if word.isdigit():
                    number.append(int(word))
                    print number[0]
        
            #convert integer back to string
            converted = str(number[0])
            
            #add string to the quantity block
            self.driver.find_element_by_name("quantity").clear(); 
            self.driver.find_element_by_name("quantity").send_keys(converted)
            
            
        
       
        addQuantity(self)
       
   
    def addToCart(self):    
        self.driver.find_element_by_id(self.driver.addtocart_by_id).click()
    
    def goToCart(self):
        self.driver.find_element_by_link_text(self.driver.gotoCart_by_link_text).click()
        
        
        
        
        