function makePayment() {
  FlutterwaveCheckout({
    public_key: "FLWPUBK_TEST-5535627c18371b8185b4169bcc2c121a-X",
    tx_ref: "titanic-48981487343MDI0NzMx",
    amount: 15000,
    currency: "UGX",
    payment_options: "card, mobilemoney",
    redirect_url: "/verify",
    meta: {
      consumer_id: 23,
      consumer_mac: "92a3-912ba-1192a",
      child_id: "cedrick_j",
    },
    customer: {
      email: "rose@unsinkableship.com",
      phone_number: "08102909304",
      name: "Parent",
    },
    customizations: {
      title: "YLearn",
      description: "Add your child",
      logo: "https://www.logolynx.com/images/logolynx/22/2239ca38f5505fbfce7e55bbc0604386.jpeg",
    },
  });
}
