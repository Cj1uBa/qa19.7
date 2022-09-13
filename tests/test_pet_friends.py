from api import PetFriends
from settings import valid_email, valid_password,valid2_password,valid2_email
import os


pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email,password=valid_password):
    status,result=pf.get_api_key(email,password)
    assert status==200
    assert 'key' in result


#bad0 проверка на ввод длинного не валидного email
def test_get_api_key_for_long_email(email='1'*10**5, password='1234'):
    status, result = pf.get_api_key(email, password)
    assert status == 400

#bad1 проверка на ввод не валидного пароля
def test_get_api_key_for_not_valid_email(email=valid_email, password='1234'):
    status, result = pf.get_api_key(email, password)
    assert status == 403

#bad2 проверка на ввод не валидного email
def test_get_api_key_for_not_valid_password(email=valid_email, password='1234'):
    status, result = pf.get_api_key(email, password)
    assert status == 403


#bad3 Проверка на ввод не валидного filter
def test_get_list_of_pets_with_not_valid_filter(filter='pets'):
        _,auth_key=pf.get_api_key(valid_email,valid_password)
        status,result=pf.get_list_of_pets(auth_key,filter)
        assert status ==500

#bad4 Добавление питомца с пустым обязательным атрибутом name
def test_add_new_pet_with_not_valid_name(name=None, animal_type='Хомяк',
                                     age='4', pet_photo='images/swin.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    if  status == 200:  print("Добавлен питомец с пустым обязательным атрибутом name")

#bad5 Добавление питомца с пустым обязательным атрибутом animal_type
def test_add_new_pet_with_not_valid_animaltype(name='Миша', animal_type=None,
                                     age='4', pet_photo='images/swin.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    if  status == 200:  print("Добавлен питомец с пустым обязательным атрибутом animal_type")

#bad6 Добавление питомца с пустым обязательным атрибутом age
def test_add_new_pet_with_not_valid_animaltype(name='Миша', animal_type='Хомяк',
                                     age=None, pet_photo='images/swin.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    if  status == 200:  print("Добавлен питомец с пустым обязательным атрибутом age")

#bad7 Добавление питомца с отрицательным атрибутом age
def test_add_new_pet_with_minus_age(name='Миша', animal_type='Хомяк',
                                     age='-500', pet_photo='images/swin.jpeg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    if  status == 200:  print("Добавлен питомец с отрицательным атрибутом age")

#Bad8 пользователь может удалить не своего питомца
def test_bed(filter='my_pets'):
    _, auth_key2 = pf.get_api_key(valid2_email, valid2_password)
    _,auth_key1= pf.get_api_key(valid_email,valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key1, filter)
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key1, "Свин", "Хомяк", "3", "images/swin.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key1, "my_pets")
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key2, pet_id)
    else:
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key2, pet_id)
    if  status == 200:  print("Пользователь удалил чужого питомца")




#Bad9 изменить чужого питомца
def test_successful_update_self_pet_info(name='Свинота', animal_type='Хомячок', age=55):
    _, auth_key2 = pf.get_api_key(valid2_email, valid2_password)
    _, auth_key1 = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key1, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key1, "Свин", "Хомяк", "3", "images/swin.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key1, "my_pets")
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.update_pet_info(auth_key2, pet_id, name, animal_type, age)
    else:
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.update_pet_info(auth_key2, pet_id, name, animal_type, age)
    if status == 200:  print("Пользователь изменил чужого питомца")
