"""
-------------------------------------------------------
This file contains and defines the SupplyChainActor class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 7th 2016
-------------------------------------------------------
"""

from Settings import *
from SupplyChainQueue import SupplyChainQueue

class SupplyChainActor:
    
    def __init__(self, incomingOrdersQueue, outgoingOrdersQueue, incomingDeliveriesQueue, outgoingDeliveriesQueue):
        """
        -------------------------------------------------------
        Constructor for the SupplyChainActor class. All other
        supply chain actors (Retailer, Wholesaler, Distributor, Factory)
        are derived from this class. 
        -------------------------------------------------------
        Preconditions:
            incomingOrdersQueue - queue for incoming orders.
            outgoingOrdersQueue - queue for outgoing orders.
            incomingDeliveriesQueue - queue for incoming deliveries.
            outgoingDeliveriesQueue - queue for outgoing deliveries.
            
        Postconditions:
            Initializes the SupplyChainActor object in its initial state.
        -------------------------------------------------------
        """
        self.currentStock = INITIAL_STOCK
        self.currentOrders = INITIAL_CURRENT_ORDERS
        self.costsIncurred = INITIAL_COST
        
        self.incomingOrdersQueue = incomingOrdersQueue
        self.outgoingOrdersQueue = outgoingOrdersQueue
        self.incomingDeliveriesQueue = incomingDeliveriesQueue
        self.outgoingDeliveriesQueue = outgoingDeliveriesQueue
        
        self.lastOrderQuantity = 0
        return
    
    def placeOutgoingDelivery(self, amountToDeliver):
        """
        -------------------------------------------------------
        Places a delivery to the actor one level higher in the supply
        chain.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Places the delivery. Note: the advancement
            of the queues is handled by the main program.
        -------------------------------------------------------
        """
        self.outgoingDeliveriesQueue.pushEnvelope(amountToDeliver)
        return
    
    def receiveIncomingDelivery(self):
        """
        -------------------------------------------------------
        Receives a delivery from the actor one level lower in
        the supply chain.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Updates the current stock based on the incoming
            deliveries queue.
        -------------------------------------------------------
        """
        quantityReceived = self.incomingDeliveriesQueue.popEnvelope()
        
        if quantityReceived > 0:
            self.currentStock += quantityReceived
                
        return
    
    def receiveIncomingOrders(self):
        """
        -------------------------------------------------------
        Receives an incoming order from from the actor one level higher in
        the supply chain.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Updates the current orders based on the incoming
            deliveries queue.
        -------------------------------------------------------
        """
        thisOrder = self.incomingOrdersQueue.popEnvelope()
        
        if thisOrder > 0:
            self.currentOrders += thisOrder
        return
    
    def calcBeerToDeliver(self):
        """
        -------------------------------------------------------
        Calculates how much beer to deliver to the customer. The
        current stock and number of cases currently on order by the
        customer are updated from within this function.
        -------------------------------------------------------
        Preconditions: 
            None
        Postconditions:
            Returns deliveryQuantitiy - the number of cases to be delivered
            to the customer. currentOrders, currentStock are
            updated to reflect this delivery quantity. 
        -------------------------------------------------------
        """
        deliveryQuantity = 0
        
         #If we can fill the customer's order, we must do it.
        if self.currentStock >= self.currentOrders:
            deliveryQuantity = self.currentOrders
            self.currentStock -= deliveryQuantity
            self.currentOrders -= deliveryQuantity
        #If the current stock cannot cover the order, we must fill as much as we can, and back-order the rest.
        elif self.currentStock >= 0 and self.currentStock < self.currentOrders:
            deliveryQuantity = self.currentStock
            self.currentStock = 0
            self.currentOrders -= deliveryQuantity

        return deliveryQuantity
    
    def calcCostForTurn(self):
        """
        -------------------------------------------------------
        This function calculates the total costs incurred for the
        current turn. 
        -------------------------------------------------------
        Preconditions: This program must be called LAST in the turn
            sequence to account for orders taken and deliveries.
        Postconditions:
            Returns costsThisTurn - the total cost incurred during
            this turn.
        -------------------------------------------------------
        """
        costsThisTurn = 0
        
        inventoryStorageCost = self.currentStock * STORAGE_COST_PER_UNIT
        backorderPenaltyCost = self.currentOrders * BACKORDER_PENALTY_COST_PER_UNIT
        
        costsThisTurn = inventoryStorageCost + backorderPenaltyCost
        
        return costsThisTurn
    
    def getCostIncurred(self):
        """
        -------------------------------------------------------
        Returns the total costs incurred. 
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: Returns self.costsIncurred
        -------------------------------------------------------
        """
        return self.costsIncurred
    
    def getLastOrderQuantity(self):
        """
        -------------------------------------------------------
        Returns the quantity of the last order made. 
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: Returns self.lastOrderQuantity
        -------------------------------------------------------
        """
        return self.lastOrderQuantity
    
    def calcEffectiveInventory(self):
        """
        -------------------------------------------------------
        Returns the effective inventory of the calling SupplyChainActor
        during the week the method is called.
        -------------------------------------------------------
        Preconditions: None.
        Postconditions: Returns the effective inventory, which
            is defined as self.currentStock - self.currentOrders.
        -------------------------------------------------------
        """
        return (self.currentStock - self.currentOrders)