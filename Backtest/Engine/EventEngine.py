# encoding=utf8
from Enum import EventType


class Event(object):
    """
    Event base class
    """
    pass


class MarketEvent(Event):
    """
    MarketEvent class define the event that the system receive the new bar data.
    """

    def __init__(self):
        self.type = EventType.MARKET


class OrderSendEvent(Event):
    """
    OrderSendEvent class define the event that a new order is been sent by the strategy.
    All the data should be included.
    """

    def __init__(self, symbol, order_type, lot, stoploss, takeprofit, opentime, status, openprice, spread):
        self.type = EventType.ORDER_SEND
        self.symbol = symbol
        self.order_type = order_type
        self.lot = lot
        self.stoploss = stoploss
        self.takeprofit = takeprofit
        self.opentime = opentime
        self.status = status
        self.openprice = openprice
        self.spread = spread
        self.return_list = [self.symbol, self.lot, self.order_type, ]
        #self.__print_order()

    def __print_order(self):
        """
        Output the order info
        """
        print(
                "Order:Symbol:%s,Type=%s,Lot=%s,Stoploss=%s,TakeProfit=%s" %
                (self.symbol, self.order_type, self.lot, self.stoploss, self.takeprofit)
        )


class OrderCloseEvent(Event):
    """
    OrderCloseEvent defines the event that the order is been closed by strategy.
    """

    def __init__(self, symbol, order_type, index, closetime, closeprice):
        self.type = EventType.ORDER_CLOSE
        self.symbol = symbol
        self.order_type = order_type
        self.index = index
        self.closetime = closetime
        self.closeprice = closeprice
        #self.__print_order()

    def __print_order(self):
        """
        Output order info
        """
        print(
                "Order Closed:Symbol:%s,Type=%s,Index=%s,Closetime=%s,Closeproce=%s" %
                (self.symbol, self.order_type, self.index, self.closetime, self.closeprice)
        )


class OrderModifyEvent(Event):
    """
    OrderCloseEvent defines the event that the order is been modified by strategy.
    """

    def __init__(self, symbol, order_type, index, info):
        self.type = EventType.ORDER_MODIFY
        self.symbol = symbol
        self.order_type = order_type
        self.index = index
        self.info = info
