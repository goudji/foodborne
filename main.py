#from stockAnalysis.dataCollection import getData
from foodborne.models import randomForestRegressor

from foodborne import app
#from stockAnalysis.tdameritrade import get_movers






if __name__ == '__main__':
  

  #symbols = ['AAPL']
  #getData(symbols)

  #userStockInput = ['APPL']

  #stockInput('BTEC')

  port1=int(os.environ.get("PORT",5000))                 
  app.run(host='0.0.0.0', port=port1)
  

  #randomForestRegressor('hist/AAPL.csv')

