q_and_a = (
    ('Я - вода и по воде плаваю. Кто я?', 'льдина'),
    ('Все меня топчут, а я - всё лучше.', 'тропинка'),
    ('Что невозможно удержать и десяти минут, хотя оно легче пёрышка?', 'дыхание'),
)

def riddle(q, a):
    return q.lower() == a.lower()

print(f'Разгадайте {len(q_and_a)} загадки!')
count = 1

for q in q_and_a:
    print(f'{count} - загадка')
    print(q[0])
    user_input = input('Ваш ответ: ')

    if riddle(q[1], user_input):
        print(f'Ответ {user_input} правильный')
    else:
        print(f'Ответ неверный! Правильный ответ {q[1]}')

    count += 1