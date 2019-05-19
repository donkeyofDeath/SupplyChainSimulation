""" 
-------------------------------------------------------
This file contains program settings and configurations.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 14th 2016
-------------------------------------------------------
"""

"""
-------------------------------------------------------
Program constants are defined here. 
-------------------------------------------------------
"""
STORAGE_COST_PER_UNIT = 1
BACKORDER_PENALTY_COST_PER_UNIT = 2

#We can play the full game since no actor is programmed to dump stock near end of game
WEEKS_TO_PLAY = 400

QUEUE_DELAY_WEEKS = 2

WEEK_TO_RAISE_ORDER_1 = 15
WEEK_TO_RAISE_ORDER_2 = 16

INITIAL_STOCK = 12

INITIAL_COST = 0

INITIAL_CURRENT_ORDERS = 0

CUSTOMER_INITIAL_ORDERS = 9
CUSTOMER_SUBSEQUENT_ORDERS_1 = 15
CUSTOMER_SUBSEQUENT_ORDERS_2 = 20

#This is only needed in the calculateAmountToOrder function
TARGET_STOCK = 40


def calculateAmountToOrder(incomingOrder, stock, weekNum):
    #First weeks are in equilibrium
    targetStock=TARGET_STOCK
    """
    if weekNum <= WEEK_TO_RAISE_ORDER:
        amountToOrder = CUSTOMER_INITIAL_ORDERS
    #After first few weeks, the actor chooses the order. We use "anchor and maintain" strategy.
    else:
    """
    #We want to cover any out flows, we know that there are some orders in the pipeline.
    amountToOrder = 0.5 * incomingOrder
    if (targetStock - stock) > 0:
        amountToOrder += targetStock - stock
    return(amountToOrder)