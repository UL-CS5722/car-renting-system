"""A separate class for Price"""
class Total:
  
    """Constructor function wth price and discount"""
  
    def __init__(self, price, cust_id, cust_type = None):
          
        """take price and discount strategy"""
          
        self.price = price
        self.cust_type = cust_type
        self.cust_id = cust_id
        
          
    """A separate function for price after customer type"""
  
    def price_after_discount(self):
          
        if self.cust_type:
            discount = self.cust_type(self)
        else:
            discount = 0
              
        return self.price - discount
  
    def __repr__(self):
          
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())
  
"""function dedicated to On Sale Discount"""
def premium_customer(order):
      
    return order.price * 0.20
  
"""function dedicated to 20 % discount"""
def classic_customer(order):
    
    return order.price * 0.30
  
"""main function
if __name__ == "__main__":
  
    '''price value will be derived from the booking record'''
    print(Total(20000, 1))
      
    #with discount strategy as 20 % discount
    print(Total(20000, cust_type = classic_customer, cust_id= 1))
  
    #with discount strategy as On Sale Discount
    print(Total(20000, cust_type = premium_customer, cust_id= 1))"""