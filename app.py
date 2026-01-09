from flask import Flask, jsonify, request
from inventory import InventoryManager, Produs

manager = InventoryManager()
app = Flask(__name__)

@app.route('/produseList', methods=['GET'])
def get_produse():
    return jsonify([p.la_dict() for p in manager.getData()])

@app.route("/produse/<int:id>", methods=["DELETE"])
def delete(id):
    if manager.sterge(id):
        return jsonify({"message": "Sters cu sucess !"}), 200
    else:
        return jsonify({"message": "Id invalid !"}), 404

@app.route("/produse/<int:id>", methods=['PATCH'])
def actualizare(id):
    data = request.get_json()
    pret = data.get('pret')
    if not pret: return jsonify({"message": "Pret invalid !"}), 400
    if pret < 0: return jsonify({"message": "Pret invalid !"}), 400
    if manager.actualizeaza_pret(id, pret):
        return jsonify({"message": "Actualizez cu sucess !"}), 200
    else:
        return jsonify({"message": "Id invalid !"}), 404
@app.route('/produse', methods=['POST'])
def addProduse():
    data = request.get_json()
    nume = data.get('nume')
    pret = data.get('pret')
    cantitate = data.get('cantitate')
    if not nume or not pret or not cantitate: return jsonify({"message": "Eroare la Valorii"}), 400
    if pret <= 0: return jsonify({"message": "Numarul trebuie sa fie unul valid"}), 400
    if cantitate <= 0: return jsonify({"message": "Cantitatea trebuie sa fie unul valid"}), 400
    if manager.adauga(nume, pret, cantitate):
        return jsonify({"message": "Adaugat cu sucess !"}), 200
    else:
        return jsonify({"message": "Eroare la adaugare !"}), 404

@app.route('/vinde', methods=["POST"])
def vinde_produs():
    data = request.get_json()
    nume = data.get('nume')
    cantitate = data.get('cantitate')
    if not cantitate: return jsonify({"message": "Eroare la cantitate"}), 400
    if not nume: return jsonify({"message": "Un nume valid te rog"}), 404
    if manager.vinde(nume, cantitate):
        return jsonify({"message": "vanzare cu success"}), 200
    else:
        return jsonify({"message": "Eroare la vanzare"}), 404


if __name__ == '__main__':
    app.run(debug=True)