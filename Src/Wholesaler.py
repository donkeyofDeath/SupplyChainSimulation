"""
-------------------------------------------------------
This file contains and defines the Wholesaler class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""
from Settings import *
from SupplyChainActor import SupplyChainActor
from Customer import Customer

class Wholesaler(SupplyChainActor):
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue, theCustomer):
        """
        -------------------------------------------------------
        Constructor for the Wholesaler class.
        -------------------------------------------------------
        Preconditions: incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue - 
                the supply chain queues.
        Postconditions:
            Initializes the Wholesaler object in its initial state
            by calling parent constructor.
        -------------------------------------------------------
        """
        super().__init__(incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue)
        customer = theCustomer
        
        return
    
    def placeOutgoingOrder(self, weekNum):
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
        
        #RECEIVE NEW DELIVERY FROM DISTRIBUTOR
        self.receiveIncomingDelivery()    #This also advances the queue!
        
        #RECEIVE NEW ORDER FROM RETAILER
        self.receiveIncomingOrders()     #This also advances the queue!
        
        #PREPARE DELIVERY
        """
        if weekNum <= WEEK_TO_RAISE_ORDER:
            self.placeOutgoingDelivery(4)
        else:
        """
        self.placeOutgoingDelivery(self.calcBeerToDeliver())
        
        #PLACE ORDER
        self.placeOutgoingOrder(weekNum)
        
        #UPDATE COSTS
        self.costsIncurred += self.calcCostForTurn()
        
        return