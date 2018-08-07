def answer(test_path):
    import time
    t0 = time.time()

    from learning import process_test_data, training_data, training_answers
    from sklearn.neural_network import MLPClassifier

    test_data = process_test_data(test_path)

    mlp = MLPClassifier()
    mlp.fit(training_data, training_answers)

    ans = mlp.predict(test_data).item()
    t1 = time.time()
    return [ans, t1 - t0]