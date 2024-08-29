immutable_var = 1,2,3,"Облака"
print ('Immutable tuple:',immutable_var)
# immutable_var[0] = 200 - Не могу добавить/изменить данный элемент, так как Кортеж относится к неизменяемому типу данных.
mutable_list = [1,2,3,"Облака"] # Благодаря элементу "список[]"- я смог добавить/изменить элемент внутри Кортежа.
mutable_list[3]='Тучи'
print ('Mutable list:',mutable_list)


