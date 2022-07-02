function makePayment(childUsername, parentName) {
  FlutterwaveCheckout({
    public_key: "FLWPUBK_TEST-5535627c18371b8185b4169bcc2c121a-X",
    tx_ref: "ylearn-pay-" + Date.now(),
    amount: 15000,
    currency: "UGX",
    payment_options: "card, mobilemoney",
    redirect_url: "/verify",
    meta: {
      consumer_id: 23,
      consumer_mac: "92a3-912-912-912",
      child_id: childUsername,
    },
    customer: {
      email: "rose@unsinkableship.com",
      phone_number: "256787483409",
      name: parentName,
    },
    customizations: {
      title: "YLearn",
      description: "Subscribe for your child",
      logo: "https://drive.google.com/u/0/uc?id=12v4dikGvz64OxyrIy9aHW_Dh8MDOoLNZ&export=download",
    },
  });
}
