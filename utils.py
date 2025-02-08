def customer_stats_utils(customers, invoices, payments):
    for customer in customers:
        customer_id = customer.get('id')
        customer['invoices'] = [invoice for invoice in invoices if invoice.get("customerId") == customer_id]
        customer['payments'] = [payment for payment in payments if payment.get("customerId") == customer_id]
        customer['invoice_total'] = sum([invoice['total'] for invoice in customer['invoices']])
        customer['payment_total'] = sum([payment['amount'] for payment in customer['payments']])
    return customers

