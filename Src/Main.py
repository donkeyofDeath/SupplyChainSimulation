"""
-------------------------------------------------------
The main program. The main program handles the simulation
by co-ordinating the game. This involves incrementing all of the
communication queues between the different parts of the system.

The main program also acts as the customer, receiving the
product at the end of the supply chain system.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 14th 2016
-------------------------------------------------------
"""

from Settings import *
from Customer import Customer
from SupplyChainQueue import SupplyChainQueue
from Retailer import Retailer
from Wholesaler import Wholesaler
from Distributor import Distributor
from Factory import Factory
from SupplyChainStatistics import SupplyChainStatistics

"""
-------------------------------------------------------
Given two SupplyChainActors B <--> A, where
A is higher in the supply chain, let "top queue" denote A's
outgoingOrderQueue/B's incomingOrderQueue. Let "bottom queue"
denote B's outgoingDeliveryQueue/A's incoming delivery queue. 
-------------------------------------------------------
"""
wholesalerRetailerTopQueue = SupplyChainQueue(QUEUE_DELAY_WEEKS)
wholesalerRetailerBottomQueue = SupplyChainQueue(QUEUE_DELAY_WEEKS)

distributorWholesalerTopQueue = SupplyChainQueue(QUEUE_DELAY_WEEKS)
distributorWholesalerBottomQueue = SupplyChainQueue(QUEUE_DELAY_WEEKS)

factoryDistributorTopQueue = SupplyChainQueue(QUEUE_DELAY_WEEKS)
factoryDistributorBottomQueue = SupplyChainQueue(QUEUE_DELAY_WEEKS)

"""
-------------------------------------------------------
Each queue should have at least 2 orders of size CUSTOMER_INITIAL_ORDER 
-------------------------------------------------------
"""
for i in range(0,2):
    wholesalerRetailerTopQueue.pushEnvelope(CUSTOMER_INITIAL_ORDERS)
    wholesalerRetailerBottomQueue.pushEnvelope(CUSTOMER_INITIAL_ORDERS)
    distributorWholesalerTopQueue.pushEnvelope(CUSTOMER_INITIAL_ORDERS)
    distributorWholesalerBottomQueue.pushEnvelope(CUSTOMER_INITIAL_ORDERS)
    factoryDistributorTopQueue.pushEnvelope(CUSTOMER_INITIAL_ORDERS)
    factoryDistributorBottomQueue.pushEnvelope(CUSTOMER_INITIAL_ORDERS)

"""
-------------------------------------------------------
Now we initialize our SupplyChainObjects. Passing the correct
queues is essential.
-------------------------------------------------------
"""

theCustomer = Customer()
myRetailer = Retailer(None, wholesalerRetailerTopQueue, wholesalerRetailerBottomQueue, None, theCustomer)

myWholesaler = Wholesaler(wholesalerRetailerTopQueue, distributorWholesalerTopQueue,
                          distributorWholesalerBottomQueue, wholesalerRetailerBottomQueue)

myDistributor = Distributor(distributorWholesalerTopQueue, factoryDistributorTopQueue,
                            factoryDistributorBottomQueue, distributorWholesalerBottomQueue)

myFactory = Factory(factoryDistributorTopQueue, None, None, factoryDistributorBottomQueue, QUEUE_DELAY_WEEKS)

#Initialize Statistics object
myStats = SupplyChainStatistics()

"""
-------------------------------------------------------
Main game-play!
-------------------------------------------------------
"""

for thisWeek in range(0, WEEKS_TO_PLAY):
    
    print("--- Week {0} ---".format(thisWeek))
    
    myStats.recordCustomerOrders(theCustomer.getOrdersGivenThisWeek())

    #Retailer takes turn, update stats
    myRetailer.takeTurn(thisWeek)
    myStats.recordRetailerCost(myRetailer.getCostIncurred())
    myStats.recordRetailerOrders(myRetailer.getLastOrderQuantity())
    myStats.recordRetailerEffectiveInventory(myRetailer.calcEffectiveInventory())
    print("Retailer Complete")
    
    #Wholesaler takes turn, update stats
    myWholesaler.takeTurn(thisWeek)
    myStats.recordWholesalerCost(myWholesaler.getCostIncurred())
    myStats.recordWholesalerOrders(myWholesaler.getLastOrderQuantity())
    myStats.recordWholesalerEffectiveInventory(myWholesaler.calcEffectiveInventory())
    print("Wholesaler Complete")
    
    #Distributor takes turn, update stats
    myDistributor.takeTurn(thisWeek)
    myStats.recordDistributorCost(myDistributor.getCostIncurred())
    myStats.recordDistributorOrders(myDistributor.getLastOrderQuantity())
    myStats.recordDistributorEffectiveInventory(myDistributor.calcEffectiveInventory())
    print("Distributor Complete")
    
    #Factory takes turn, update stats
    myFactory.takeTurn(thisWeek)
    myStats.recordFactoryCost(myFactory.getCostIncurred())
    myStats.recordFactoryOrders(myFactory.getLastOrderQuantity())
    myStats.recordFactoryEffectiveInventory(myFactory.calcEffectiveInventory())
    print("Factory Complete")

print("--- Final Statistics ----")
print("Beer received by customer: {0}".format(theCustomer.getBeerReceived()))
"""
myStats.PlotCosts()
myStats.PlotOrders()
myStats.PlotEffectiveInventory()
"""
myStats.plotStatistics()