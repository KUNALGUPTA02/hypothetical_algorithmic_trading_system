# hypothetical_algorithmic_trading_system
>The trading system is designed to handle several users, and each user has a random suite of strategies.
>A strategy is simply an algorithm that buys/sells a select group of stocks according to some logic.
>Each strategy can trade in a random group of stocks.
>In this i am design an API that handles order placement for this system. Order will come in for a particular stock inside a particular strategy.
>Our API will thus take in the following parameters: STRATEGY, INSTRUMENT, POSITION. These parameters represent an incoming order.
>STRATEGY represents which strategy the order is for. INSTRUMENT represent which instrument is to be traded. POSITION is either "BUY" or "SELL". It represent whether that strategy is buying or selling a certain stock. A sell cannot take place without a prior buy. If a strategy has already bought that instrument, it cannot re-buy that instrument again, until it has sold. In either case, the order would be invalid.
>Our API must decide which users an incoming order is valid for, if at all, and then buy/sell. 

For example :
>Consider we have a user named "Holland Proctor", who trades in 2 strategies named "STRATEGY_A" and "STRATEGY_B". "STRATEGY_A" trades in the following instruments: "BIRLASOFT","GRASIM" and "EICHER". "STRATEGY_B" trades in "MINDA". We have another user named "Oaklee Wagner", who trades in only 1 strategy "STRATEGY_D" which only trades in "ACC".
>Now let's say our first order (Order #1) has the following parameters: "STRATEGY_A", "GRASIM", "SELL". This is an invalid order, as STRATEGY_A is yet to buy GRASIM in the first place.
>The next order (Order #2) has the following parameters: "STRATEGY_B", "MINDA", "BUY". This is a valid order that only applies to "Holland Proctor". Your system must register this buy.
>The next order (Order #3) has the following parameters: "STRATEGY_D", "INFY", "BUY". This order is invalid for both users, and thus, is rejected.
>The next order (Order #4) has the following parameters: "STRATEGY_A", "MINDA", "SELL". Order #2 already bought that instrument for Holland Proctor. The order is thus valid, and the buy position should be deleted for that user.

In brief, our system thus decides if an incoming order is valid or not, and if it's valid, it acts upon it by placing the corresponding buy or sell for the right users and strategies. Your system must thus:
>Keep track of all existing buy orders that are yet to be sold.
>Keep track of those buys in a permanent way (via a database/Json). Your system must be resilient to shutdowns/crashes.
>Bonus points for maintaining a permanent "order log", a history of past buys and sells which have since been closed.
>The status of the order (Rejected/accepted) must be returned by the API.

SETUP:
>Our code is in python.  
>Project contains the following directories: 
1. Jsons: Contains json files that are nessecary for execution.
2. Logs: The project comes packaged with a logging script, that writes to files inside the Logs folder. We are use of that module to track our API's execution .
3. Scripts: Python scripts nessecary for execution. We work with Order_Handler.py. Feel free to create any new python scripts if you so desire.
> To start, run Generate_User_Profile.py. This will create a json of random user profiles which will appear in the Jsons folder.
> Next, run Order_Handler.py. This is a FastAPI code which we will have to work on. And we have to install certain dependencies to get it running. Setting up the right modules . The command to start it is "uvicorn Order_Handler:app --host 0.0.0.0 --port 8080". The API is to be hosted on port 8080. 
> Next, on a different terminal, run Order_Producer.py. It will produce random orders in a 1s interval that will go to the API at Order_Handler.py. Currently, the Order_Handler API only prints out the orders it receives. 

