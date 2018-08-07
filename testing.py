def test_algorithm(answer_func):
    from learning import training_answers

    for i in range(1,21):
        try:
            ans = answer_func('pictures/ato' + str(i) + '.jpg')
        except:
            ans = answer_func('pictures/ato' + str(i) + '.jpeg')
        print("The image is an " +
              str(training_answers[i-1]) +
              ", the data says its a " + str(ans[0]) +
              ", and the whole process took about " +
              str(round(ans[1])) + " seconds.")


def test_custom(answer_func, img_path):
    print(answer_func(img_path))