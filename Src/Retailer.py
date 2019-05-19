"""
-------------------------------------------------------
This file contains and defines the Retailer class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from Settings import *
from Customer import Customer
from SupplyChainActor import SupplyChainActor
from SupplyChainQueue import SupplyChainQueue

class Retailer(SupplyChainActor):
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue, theCustomer):
        """
        -------------------------------------------------------
        Constructor for the Retailer class.
        -------------------------------------------------------
        Preconditions: incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue - 
                the supply chain queues. Note: outgoingDeliveriesQueue and incomingOrdersQueue should be NONE.
                
                theCustomer - a customer object.
        Postconditions:
            Initializes the retailer object in its initial state
            by calling parent constructor and setting the
            retailer's customer.
        -------------------------------------------------------
        """
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        self.customer = theCustomer

        return
    
    def receiveIncomingOrderFromCustomer(self, weekNum):
        """
        -------------------------------------------------------
        Receives an order from the customer.
        -------------------------------------------------------
        Preconditions: weekNum - the current week.
        Postconditions:
            Adds the customer's order to the current orders.
        -------------------------------------------------------
        """
        self.currentOrders += self.customer.calculateOrder(weekNum)
        return
    
    def shipOutgoingDeliveryToCustomer(self):
        """
        -------------------------------------------------------
        Ships an order from the customer.
        -------------------------------------------------------
        Preconditions: None
        Postconditions: Calculates the amount of beer to be delivered
            based on the current stock. This is then added to the customer's
            total beer received. 
        -------------------------------------------------------
        """
        self.customer.recieveFromRetailer(self.calcBeerToDeliver())
        return

    def placeOutgoingOrder(self, weekNum):
        
        customerOrder = self.customer.getOrdersGivenThisWeek()
        customerOrderLastWeek = self.customer.getOrdersGivenLastWeek()
        customerDelta = customerOrderLastWeek - customerOrder
        
        if customerDelta > 0:
            targetStock = 3*customerOrder

        """
        -------------------------------------------------------
        Calculates the size of the weekly outgoing order.
        -------------------------------------------------------
        Preconditions: weekNum - the current week number.
        Postconditions:
            Calculates the order quantity using an anchor and maintain
            strategy.
        -------------------------------------------------------
        """
        #calculateAmountToOrder can be found in Settings.py
        amountToOrder=calculateAmountToOrder(self.currentOrders, self.currentStock, weekNum)
        self.outgoingOrdersQueue.pushEnvelope(amountToOrder)
        self.lastOrderQuantity = amountToOrder
        return

    def takeTurn(self, weekNum):
        
        #The steps for taking a turn are as follows:
        
        #RECEIVE NEW DELIVERY FROM WHOLESALER
        self.receiveIncomingDelivery()    #This also advances the queue!
        
        #RECEIVE NEW ORDER FROM CUSTOMER
        self.receiveIncomingOrderFromCustomer(weekNum)
        
        #CALCULATE AMOUNT TO BE SHIPPED, THEN SHIP IT
        #self.ShipOutgoingDeliveryToCustomer()
        """
        if weekNum <= WEEK_TO_RAISE_ORDER:
            self.customer.recieveFromRetailer(4)
        else:
        """
        self.customer.recieveFromRetailer(self.calcBeerToDeliver())
        
        #PLACE ORDER TO WHOLESALER
        self.placeOutgoingOrder(weekNum)
        
        #UPDATE COSTS
        self.costsIncurred += self.calcCostForTurn()
        
        return