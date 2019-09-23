# Multisafepay integration #

This package enables you to use a Multisafepay payment provider. 
It is a very minimal implementation, using the now deprecated xml api of Multisafepay.

The team at Multisafepay has now produced their own python integration package
'multisafepay' that can found on PyPI. That package is built on top of the current
Multisafepay json API.

This package started its life under the name 'multisafepay', but has now been renamed to 'mini-multisafepay'.

The original name has been donated to the Multisafepay developers, so that they can
provide their canonical implementation under the proper name.

A minimal example (for explanation of the arguments, see MSP documentation):

```
    transaction = Transaction(
        account="a",
        site_id="b",
        site_secure_code="c",
        notification_url="http://localhost/notify",
        cancel_url="",
        locale="nl_NL",
        ipaddress="1.2.3.4",
        email="test@example.com",
        transaction_id="1234",
        amount="2300",
        description="party",
        api_url="http://localhost:9000/ok",
        redirect_url="http://localhost:9000/success",
    )
    payment_url = transaction.start()

    # Now redirect the user to the payment_url, located on the Multisafepay servers
```

For more documentation have a look at the tests ("test_msp.py").
