from datetime import datetime
from http import HTTPStatus
from uuid import UUID
from starlette.responses import Response
from starlette import status

from orders.app import app

order = {
    'id': 'asdzxc',
    'status': 'delivered',
    'created': datetime.now(),
    'order': [
        {
            'product': 'cappuccino',
            'size': 'medium',
            'quantity': 1
        }
    ]
}

@app.get('/orders')
def get_orders():
    return {'orders': [order]}

@app.post('/orders', status_code=status.HTTP_201_CREATED)
def create_order(order_id: UUID):
    return order

@app.put('/orders/{order_id}', )
def update_order(order_id: UUID):
    return order

@app.delete('/orders/{order_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: UUID):
    return order

@app.post('/orders/{order_id}/pay')
def pay_order(order_id: UUID):
    return order