@app.route("/client_token",methods=["GET"])
def client_token():
    return gateway.client_token.generater()

