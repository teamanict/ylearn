function makePayment() {
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
      child_id: "cedrick_j",
    },
    customer: {
      email: "rose@unsinkableship.com",
      phone_number: "256787483409",
      name: "",
    },
    customizations: {
      title: "YLearn",
      description: "Subscribe for your child",
      logo: "https://www.logolynx.com/images/logolynx/22/2239ca38f5505fbfce7e55bbc0604386.jpeg",
    },
  });
}
