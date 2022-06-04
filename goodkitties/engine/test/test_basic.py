from goodkitties.engine.basic import generate_item


def test_generate_item():


    answers = {}

    for _ in range(1000):
        item = generate_item()
        answers[item] = answers.get(item, 0) + 1

    print(answers)