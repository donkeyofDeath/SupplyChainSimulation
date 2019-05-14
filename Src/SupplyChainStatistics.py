"""
-------------------------------------------------------
This file contains and defines the SupplyChainStatistics class.
-------------------------------------------------------
Author:  Tom LaMantia
Email:   tom@lamantia.mail.utoronto.ca
Version: February 15th 2016
-------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import ctypes

class SupplyChainStatistics:
    
    def __init__(self):
        
        #Cost statistics
        self.retailerCostsOverTime = []
        self.wholesalerCostsOverTime = []
        self.distributorCostsOverTime = []
        self.factoryCostsOverTime = []
        
        #Order statistics
        self.customerOrdersOverTime = []
        self.retailerOrdersOverTime = []
        self.wholesalerOrdersOverTime = []
        self.distributorOrdersOverTime = []
        self.factoryOrdersOverTime = []
        
        #Effective inventory statistics
        self.retailerEffectiveInventoryOverTime = []
        self.wholesalerEffectiveInventoryOverTime = []
        self.distributorEffectiveInventoryOverTime = []
        self.factoryEffectiveInventoryOverTime = []
        
        return
    
    def recordCustomerOrders(self, customerOrdersThisWeek):
        self.customerOrdersOverTime.append(customerOrdersThisWeek)
        return

    def recordRetailerOrders(self, retailerOrdersThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly order to the retailer's record.
        -------------------------------------------------------
        Preconditions: retailerOrdersThisWeek - the orders made
                 by the retailer during the given week.
        Postconditions: retailerOrdersThisWeek is appended to 
            retailerOrdersOverTime, a list which tracks the retailer's
            weekly orders.
        -------------------------------------------------------
        """
        self.retailerOrdersOverTime.append(retailerOrdersThisWeek)
        return
    
    def recordWholesalerOrders(self, wholesalerOrdersThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly order to the wholesaler's record.
        -------------------------------------------------------
        Preconditions: wholesalerOrdersThisWeek - the orders made
                 by the wholesaler during the given week.
        Postconditions: wholesalerOrdersThisWeek is appended to 
            wholesalerOrdersOverTime, a list which tracks the wholesalers's
            weekly orders.
        -------------------------------------------------------
        """
        self.wholesalerOrdersOverTime.append(wholesalerOrdersThisWeek)
        return
    
    def recordDistributorOrders(self, distributorOrdersThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly order to the distributor's record.
        -------------------------------------------------------
        Preconditions: distributorOrdersThisWeek - the orders made
                 by the distributor during the given week.
        Postconditions: distributorOrdersThisWeek is appended to 
            distributorOrdersOverTime, a list which tracks the distributor's
            weekly orders.
        -------------------------------------------------------
        """
        self.distributorOrdersOverTime.append(distributorOrdersThisWeek)
        return
    
    def recordFactoryOrders(self, factoryOrdersThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly order to the factory's record.
        -------------------------------------------------------
        Preconditions: factoryOrdersThisWeek - the orders made
                 by the factory during the given week.
        Postconditions: factoryOrdersThisWeek is appended to 
            factoryOrdersOverTime, a list which tracks the factory's
            weekly orders.
        -------------------------------------------------------
        """
        self.factoryOrdersOverTime.append(factoryOrdersThisWeek)
        return
    
    def recordRetailerCost(self, retailerCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the retailer's record.
        -------------------------------------------------------
        Preconditions: retailerCostsThisWeek - the cost (dollars)
            incurred by the retailer during the given week.
        Postconditions: retailerCostsThisWeek is appended to 
            retailerCostsOverTime, a list which tracks the retailer's
            weekly costs.
        -------------------------------------------------------
        """
        self.retailerCostsOverTime.append(retailerCostsThisWeek)
        return
    
    def recordWholesalerCost(self, wholesalerCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the wholesaler's record.
        -------------------------------------------------------
        Preconditions: wholesalerCostsThisWeek - the cost (dollars)
            incurred by the wholesaler during the given week.
        Postconditions: wholesalerCostsThisWeek is appended to 
            wholesalerCostsThisWeek, a list which tracks the wholesalers's
            weekly costs.
        -------------------------------------------------------
        """
        self.wholesalerCostsOverTime.append(wholesalerCostsThisWeek)
        return
    
    def recordDistributorCost(self, distributorCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the distributor's record.
        -------------------------------------------------------
        Preconditions: distributorCostsThisWeek - the cost (dollars)
            incurred by the distributor during the given week.
        Postconditions: distributorCostsThisWeek is appended to 
            distributorCostsThisWeek, a list which tracks the distributor's
            weekly costs.
        -------------------------------------------------------
        """
        self.distributorCostsOverTime.append(distributorCostsThisWeek)
        return
    
    def recordFactoryCost(self, factoryCostsThisWeek):
        """
        -------------------------------------------------------
        Adds a weekly cost to the factory's record.
        -------------------------------------------------------
        Preconditions: factoryCostsThisWeek - the cost (dollars)
            incurred by the factory during the given week.
        Postconditions: factoryCostsThisWeek is appended to 
            factoryCostsOverTime, a list which tracks the factory's
            weekly costs.
        -------------------------------------------------------
        """
        self.factoryCostsOverTime.append(factoryCostsThisWeek)
        return
    
    def recordRetailerEffectiveInventory(self, retailerEffectiveInventoryThisWeek):
        """
        -------------------------------------------------------
        Adds weekly effective inventory to the wholesaler's record.
        -------------------------------------------------------
        Preconditions: retailerEffectiveInventoryThisWeek - effective
            inventory of the retailer during the given week.
        Postconditions: retailerEffectiveInventoryThisWeek is appended to 
            retailerEffectiveInventoryOverTime, a list which tracks the retailer's
            effective inventory.
        -------------------------------------------------------
        """
        self.retailerEffectiveInventoryOverTime.append(retailerEffectiveInventoryThisWeek)
        return
    
    def recordWholesalerEffectiveInventory(self, wholesalerEffectiveInventoryThisWeek):
        """
        -------------------------------------------------------
        Adds weekly effective inventory to the wholesaler's record.
        -------------------------------------------------------
        Preconditions: wholesalerEffectiveInventoryThisWeek - effective
            inventory of the wholesaler during the given week.
        Postconditions: wholesalerEffectiveInventoryThisWeek is appended to 
            wholesalerEffectiveInventoryOverTime, a list which tracks the wholesalers's
            effective inventory.
        -------------------------------------------------------
        """
        self.wholesalerEffectiveInventoryOverTime.append(wholesalerEffectiveInventoryThisWeek)
        return
    
    def recordDistributorEffectiveInventory(self, distributorEffectiveInventoryThisWeek):
        """
        -------------------------------------------------------
        Adds weekly effective inventory to the distributor's record.
        -------------------------------------------------------
        Preconditions: distributorEffectiveInventoryThisWeek - effective
            inventory of the distributor during the given week.
        Postconditions: distributorEffectiveInventoryThisWeek is appended to 
            distributorEffectiveInventoryOverTime, a list which tracks the distributor's
            effective inventory.
        -------------------------------------------------------
        """
        self.distributorEffectiveInventoryOverTime.append(distributorEffectiveInventoryThisWeek)
        return
    
    def recordFactoryEffectiveInventory(self, factoryEffectiveInventoryThisWeek):
        """
        -------------------------------------------------------
        Adds weekly effective inventory to the factory's record.
        -------------------------------------------------------
        Preconditions: factoryEffectiveInventoryThisWeek - effective
            inventory of the factory during the given week.
        Postconditions: distributorEffectiveInventoryThisWeek is appended to 
            factoryEffectiveInventoryOverTime, a list which tracks the factory's
            effective inventory.
        -------------------------------------------------------
        """
        self.factoryEffectiveInventoryOverTime.append(factoryEffectiveInventoryThisWeek)
        return
    
    def plotCosts(self):
        """
        -------------------------------------------------------
        Graphs the costs of each supply chain actor.
        -------------------------------------------------------
        Preconditions: None
        Postconditions: Outputs MatplotLib chart.
        -------------------------------------------------------
        """
        plt.title("Angesammelte Kosten")
        plt.plot(self.retailerCostsOverTime, "r", label = "Einzelhandel")
        plt.plot(self.wholesalerCostsOverTime, "g", label = "Großhandel")
        plt.plot(self.distributorCostsOverTime, "b", label = "Verteiler")
        plt.plot(self.factoryCostsOverTime, "m", label="Brauerei")
        legend = plt.legend(loc='upper left', shadow=True)
        plt.ylabel("Kosten in €")
        plt.xlabel("Wochennummer")
        plt.grid(True)
    
    def plotOrders(self):
        """
        -------------------------------------------------------
        Graphs the orders of each supply chain actor.
        -------------------------------------------------------
        Preconditions: None
        Postconditions: Outputs MatplotLib chart.
        -------------------------------------------------------
        """
        plt.title("Aufgegebenen Bestellungen")
        plt.plot(self.customerOrdersOverTime, "orange", label = "Kunde")
        plt.plot(self.retailerOrdersOverTime, "r", label = "Einzelhandel")
        plt.plot(self.wholesalerOrdersOverTime, "g", label = "Großhandel")
        plt.plot(self.distributorOrdersOverTime, "b", label = "Einzelhandel")
        plt.plot(self.factoryOrdersOverTime, "m", label="Brauerei")
        legend = plt.legend(loc='upper left', shadow=True)
        plt.ylabel("Bestellungen")
        plt.xlabel("Wochennummer")
        plt.grid(True)

    
    def plotEffectiveInventory(self):
        """
        -------------------------------------------------------
        Graphs the effective inventory of each supply chain actor.
        -------------------------------------------------------
        Preconditions: None
        Postconditions: Outputs MatplotLib chart.
        -------------------------------------------------------
        """
        plt.title("Restinventar")
        plt.plot(self.retailerEffectiveInventoryOverTime, "r", label = "Einzelhandel")
        plt.plot(self.wholesalerEffectiveInventoryOverTime, "g", label = "Großhandel")
        plt.plot(self.distributorEffectiveInventoryOverTime, "b", label = "Verteiler")
        plt.plot(self.factoryEffectiveInventoryOverTime, "m", label="Brauerei")
        legend = plt.legend(loc='upper left', shadow=True)
        plt.ylabel("Restinventar in Bierkisten")
        plt.xlabel("Wochennummer")
        plt.grid(True)

    def plotStatistics(self):
        plt.figure(1)

        plt.subplot(221)
        self.plotOrders()

        plt.subplot(222)
        self.plotEffectiveInventory()

        plt.subplot(223)
        self.plotCosts()

        # Adjust the subplot layout, because the logit one may take more space
        # than usual, due to y-tick labels like "1 - 10^{-3}"
        plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                            wspace=0.35)
        
        #Shows a message
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo('User Info', 'Press "CRTL + F" to leave full screen mode')

        #Makes the image full screen,use CRTL + f to get out
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        
        #Use these statements when using Linux to maximize the Window
        """
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        """
        #Use these statements when using Windows to maximize the Window
        """
        mng = plt.get_current_fig_manager()
        mng.frame.Maximize(True)
        """
        plt.show()