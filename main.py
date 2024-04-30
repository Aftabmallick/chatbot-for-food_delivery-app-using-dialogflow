from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()

inprogress_orders = {}

@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]['name'])


    #print(parameters)
    intent_handler_dict = {
        'order.add - context: ongoing-order': add_to_order,
        #'order.remove - context: ongoing-order':remove_from_order,
        #'oredr.complete - context: ongoing-order': complete_order,
        'track.order - context: ongoing-tracking':track_order
    }   
    return intent_handler_dict[intent](parameters, session_id)



def add_to_order(parameters: dict,session_id: str):
    food_items = parameters['food-item']
    quantities = parameters['number']

    if len(food_items) != len(quantities):
        fulfillment_text = "Sorry I didn't understand. Can you pleaes specify food items and quantity?"
    else:
        new_food_dict = dict(zip(food_items,quantities))

        
        if session_id in inprogress_orders:
            current_food_dict = inprogress_orders[session_id]
            current_food_dict.update(new_food_dict)
            inprogress_orders[session_id] = current_food_dict

        else:
            inprogress_orders[session_id] = new_food_dict

        order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
        fulfillment_text=f"So far you have: {order_str}. Do you need anything else?"
    
    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

def track_order(parameters: dict):
    #print(parameters)
    order_id = int(parameters['number'])
    order_status = db_helper.get_order_status(order_id)
    if order_status:
        fulfillment_text = f"The order status for order id: {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })