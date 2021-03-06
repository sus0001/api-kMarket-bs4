from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from functionalities_bs4 import kalimati_market_np, date_header_np


app = FastAPI()


@app.get("/")
def main_page():
    return {'api-endpoints': [
                            "/kalimati_market",                            
                            "/kalimati_market/commodity",
                            "/kalimati_market/unit",
                            "/kalimati_market/minimum",
                            "/kalimati_market/maximum",
                            "/kalimati_market/average",
                            
        ]}
             
        


@app.get("/kalimati_market")
def market_today():
    return {date_header_np(): {
                        "वस्तु": kalimati_market_np(0),
                        "एकाइ": kalimati_market_np(1),
                        "न्यूनतम": kalimati_market_np(2),
                        "अधिकतम": kalimati_market_np(3),
                        "औसत": kalimati_market_np(4)
                }
                }
            
            


@app.get("/kalimati_market/commodity")
def commodity():
    return {date_header_np():{
            "वस्तु": kalimati_market_np(0)}}
         
        


@app.get("/kalimati_market/unit")
def unit():
    return {date_header_np():{
            "एकाइ": kalimati_market_np(1)}}     
        


@app.get("/kalimati_market/minimum")
def minimum():
    return {date_header_np():{
            "न्यूनतम": kalimati_market_np(2)}}    
        


@app.get("/kalimati_market/maximum")
def maximum():
    return {date_header_np():{
            "अधिकतम": kalimati_market_np(3)}}    
        


@app.get("/kalimati_market/average")
def average():
    return {date_header_np():{
            "औसत": kalimati_market_np(4)}}
    
        
