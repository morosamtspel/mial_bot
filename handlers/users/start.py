from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import data.config as dc
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    mycursor = dc.mydb.cursor(dictionary=True)
    current_user_id = message.from_user.id
    global user

    print(str(current_user_id) + "---")

    mycursor.execute(f"SELECT * FROM `customers` WHERE `id`=" + str(current_user_id))
    records = mycursor.fetchall()
    for row in records:
        result = row.get("id")

        print(result)

    if str(row.get('id')):
        print("yes")
    else:
        print("no")

    # sql = "INSERT INTO customers (name, id, username) VALUES (%s, %s, %s)"
    # val = (str(message.from_user.full_name), str(message.from_user.id), "@"+str(message.from_user.username))
    # mycursor.execute(sql, val)

    mycursor.execute(f"SELECT * FROM `customers` WHERE `id`=" + str(current_user_id))
    records = mycursor.fetchall()

    if "+7" in str(row.get('phone')):
        phone = str(row.get('phone'))
    else:
        phone = "Нет номера телефона у нас в базе"



    dc.mydb.commit()

    await message.answer(f"Привет, {message.from_user.full_name}! \n"
                         "Ваши данные, по нашей базе: "
                         "\nВаш id : " + str(row.get('id')) +
                         "\nСрок онончания ОФД : " + str(row.get('date_ofd_exep')) +
                         "\nСрок онончания ФН : " + str(row.get('date_fn_exep')) +
                         "\nТелефон : " + phone
                         )
