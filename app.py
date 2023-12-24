from flask import request, render_template, url_for, Flask
import random

app = Flask(__name__)

flowers = {
    1: {'name': 'Ромашковое настроение', 'description': 'Свежие ромашки с луга...', 'price': '1500 руб.', 'delivery_time': '2 часа', 'image_filename': 'flower1.jpg'},
    2: {'name': 'Розовая фантазия', 'description': 'Нежные розы для вашей любимой...', 'price': '2500 руб.', 'delivery_time': '3 часа', 'image_filename': 'flower2.jpg'},
    3: {'name': 'Прекрасное счастье', 'description': 'Прелесть в запахе цветов...', 'price': '1300 руб.', 'delivery_time': '2 часа', 'image_filename': 'flower3.jpg'},
    4: {'name': 'Летнее настроение', 'description': 'Яркие краски лета в каждом лепестке...', 'price': '2000 руб.', 'delivery_time': '1 час', 'image_filename': 'flower4.jpg'},
    5: {'name': 'Осенний вальс', 'description': 'Теплые тона осени для уюта в вашем доме...', 'price': '1800 руб.', 'delivery_time': '1.5 часа', 'image_filename': 'flower5.jpg'},
    6: {'name': 'Зимний рассвет', 'description': 'Свежесть зимнего утра в каждом букете...', 'price': '2200 руб.', 'delivery_time': '2.5 часа', 'image_filename': 'flower6.jpg'},
}

@app.route('/')
def home():
    return render_template('home.html', flowers=flowers)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/how-to-order')
def how_to_order():
    return render_template('how_to_order.html')

@app.route('/flower/<int:flower_id>')
def flower_profile(flower_id):
    flower = flowers.get(flower_id)
    if flower:
        # Добавляем 'id' к словарю 'flower' для использования в шаблоне
        flower['id'] = flower_id
        return render_template('profile.html', flower=flower)
    else:
        return 'Цветок с таким ID не найден', 404


@app.route('/place_order', methods=['POST'])
def place_order():
    flower_id = request.form.get('flower_id')
    if not flower_id or not flower_id.isdigit():
        return "Некорректный ID цветка.", 400

    flower_id = int(flower_id)
    flower = flowers.get(flower_id)
    if not flower:
        return "Цветок с таким ID не найден.", 404

    # Попытка получить quantity и преобразовать его в целое число
    quantity_str = request.form.get('quantity', '1')
    if not quantity_str.isdigit():
        return "Некорректное количество.", 400
    quantity = int(quantity_str)

    # Убираем " руб." из цены и преобразуем в целое число
    price = int(flower['price'].replace(' руб.', ''))

    # Рассчитываем общую стоимость
    total_price = quantity * price

    # Получаем примечание к заказу, оно может быть пустым
    note = request.form.get('note', '')

    # Генерация случайного номера заказа
    order_number = random.randint(1000, 9999)

    # Получение данных о доставке
    address = request.form.get('address')
    apartment = request.form.get('apartment')
    floor = request.form.get('floor')
    entrance = request.form.get('entrance')

    # Перенаправление на страницу подтверждения заказа с номером заказа
    return render_template('order_confirmation.html',
                           flower_name=flower['name'],
                           quantity=quantity,
                           comment=request.form.get('comment', ''),
                           order_number=order_number,
                           total_price=f"{total_price} руб.",
                           delivery_time=flower['delivery_time'],
                           address=address,
                           apartment=apartment,
                           floor=floor,
                           entrance=entrance)

@app.route('/create_flower')
def create_flower():
    return render_template('create_flower.html')

@app.route('/new_order_confirmation')
def new_order_confirmation():
    return render_template('new_order_confirmation.html')



if __name__ == '__main__':
    app.run(debug=True)


